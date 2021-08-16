from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list
from django.db import models


class CBU(models.Model):
    unit = models.PositiveIntegerField()
    reach = models.CharField(validators=[validate_comma_separated_integer_list], max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Owner- {self.owner}, unit:{self.unit}"
