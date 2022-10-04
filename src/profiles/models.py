import uuid
from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class Profile(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(_('First name'), max_length=50)
    last_name = models.CharField(_('Last name'), max_length=50)
    birthdate = models.DateField(_('Date of birth'))
    biography = models.TextField(_('Biography'), blank=True)
    contacts = models.EmailField(_('Email'), max_length=254, blank=False, unique=True)

    def __str__(self) -> str:
        return f'Profile {self.id} | {self.first_name} {self.last_name}'

    def get_full_name(self) -> str:
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()
