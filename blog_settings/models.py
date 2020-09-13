from django.db import models


# Create your models here.
class Setting(models.Model):
    # header
    site_logo = models.ImageField()
    site_title = models.CharField(max_length=159)
    site_subheading = models.CharField(max_length=159)
    # navbar
    nav_copy_right = models.CharField(max_length=150, default="amirhossein")
    social_link = models.URLField(default="your url here")
    social2_link = models.URLField(default="your url here")

    def __str__(self):
        return self.site_title