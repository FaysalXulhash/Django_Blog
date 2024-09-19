from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default = 'default.JPG', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile!'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        i = Image.open(self.img.path)

        if i.height > 300 or i.width > 300:
            output_size = (300, 300)
            i.thumbnail(output_size)
            i.save(self.img.path)
    