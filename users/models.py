from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=50)
    email        = models.EmailField(max_length=100, unique=True)
    password     = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=30, null=True)
    birthdate    = models.DateField(null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "users"
        
        
