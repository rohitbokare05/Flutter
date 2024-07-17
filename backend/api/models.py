from datetime import datetime
from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=50,default='task')
    desc = models.CharField(max_length=200,default='default description')
    isDone = models.BooleanField(default = False)
    date=models.DateTimeField(default=datetime.now)
    
    
    def __str__(self):
        return self.title[:20]