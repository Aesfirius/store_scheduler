from django.contrib.auth.models import User, Group
from shop_scheduler import models


def create_user(username, password):
    user = User.objects.create_user(username=username, password=password)
    user.save()
    my_group, created = Group.objects.get_or_create(name=str(user.username))
    user.groups.add(my_group)
    user.save()


def get_products_by_user_id(user_id):
    user_products_data = list(models.Products.objects.filter(groups__contains=[user_id]))
    return user_products_data


def get_product(product_id):
    product_data = models.Products.objects.get(product_id=product_id)
    return product_data


def add_group_for(product, share_add):
    product.groups.append(share_add)
    product.save()
