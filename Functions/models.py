from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.




class Services(models.Model):
    Title = models.CharField(max_length=20)
    discription = models.TextField(null=True, blank= True)
    icon_class = models.CharField(max_length=200, null=True, blank= True)
    image = models.ImageField(upload_to='services', null=True, blank=True)
    status = models.BooleanField(default=True)
    


class Portflolio_Projecrs(models.Model):
    TYPE = (
        ("Web","Website"),
        ("app","Mobile App"),
        ("card","Card"),
        )
    projects_type = models.CharField(choices = TYPE,max_length=50, null=True, blank=True)
    Title = models.CharField(max_length=20)
    discription = models.CharField(max_length=45)       
    image = models.ImageField(upload_to="Projects")

class TeamMember(models.Model):
    Name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    Short_discription = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to="Teams", default="image.jpj")
    facebook_link = models.TextField(null=True, blank=True)
    instragram_link = models.TextField(null=True, blank=True)
    linked_link = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)


class Pricing(models.Model):
    Title = models.CharField(max_length=250)
    max_price = models.PositiveIntegerField()
    min_price = models.PositiveIntegerField()



class PublicMessage(models.Model):
    Name = models.CharField(max_length=250)
    Email = models.EmailField()
    Subject = models.CharField(max_length=250)
    Message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    seen_status = models.BooleanField(default=False)
    def __str__(self):
        return self.Name