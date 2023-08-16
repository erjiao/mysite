from django.db import models


# Create your models here.


class Status(models.TextChoices):
    UNSTARTED = 'u', 'Not Started yet'
    ONGOING = 'o', 'Ongoing'
    FINISHED = 'f', 'Finished'


class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=200, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices,
                              default=Status.UNSTARTED)

    def __str__(self):
        return self.name
