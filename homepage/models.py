from django.db import models

class Cow(models.Model):
    cow = models.TextField(default="")
    text = models.CharField(max_length=80)
    
    def __str__(self):
        return self.text

