from django.db import models

# Create your models here.
class Produce(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 50)
    # category = models.CharField(max_length = 50, default = "")
    # subcategory = models.CharField(max_length = 50, default = "")
    # price = models.IntegerField(default=0)
    description = models.CharField(max_length = 300)
    published_date = models.DateField()
    # image = models.ImageField(upload_to = 'tribal/images', default = "")