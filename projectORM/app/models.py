from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=20,primary_key=True)
    
    def __str__(self):
        return self.topic_name
    
class Webpage(models.Model):
    id = models.IntegerField(primary_key=True)
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    url = models.URLField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name
