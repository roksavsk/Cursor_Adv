from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):

    STATUS_OPEN = 'open'
    STATUS_IN_PROGRESS = 'in progress'
    STATUS_CLOSED = 'closed'
    STATUS_CANCELLED = 'cancelled'

    STATUS_CHOICES = (
        (STATUS_OPEN, 'Open'),
        (STATUS_IN_PROGRESS, 'In progress'),
        (STATUS_CLOSED, 'Closed'),
        (STATUS_CANCELLED, 'Cancelled'),
    )

    car = models.ForeignKey('car.Car', on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=STATUS_OPEN,
        blank=True
    )
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.EmailField(max_length=75)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
