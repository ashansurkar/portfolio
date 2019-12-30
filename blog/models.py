from django.db import models

class blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now = False)
    body = models.TextField()
