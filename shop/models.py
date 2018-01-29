from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import uuid
from PIL import Image
from django.conf import settings
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


def make_upload_path(instance, filename, prefix=False):
    """
    Create unique name for image or file
    :param instance:
    :param filename:
    :param prefix:
    :return: unique name
    """
    new_name = str(uuid.uuid1())
    parts = filename.split('.')
    file_type = parts[-1]
    filename = '%s.%s' % (new_name, file_type)
    return u'%s/%s' % (settings.SHOP_IMAGE_DIR, filename)


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название категории')
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', verbose_name='Родитель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    class MPTTMeta:
        order_insertion_by = ['name']


class Product(models.Model):
    prod_name = models.CharField(max_length=100, verbose_name='Название продукта')
    prod_slug = models.SlugField(default='', unique=True, max_length=250)
    prod_description = models.TextField(verbose_name='Описание')
    prod_category = TreeForeignKey(Category, null=True, blank=True,
                            related_name='category', verbose_name='Категория')
    prod_image = models.FileField(upload_to=make_upload_path, null=True)

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'

    @models.permalink
    def get_absolute_url(self):
        return ('shop', [self.prod_slug])

    def __str__(self):
        return self.prod_name


@receiver(pre_delete, sender=Product)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    print('-----------===---EEeeyha----===--')
    instance.prod_image.delete(False)