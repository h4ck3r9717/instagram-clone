
  
from django.db import models

from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    """
    class to define profile profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
      #image field
    image = CloudinaryField('image')
    #image = models.ImageField(default='profile.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' 
    
    def save_profile(self):
        super().save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls,search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'