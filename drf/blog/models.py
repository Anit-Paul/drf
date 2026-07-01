from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    
    def __str__(self):
        return self.title

class comment(models.Model):
    blog=models.ForeignKey(blog,on_delete=models.CASCADE,related_name='comments')
    comment=models.TextField()
    
    def __str__(self):
        return self.comment