from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.models import Gallery

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill 
from imagekit.models import ProcessedImageField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # image = models.FileField(null = True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    #code for Thumbnail
    # image = models.ImageField(upload_to = "media", default='DEFAULT VALUE')
    image_thumbnail = ProcessedImageField(upload_to = "thumbnail",
                                        processors = [ResizeToFill(100,50)],format = 'JPEG',options = {'quality':60},default='DEFAULT VALUE')


    


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

#code for uploading multiple images
class PostPicture(models.Model):
     picture =models.ImageField(upload_to="blog_images", blank=True)
     postid =models.ForeignKey(Post,on_delete=models.CASCADE,related_name='pictures')       




class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)




