import datetime
import typing

from django.db import transaction
from django.db.models import QuerySet
from django.utils import timezone
from django_api_example.app_core import models


def get_emails_to_process() -> typing.Union[QuerySet, typing.List[models.Emails]]:
    qs = models.Emails.objects.filter(
        next_process_at__lt=timezone.now(),
    ).order_by("pk")

    return qs


@transaction.atomic
def process_emails(obj: models.Emails):
    obj.next_process_at += datetime.timedelta(days=1)
    obj.save(update_fields=["next_process_at"])
