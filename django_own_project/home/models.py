from django.db import models

# Create your models here.

class Contact(models.Model):
    sn = models.IntegerField(primary_key=1)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=140)

    def __str__(self):
        return self.name, self.sn
