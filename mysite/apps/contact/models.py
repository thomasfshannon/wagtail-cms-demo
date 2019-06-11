from django.db import models

# Create your models here.

class ContactSubmission(models.Model):
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return "%s" % self.email
