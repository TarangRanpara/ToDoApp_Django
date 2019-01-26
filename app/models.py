from django.db import models

# Create your models here.
class ToDo(models.Model):
    description     = models.CharField(max_length = 500)
    author          = models.CharField(max_length = 100)
    pub             = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.author + ":" + str(self.pub)