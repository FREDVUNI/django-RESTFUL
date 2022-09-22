from django.db import models

# Create your models here.
class companies(models.Model):
    name = models.CharField(max_length=25)
    products =models.CharField(max_length=50)

    def __str__(self):
        return self.name

class blog(models.Model):
    post = models.CharField(max_length=50)
    author = models.CharField(max_length=25)
    title = models.CharField(max_length=80)

    def __str__(self):
        return self.post        