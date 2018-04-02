import uuid
from django.utils.translation import gettext_lazy as _
from backend.util import models


def get_photo_path(instance, filename):
    ext = filename.split('.')[-1]
    return u'products/{}.{}'.format(uuid.uuid4(), ext, )


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=60, help_text=_('The name of the product.'))
    price = models.DecimalField(_('Price'), max_digits=7, decimal_places=2, help_text=_('The price of the product.'))
    stock_quantity = models.IntegerField(_('Stock Quantity'), help_text=_('The quantity of this product that you have in stock.'))
    photo = models.ImageField(upload_to=get_photo_path, help_text=_('Choose an image for the product.'))
    date_created = models.DateTimeField(_('Creation Date'), auto_now_add=True)
