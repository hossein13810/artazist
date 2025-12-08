from django.db import models

from auth_app.models import UsersData


class WalletsData(models.Model):
    user_data = models.ForeignKey(UsersData, blank=True, null=True, on_delete=models.CASCADE)
    inventory = models.IntegerField(blank=True, null=True)
    sheba_number = models.CharField(max_length=200, blank=True, null=True)
