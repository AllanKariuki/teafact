from django.db import models
from django.db.models.deletion import CASCADE
from PIL import Image
from Company.models import Farmers

class Profile(models.Model):
    farmer_name = models.ForeignKey(Farmers, on_delete=CASCADE)
    image = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return f'{self.farmer_name}Profile'

    def save(self):
        super().save()
        img= Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Reviews(models.Model):
    farmer_name = models.ForeignKey(Farmers, on_delete=CASCADE)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title