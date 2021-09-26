from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Genre(models.Model):
    category=models.CharField(max_length=200,unique=True)
    

    def __str__(self):
        return self.category

class Book(models.Model):
    book_category=models.ForeignKey(Genre,on_delete=CASCADE)
    name=models.CharField(max_length=200,unique=True)
    image=models.ImageField(upload_to='pictures')
    desc=models.TextField()
    available=models.BooleanField(default=False)
    genre=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    keyword=models.CharField(max_length=200)

    document=models.FileField(upload_to='document',null=True)
    
    


    def __str__(self):
        return self.name





