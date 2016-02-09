# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Bares(models.Model):
    nombre = models.CharField(max_length=35, unique=True, null=False)
    direccion = models.CharField(max_length=45, unique=True, null=False)
    num_visitas=models.IntegerField(default=0)
    visits_bar= models.IntegerField(default=0)		
    likes= models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Bares, self).save(*args, **kwargs)

    #That´s for use print after. When we use print(Bares) it will show only the name
    def __str__(self):  #For Python 2, use __str__ on Python 3
        return self.nombre

class Tapas(models.Model):
    bar=models.ForeignKey(Bares, null=False) #We define the foreign key
    nombre = models.CharField(max_length=30, unique=True, null=False)
    votos=models.IntegerField(default=0)
    likes= models.IntegerField(default=0)
    picture = models.FileField(upload_to='images', blank=True)
    def __str__(self):      #For Python 2, use __str__ on Python 3
        return self.nombre

class UploadToPathAndRename(object):
    def __init__(self, path):
        self.sub_path = path
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
           filename = '{}.{}'.format(instance.pk, ext)
        else:
           filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.sub_path, filename)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model 
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.FileField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username



