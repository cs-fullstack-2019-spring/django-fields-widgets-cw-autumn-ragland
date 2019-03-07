from django.db import models


# Super hero model
class SuperHeroModel(models.Model):
    name = models.CharField(max_length=500, default='')
    city_or_origin = models.CharField(max_length=500, default='')
    rich_or_superpowers = models.CharField(max_length=500, default='')
    powers = models.CharField(max_length=500, default='')
    good_or_evil = models.CharField(max_length=500, default='')
    proof_of_powers = models.TextField(default='')

    def __str__(self):
        return self.name
