from django.db import models
# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    author_email = models.EmailField(null=True, blank=True)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
