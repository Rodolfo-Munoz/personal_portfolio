from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=2002)
    date = models.DateField()
    text = models.TextField()


