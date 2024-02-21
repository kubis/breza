from django.db import models

# Create your models here.
class AppType(models.Model):
    name = models.CharField(max_length=20)
    koda = models.CharField(max_length=8,null=True, blank=True)
    opis = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class AppTypeImage(models.Model):
    apptype = models.ForeignKey(AppType, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='appartmens/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.apptype.name} : {self.title}'