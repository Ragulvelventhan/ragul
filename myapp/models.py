from django.db import models

# Create your models here.
class datas(models.Model):
    pid=models.IntegerField()
    fname=models.CharField(max_length=200)
    files=models.FileField(upload_to='files')
    def __str__(self):
        return self.fname
