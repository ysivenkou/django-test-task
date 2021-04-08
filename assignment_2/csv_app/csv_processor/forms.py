from django.forms import Form, ModelForm
from csv_processor.models import CsvFile


class CsvFileForm(ModelForm):
    class Meta:
        model = CsvFile
        fields = '__all__'