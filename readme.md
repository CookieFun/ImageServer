### Objective

The objective of this mini project is to demonstarte image upload via django rest framework.

### Reference

Most of the code comes directly from http://stackoverflow.com/questions/20303252/django-rest-framework-imagefield.

### Rename photos upon upload
We want to rename the uploaded photos to make more sense. What's more, we wanna to perform it at the django level instead of rest framework level. In this way, all imaged saved will have the same format, also easier to manager.

**Solution**, follow the discussion on http://stackoverflow.com/questions/15140942/django-imagefield-change-file-name-on-upload.

### Implementation

**settings.py**
```python
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
    'rest_framework.parsers.JSONParser',
    'rest_framework.parsers.FormParser',
    'rest_framework.parsers.MultiPartParser',
    )
}
```
**models.py**
```python
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
    image = models.ImageField(upload_to=path_name('photos'), max_length=254,null=True)
```
----
### Test Script

**Create**
```bash
curl -X POST -S \
  -F "name=a_photo" \
  -F "image=@/Users/diansheng/Pictures/ali rush.jpg" \
  127.0.0.1:8000/api/photo/ > reply.html;
open reply.html
```

**Update**
```bash
curl -X PUT -S \
  -F "name=another_photo" \
  -F "image=@/Users/diansheng/Pictures/ali rush.jpg" \
  127.0.0.1:8000/api/photo/8/ > reply.html;
open reply.html
```
