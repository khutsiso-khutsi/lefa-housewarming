from django.contrib import admin
from .models import RSVP, GiftClaim


@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'guest_count', 'attending', 'created_at')
    list_filter = ('attending', 'created_at')
    search_fields = ('full_name', 'email', 'phone_number')
    ordering = ('-created_at',)


@admin.register(GiftClaim)
class GiftClaimAdmin(admin.ModelAdmin):
    list_display = ('gift_name', 'claimant_name', 'claimant_email', 'created_at')
    list_filter = ('gift_name', 'created_at')
    search_fields = ('gift_name', 'claimant_name', 'claimant_email')
    ordering = ('-created_at',)
