from django.db import models
from blog_app.models import CultureAfrica


class Country(models.Model):
    name_country = models.CharField(max_length=200)
    name_province = models.CharField(max_length=200)
    name_ville = models.CharField(max_length=200)
    name_quartier = models.CharField(max_length=200)
    name_avenue = models.CharField(max_length=200)

    def __str__(self):
        return self.name_country


class Admin(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
class GestionCulture(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    culture = models.ForeignKey(CultureAfrica, on_delete=models.CASCADE)
    decription = models.CharField(max_length=200)

    def __str__(self):
        return self.culture, self.culture
