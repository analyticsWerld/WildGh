from django.db import models
import datetime

# Create your models here.

now = datetime.date.today()
def path_watermarked(instance, filename):
    return '/'.join(filter(None, (instance.category,"watermarked",now.strftime('%Y'), filename)))

def path_no_watermark(instance, filename):
    return '/'.join(filter(None, (instance.category,"no_watermark",now.strftime('%Y'), filename)))



class Gallery(models.Model):

    category = models.CharField(max_length=200)
    image_watermarked = models.ImageField(name = "Watermarked Image",upload_to=path_watermarked,blank=True)
    image_none = models.ImageField(name="Actual Image",upload_to=path_no_watermark,blank=True)
    description = models.TextField(max_length=200,blank=True,null=True)
    price = models.IntegerField(blank=True,null=True,default=50)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
  
