from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from dkp.models import Transaction, Bonus, ResourceContrib, EventItem, EventEntity, EventAttendance

TRANSACTION_MODELS = (
    Bonus,
    ResourceContrib,
)


@receiver(post_save)
def create_bonus_transaction(sender, instance, created, **kwargs):

    if sender not in TRANSACTION_MODELS:
        return

    if created:
        if instance.dkp != 0:
            transaction = Transaction()
            transaction.user_id = instance.user_id
            transaction.set_related_property(instance)
            transaction.section = instance.get_section()
            if instance.dkp > 0:
                transaction.description = instance.credit_description()
                transaction.credit = instance.dkp
            if instance.dkp < 0:
                transaction.description = instance.debit_description()
                transaction.debit = instance.dkp
            transaction.save()
    else:
        # Get latest transaction and refund it
        filter_kwargs = {
            Transaction().get_related_property_name(sender): instance
        }
        previous = Transaction.objects.filter(**filter_kwargs).order_by('-created').first()
        if not previous:
            raise Transaction.DoesNotExist('No previous transaction to edit')
        transaction = Transaction()
        transaction.user_id = previous.user_id
        transaction.set_related_property(instance)
        transaction.section = instance.get_section()
        if previous.debit:
            transaction.description = instance.credit_description()
            transaction.credit = previous.debit
        if previous.credit:
            transaction.description = instance.debit_description()
            transaction.debit = previous.credit
        transaction.save()

        # If updated value isn't zero make a new transaction with the new values
        if instance.dkp != 0:
            transaction = Transaction()
            transaction.user_id = instance.user_id
            transaction.set_related_property(instance)
            transaction.section = instance.get_section()
            if instance.dkp > 0:
                transaction.description = instance.credit_description()
                transaction.credit = instance.dkp
            if instance.dkp < 0:
                transaction.description = instance.debit_description()
                transaction.debit = instance.dkp
            transaction.save()\

@receiver(post_save, sender=EventItem)
def create_item_transaction(sender, instance, created, **kwargs):

    if created:
        if instance.dkp != 0:
            transaction = Transaction()
            transaction.user_id = instance.user_id
            transaction.item = instance
            transaction.section = instance.get_section()
            if instance.dkp < 0:
                transaction.description = instance.credit_description()
                transaction.credit = instance.dkp
            if instance.dkp > 0:
                transaction.description = instance.debit_description()
                transaction.debit = instance.dkp
            transaction.save()
    else:
        # Get latest transaction and refund it
        previous = Transaction.objects.filter(item=instance).order_by('-created').first()
        if not previous:
            raise Transaction.DoesNotExist('No previous transaction to edit')
        transaction = Transaction()
        transaction.user_id = previous.user_id
        transaction.item = instance
        transaction.section = instance.get_section()
        if previous.debit:
            transaction.description = instance.credit_description()
            transaction.credit = previous.debit
        if previous.credit:
            transaction.description = instance.debit_description()
            transaction.debit = previous.credit
        transaction.save()

        # If updated value isn't zero make a new transaction with the new values
        if instance.dkp != 0:
            transaction = Transaction()
            transaction.user_id = instance.user_id
            transaction.item = instance
            transaction.section = instance.get_section()
            if instance.dkp < 0:
                transaction.description = instance.credit_description()
                transaction.credit = instance.dkp
            if instance.dkp > 0:
                transaction.description = instance.debit_description()
                transaction.debit = instance.dkp
            transaction.save()


@receiver(post_save, sender=EventEntity)
def create_entity_transaction(sender, instance, created, **kwargs):
    if created:
        print instance.created
        for attendee in EventAttendance.objects.filter(event=instance.event, standby=False, started__lt=instance.created, stopped__isnull=True):
            if instance.dkp:
                transaction = Transaction()
                transaction.user_id = attendee.user_id
                transaction.set_related_property(instance)
                transaction.section = instance.get_section()
                if instance.dkp > 0:
                    transaction.description = instance.credit_description()
                    transaction.credit = instance.dkp
                if instance.dkp < 0:
                    transaction.description = instance.debit_description()
                    transaction.debit = instance.dkp
                transaction.save()
    else:
        for attendee in EventAttendance.objects.filter(event=instance.event, standby=False, started__lt=instance.created, stopped__isnull=True):

            previous = Transaction.objects.filter(entity=instance, user=attendee.user).order_by('-created').first()
            if not previous:
                raise Transaction.DoesNotExist('No previous transaction to edit')
            if instance.dkp:
                transaction = Transaction()
                transaction.user_id = previous.user_id
                transaction.set_related_property(instance)
                transaction.section = instance.get_section()
            if previous.debit:
                transaction.description = instance.credit_description()
                transaction.credit = previous.debit
            if previous.credit:
                transaction.description = instance.debit_description()
                transaction.debit = previous.credit
            transaction.save()

        for attendee in EventAttendance.objects.filter(event=instance.event, standby=False, started__lt=instance.created, stopped__isnull=True):
            if instance.dkp:
                transaction = Transaction()
                transaction.user_id = attendee.user_id
                transaction.set_related_property(instance)
                transaction.section = instance.get_section()
                if instance.dkp > 0:
                    transaction.description = instance.credit_description()
                    transaction.credit = instance.dkp
                if instance.dkp < 0:
                    transaction.description = instance.debit_description()
                    transaction.debit = instance.dkp
                transaction.save()


# @receiver(post_delete, sender=Niggers)