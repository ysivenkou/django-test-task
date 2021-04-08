from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.views.generic.base import View
from django.conf import settings
from django.http import HttpResponse

from csv_processor.forms import CsvFileForm

import pandas as pd
import numpy as np
import os



class UploadCsvView(View):
    def get(self, request):
        form = CsvFileForm()
        return render(request, 'csv_processor/upload.html', context={'form': form})

    def post(self, request):
        form = CsvFileForm(request.POST, request.FILES)
        if not form.is_valid():
            return redirect('upload_csv')
        csv_file = form.save()
        df = pd.read_csv(csv_file.file)
        context = {}
        context['csv_html'] = mark_safe(df.to_html())
        context['csv_name'] = csv_file.file.name.split('/')[-1]
        context['csv_path'] = csv_file.file.name
        context['pivot_options_index_and_column'] = [column[0] for column in dict(df.dtypes).items() if column[1] == np.dtype('O')]
        context['pivot_options_values'] = [column[0] for column in dict(df.dtypes).items() if column[1] != np.dtype('O')]
        return render(request, 'csv_processor/dataframe.html', context=context)



class PivotTableView(View):
    def post(self, request):
        index_choise = request.POST['index-choises']
        column_choise = request.POST['column-choises']
        value_choise = request.POST['value-choises']
        csv_path = request.POST['csv_path']
        df = pd.read_csv(os.path.join(settings.MEDIA_ROOT, csv_path))
        if index_choise == column_choise:
            return HttpResponse("Please, select different values for index and column", status=400)
        pivot_table = df.pivot_table(
            index=index_choise,
            columns=column_choise,
            values=value_choise,
            aggfunc='sum'
        )
        pivot_html = mark_safe(pivot_table.to_html())
        return render(request, 'csv_processor/pivot.html', context={'pivot_html': pivot_html}, status=200)