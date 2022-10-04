from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete

import logging

logger = logging.getLogger('main')


@receiver(pre_save)
def model_pre_save(sender, instance, **kwargs):
    if instance.pk:
        try:
            previous = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            return
        fields = [f.name for f in instance._meta.model._meta.get_fields()]
        for field in fields:
            if hasattr(previous, str(field)):
                if getattr(previous, str(field)) != getattr(instance, str(field)):
                    logger.info(
                        "Changed {} model instance id:{}, field:{} from {} to {}"
                        .format(
                            instance._meta.model.__name__,
                            instance.pk,
                            field,
                            getattr(previous, str(field)),
                            getattr(instance, str(field))
                        )
                    )


@receiver(post_save)
def model_post_save(sender, instance, created, **kwargs):
    if created:
        logger.info("Created {} model instance id:{}".format(instance._meta.model.__name__, instance.pk))


@receiver(post_delete)
def model_instance_deleted(sender, instance, **kwargs):
    logger.info("Deleted {} model instance id:{}".format(instance._meta.model.__name__, instance.pk))

