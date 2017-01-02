from django.db import models
from uuid import uuid4
import os

# Create your models here.

def path_name(path):
    def wrapper(instance, filename):
        # get filename extension
        ext = filename.split('.')[-1]
        #if instance.pk:
        #    filename = '{}.{}'.format(instance.pk, ext)
        #else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper

class MyPhoto(models.Model):
    name = models.CharField(max_length=254, null=True)
    image = models.ImageField(upload_to=path_name(''), max_length=254,null=True)


