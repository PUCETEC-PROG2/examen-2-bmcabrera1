from django.db import models

class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=200, null=False)
    directorName = models.CharField(max_length=200, null=False)
    year = models.IntegerField(null=False)
    sinopsis = models.TextField(max_length=2000)
    
    def __str__(self) -> str:
        return self.title