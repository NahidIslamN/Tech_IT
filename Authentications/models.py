from django.db import models

# Create your models here.


class Subsripbers(models.Model):
    Email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)




    
