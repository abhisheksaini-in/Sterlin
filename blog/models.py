import email
from email import message
from msilib.schema import Class
from turtle import title
from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return self.title
   
    

class PostModel(models.Model):  
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    url = models.SlugField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = HTMLField()
    image = models.ImageField(upload_to = 'PostImage/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
           return self.title


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
    

    
        
    

    

    