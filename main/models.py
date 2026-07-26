from django.db import models


class RSVP(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    guest_count = models.PositiveIntegerField()
    attending = models.BooleanField(default=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class GiftClaim(models.Model):
    gift_name = models.CharField(max_length=100)
    claimant_name = models.CharField(max_length=150)
    claimant_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Gift claims'

    def __str__(self):
        return f'{self.gift_name} - {self.claimant_name}'
