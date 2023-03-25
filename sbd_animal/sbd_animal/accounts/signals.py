from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
from .models import User


@receiver(pre_save, sender=User)
def pre_save_profile(sender, instance, *args, **kwargs):
    """
    old profile image delete before profile edited with new profile image
    """
    try:
        old_avatar = instance.__class__.objects.get(id=instance.id).avatar.path
        try:
            new_avatar = instance.avatar.path
        except:
            new_avatar = None
        if new_avatar != old_avatar:
            import os

            if os.path.exists(old_avatar):
                os.remove(old_avatar)
    except:
        pass
