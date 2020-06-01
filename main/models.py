from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal

from .utilites import send_activation_notification

user_registrated = Signal(providing_args=['instance'])

def user_registrated_dispacher(sender, **kwargs):
    send_activation_notification(['instance'])

user_registrated.connect(user_registrated_dispacher)





class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                      verbose_name='Прошёл активацию?')

    send_messages = models.BooleanField(default=True, verbose_name='Послать оповещения о новых комментариях?')

    class Meta(AbstractUser.Meta):
        pass
