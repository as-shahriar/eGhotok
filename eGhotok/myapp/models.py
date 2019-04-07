from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    name = models.CharField(max_length = 200)
    cell = models.CharField(max_length = 20)
    address = models.CharField(max_length = 400)
    city = models.CharField(max_length = 50)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length = 10)
    religion = models.CharField(max_length = 50)
    pic = models.ImageField(upload_to='profile_pics',blank=True,default="default.jpg")
    fb = models.URLField(blank=True)
    insta = models.URLField(blank=True)
    education_level = models.CharField(max_length = 100,blank=True)
    education_field = models.CharField(max_length = 200,blank=True)
    work_as = models.CharField(max_length = 50,blank=True)
    work_in = models.CharField(max_length = 200,blank=True)


    def __str__(self):
        return self.user.username
