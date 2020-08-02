from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=2002)
    date = models.DateField()
    text = models.TextField()

    # This function returns the name of the objects
    def __str__(self):
        return self.title



