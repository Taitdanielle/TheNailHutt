from django.db import models

# Create your models here.
class Services(models.Model):

    class Meta:
        verbose_name_plural ='Services'

    name = models.CharField(max_length=254, null=True)
    friendly_name = models.OneToOneField('Services', null=True, blank=True, 
                                    on_delete=models.CASCADE)    

    def __str__(self):
        return self.name

class ServicesDetail(models.Model):
    service = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_a_service = models.BooleanField(default=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return self.name        