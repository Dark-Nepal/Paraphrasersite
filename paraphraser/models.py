from django.db import models

class Site(models.Model):
    title = models.CharField( max_length=100, verbose_name='Name of site')
    description = models.CharField(max_length=200, verbose_name='Descritpions of site')
    link = models.URLField()
    img = models.ImageField(upload_to='site_img/')


    def __str__(self):
        return self.title

class Contact(models.Model):
    fullname =models.CharField(max_length=100, verbose_name='Full Name')
    email = models.EmailField(verbose_name='Email')
    phone = models.IntegerField()
    message = models.TextField( verbose_name='Message')
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

