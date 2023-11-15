from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(default='11.11.2023')
    text = models.TextField(default='')
    
   
    

    def __str__(self) -> str:
        return self.name