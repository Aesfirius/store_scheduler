from django.db import models


class StoreLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    location_name = models.CharField(max_length=64, null=False)
    location_desc = models.CharField(max_length=100, null=True)
    location_coord = models.CharField(max_length=50, null=True)
    location_photo = models.CharField(max_length=300, null=True)


class Products(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=64, null=False)
    product_desc = models.CharField(max_length=100, null=True)
    product_amount = models.CharField(max_length=24, null=True)
    product_cost = models.FloatField(null=True)
    product_date = models.CharField(max_length=24, null=False, default='not_scheduled')
    product_photo = models.CharField(max_length=300, null=True)
    product_loc = models.ForeignKey(StoreLocations, on_delete=models.CASCADE, null=True)
    groups = models.JSONField(null=False)
