from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    # show title on admin dashboard

    def __str__(self):
        return self.title
