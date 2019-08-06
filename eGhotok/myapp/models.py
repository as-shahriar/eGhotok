from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
import random
import string
from django.utils.text import slugify

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    slug = models.SlugField(blank=True, null = True, max_length=50)
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



def random_string_generator(size=10, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        # We are using .lower() method for case insensitive
        # you can use instance.<fieldname> if you want to use another field
        str = instance.name.lower()
        slug = slugify(str)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def slug_generator(sender,instance,*args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator,sender=UserInfo)
