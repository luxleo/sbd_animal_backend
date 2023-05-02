from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
from .models import User
from django.conf import settings


@receiver(pre_save, sender=User)
def pre_save_profile(sender, instance, *args, **kwargs):
    """
    old profile image delete before profile edited with new profile image
    """
    if settings.DEBUG:
        try:
            old_avatar = instance.__class__.objects.get(id=instance.id).avatar.path

            # 프로필 설정했을 때
            try:
                new_avatar = instance.avatar.path

            # 프로필 설정 안했을때
            except:
                new_avatar = None
            if new_avatar != old_avatar:
                import os

                if os.path.exists(old_avatar):
                    os.remove(old_avatar)
        except:
            pass
    else:
        try:
            # prod 모드에서는 path로 접근시 오류발생
            old_avatar = instance.__class__.objects.get(id=instance.id).avatar.name
            try:
                new_avatar = instance.avatar.name
            except:
                new_avatar = None
            if new_avatar != old_avatar:
                # s3 Storage
                from django.core.files.storage import default_storage

                try:
                    if default_storage.exists(old_avatar):
                        default_storage.delete(old_avatar)
                except:
                    pass
        except:
            pass
