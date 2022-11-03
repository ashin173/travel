from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='images')
    desc=models.TextField()

    def __str__(self):
      return self.name
class team(models.Model):
    playername=models.CharField(max_length=250)
    playerimage=models.ImageField(upload_to='images')


    def __str__(self):
        return self.playername
