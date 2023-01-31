from django.db import models


# Create your models here.

class Info(models.Model):
    bat = models.CharField(max_length=30,null=True, blank=True)
    color_r = models.IntegerField(default=0)
    color_g = models.IntegerField( default=0)
    color_b = models.IntegerField( default=0)
    encoder_l = models.IntegerField(null=True, blank=True)
    encoder_r = models.IntegerField(null=True, blank=True)
    a=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at.strftime("%D %H:%M")}'


