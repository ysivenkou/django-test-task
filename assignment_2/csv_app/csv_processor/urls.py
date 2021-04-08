from django.urls import path
from csv_processor.views import UploadCsvView, PivotTableView


urlpatterns = [
    path('', UploadCsvView.as_view(), name='upload_csv'),
    path('pivot/', PivotTableView.as_view(), name='build_pivot')
]