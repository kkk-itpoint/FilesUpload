from django.db import models

# Create your models here.
class Info(models.Model):
    fn = models.CharField(max_length = 50)
    ln = models.CharField(max_length = 50)
    tech = models.CharField(max_length = 200)
    email = models.EmailField()
    photo = models.FileField()

    # class Meta:
    #     db_table = 'Profiles'