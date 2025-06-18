from django.db import models

# Create your models here.
import os
from datetime import date
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    today = date.today()
    folder = f"user_files/{instance.user.username}/{today}/"
    return os.path.join(folder, filename)

class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
