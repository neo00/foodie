from django.db import models

class Restaurant(models.Model):
    """Restaurant model"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
