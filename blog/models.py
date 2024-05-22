from django.db import models

# Create your models here.

class Adminstrator(models.Model):
    cource_title=models.CharField(max_length=150)
    descrition=models.TextField(max_length=150)
    instructo_name=models.CharField(max_length=150)
    start_date=models.DateField()
    end_date=models.DateField()
    price=models.IntegerField()
    
    def __str__(self):
        return self.cource_title
    
class Students(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(unique=True)
    selected_cource=models.ForeignKey(Adminstrator, on_delete=models.CASCADE)
    homework=models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.name}"