from django.db import models

# Create your models here.

class Pick(models.Model):
    user_id = models.IntegerField()
    pick_id = models.IntegerField()

