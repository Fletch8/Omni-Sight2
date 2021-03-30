from django.db import models
# thank you Django for this user :-)
from django.contrib.auth.models import User

# Create your models here.
class Currency(models.Model):
    symbol = models.CharField(max_length=6)
    price = models.IntegerField()