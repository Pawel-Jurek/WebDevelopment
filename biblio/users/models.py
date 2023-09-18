from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
# Create your models here.
logger = logging.getLogger('django')

class BiblioUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, default='')

    
    """
    Second idea
    
    def save(self, *args, **kwargs):
        super(BiblioUser, self).save(*args, **kwargs)
        try:
            p = Permission.objects.get(codename='can_rent')
            self.user_permissions.add(p)
        except Exception as e: #Permission.DoesNotExist or Permission.MultipleObjectsReturned:
            logger.error("Error: %s" % e)
        
    """
@receiver(post_save, sender=BiblioUser)    
def add_rent_permission(sender, *args, **kwargs):
    user = kwargs.get('instance')
    try:
        p = Permission.objects.get(codename='can_rent')
        user.user_permissions.add(p)
        logger.info('Permissions added succesfully')
    except Exception as e:
        logger.error("Error: %s" % e)
        