from django.db.models.signals import post_save
from django.dispatch import receiver
from dkp.models import Transaction, Bonus, ResourceContrib, EventItem, EventEntity, EventAttendance

@receiver(post_save, sender=Bonus)
def create_bonus_transaction(sender, instance, created, **kwargs):
    # TODO update and delete
    if created:
        if instance.dkp is not 0:
            transaction = Transaction()
            transaction.user_id = instance.user_id
            transaction.bonus = instance
            if instance.dkp > 0:
                transaction.credit = instance.dkp
            if instance.dkp < 0:
                transaction.debit = instance.dkp
            transaction.save()

@receiver(post_save, sender=ResourceContrib)
def create_resourcecontrib_transaction(sender, instance, created, **kwargs):
    # TODO update, and delete
    if created:
        if instance.dkp is not 0:
            transaction = Transaction()
            transaction.user_id = instance.user_id
            transaction.resource_contrib = instance
            if instance.dkp > 0:
                transaction.credit = instance.dkp
            if instance.dkp < 0:
                transaction.debit = instance.dkp
            transaction.save()

@receiver(post_save, sender=EventItem)
def create_item_transaction(sender, instance, created, **kwargs):
    # TODO update, and delete
    if created:
        if instance.dkp is not 0:
            transaction = Transaction()
            transaction.user_id = instance.user_id
            transaction.item = instance
            transaction.debit = instance.dkp
            transaction.save()

@receiver(post_save, sender=EventEntity)
def create_entity_transaction(sender, instance, created, **kwargs):
    # TODO update and delete
    if created:
        for attendee in EventAttendance.objects.filter(event=instance.event):
            if attendee.started < instance.created and not attendee.stopped:
                if attendee.standby is False:
                    transaction = Transaction()
                    transaction.user_id = attendee.user_id
                    transaction.entity = instance
                    transaction.credit = instance.dkp
                    transaction.save()
