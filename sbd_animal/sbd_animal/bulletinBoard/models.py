from django.db import models
from django.conf import settings

# Create your models here.


class Inquery(models.Model):
    class Meta:
        ordering = ["created_at"]

    class ReplyState(models.TextChoices):
        NO = "N", "미응답"
        YES = "Y", "응답"
        PLS = "P", "추가의문"
        FIN = "F", "처리완료"

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    state = models.CharField(
        max_length=1, choices=ReplyState.choices, default=ReplyState.NO
    )
    created_at = models.DateField(auto_now_add=True)

    @property
    def state_label(self):
        return self.get_state_display()


class Reply(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    inquery = models.ForeignKey(Inquery, on_delete=models.CASCADE)
    parent_reply = None
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
