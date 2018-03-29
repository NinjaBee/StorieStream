from django.db import models

# Create your models here.


class Document(models.Model):
    upload_by = models.ForeignKey('auth.User', related_name='uploaded_documents')
    datestamp = models.DateTimeField(auto_now_add=True)
    document = models.Field(upload_to='uploads/')
    # ...


class MainModel(models.Model):
    title = models.CharField(max_length=42)
    document = models.ForeignKey(Document)
    #...
