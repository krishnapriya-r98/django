from django.db import models


class users(models.Model):
    user_id = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    team_id = models.CharField(max_length=5)
    class Meta:
        db_table = "Users"


class teams(models.Model):
    team_id = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    class Meta:
        db_table = "Teams"