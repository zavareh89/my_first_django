from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        """ if we didn't ovveride the save method, only this method would be executed 
            whenever the save method was called on an instance of profile. Instead, now
            the following lines of code are also executed.
        """
        with Image.open(self.image.path) as img:
            # path attribute is the full path to the image.

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
