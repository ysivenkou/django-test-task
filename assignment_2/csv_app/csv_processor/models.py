import datetime
from django.db import models


class CsvFile(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d/')

    def delete(self, *args, **kwargs):
        self.file.delete()
        super(CsvFile, self).delete(*args, **kwargs)