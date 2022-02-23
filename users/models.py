from django.db import models
from django.core.validators import RegexValidator

alphaSpaces = RegexValidator(r'^[a-zA-Z ]+$', 'Only letters and spaces are allowed')
phone_regex = RegexValidator(regex=r'[1-9][0-9]{9,14}', message="Only accepts 10 to 15 digits")



class users(models.Model):
    user_id = models.CharField(max_length=5)
    name = models.CharField(max_length=100, validators=[alphaSpaces])
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, validators=[phone_regex])
    team_id = models.CharField(max_length=5)
    class Meta:
        db_table = "Users"


class teams(models.Model):
    team_id = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    class Meta:
        db_table = "Teams"