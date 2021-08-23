from django.contrib.auth.models import User
from django.db import models


class CBU(models.Model):
    unit = models.PositiveIntegerField()
    reach = models.CharField(max_length=60)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Owner- {self.owner}, unit:{self.unit}"
