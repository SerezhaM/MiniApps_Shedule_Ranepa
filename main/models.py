from django.db import models


class Customer(models.Model):
    kurs = models.CharField(max_length=2)
    group = models.CharField(max_length=10)

    def __str__(self):
        return self.kurs + "-" + self.group
