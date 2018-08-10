from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Planner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    category = models.CharField(max_length=1)
    type = models.CharField(max_length=100, default='U\A')
    website = models.CharField(max_length=100, null=True, blank=True)
    logo = ProcessedImageField(upload_to='logo',
                               processors=[ResizeToFill(400, 400)],
                               format='JPEG',
                               options={'quality': 60},
                               default = "events/img/profile/logo.JPG" )

    def __str__(self):
        return self.name


class Event(models.Model):
    selectPlanners = models.ManyToManyField(Planner, related_name='selectedPlanners')
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    date_and_time = models.DateTimeField('Event date and Time')
    address = models.CharField(max_length=100, null=True, blank=True)
    pud_date = models.DateTimeField('Publish Date')
    duration = models.PositiveSmallIntegerField()
    details = models.CharField(max_length=200)
    expcted_cpacity = models.PositiveSmallIntegerField()
    max_price = models.DecimalField(max_digits=9, decimal_places=2,
                                    validators=[MinValueValidator(0), MaxValueValidator(999999999)])
    # Status properties
    SENT = 0
    OFFERED = 1
    ACCEPTED = 2
    REJECTED = 3
    STATUS_CHOICES = (
        (SENT, 'Sent'),
        (OFFERED, 'Offered'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    )
    # end of status properties
    status = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True)
    planner = models.ForeignKey(Planner, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Offer(models.Model):
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.CharField(max_length=200)
    planner = models.ForeignKey(Planner, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # Status properties
    PENDING = 0
    ACCEPTED = 1
    REJECTED = 2
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    )
    # end of status properties
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return f"Offer with {self.price}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Planner.objects.create(user=instance, name=instance.username)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.planner.save()