from django.db import models

# Create your models here.
class RegisterStudent(models.Model):
    st_name = models.TextField(max_length=100)
    st_contact = models.TextField(max_length=10)    
    st_email = models.TextField(max_length=50)
    st_username = models.TextField(max_length=100)
    st_password = models.TextField(max_length=100)
    st_confirmpassword = models.TextField(max_length=100)
    st_usertype = models.TextField(max_length=100)
    st_status = models.TextField(max_length=100)
