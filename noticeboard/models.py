from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField

class Notice(models.Model):

    title = models.CharField(max_length=45, unique=True)
    approved = models.BooleanField(default=False)
    description = models.TextField()
    contact_number = models.CharField(max_length=25, blank=True)
    contact_email = models.EmailField(max_length = 254)
    location = models.CharField(max_length=60, null=True)
    background_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "created_on"

    def __str__(self):
        return f"Notice title: {self.title}, Approved: {self.approved}, Contact email: {self.contact_email}"
