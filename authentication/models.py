from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.
class FEUser(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name']

    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile/", verbose_name="Profile picture")
    bio = models.TextField(max_length=512, null=True, blank=True, verbose_name="Bio", help_text="About you")
    last_login = models.DateTimeField(auto_now_add=True, verbose_name="Last login")
    organizations = models.CharField(max_length=200, verbose_name='Organizations', help_text='Separate organizations with a semicolon \';\'')
    orcid_id = models.CharField(max_length=20, verbose_name='Orcid ID')
    location = models.CharField(max_length=30, null=True, blank=True, verbose_name='Location')
    slug = models.SlugField(null=True, verbose_name="Slug")

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def save(self, *args, **kwargs):
        if not self.vanity:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)