from django.db import models


class Access(models.Model):
    token = models.CharField(verbose_name="Access token", max_length=200, null=True)
    user_id = models.CharField(verbose_name="id пользователя vk", max_length=40, null=True)
    app_id = models.CharField(verbose_name="id приложения", max_length=40, null=True)

