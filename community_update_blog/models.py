from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinLengthValidator

STATUS = ((0, "Draft"), (1, "Published"))

class CommunityUpdate(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_update')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(validators=[
            MinLengthValidator(200, 'the field must contain at least 200 characters')
            ])
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='community_update_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Community update: {self.title}, Status: {self.status}, Author: {self.author}"

    def number_of_likes(self):
        return self.likes.count()


class CommunityUpdateComment(models.Model):

    post = models.ForeignKey(CommunityUpdate, on_delete=models.CASCADE,
                             related_name="community_update_comment")
    commenter = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:

        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.commenter}"

