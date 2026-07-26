from django import forms
from .models import RSVP, GiftClaim


class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['full_name', 'email', 'phone_number', 'guest_count', 'attending', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'guest_count': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Optional note'}),
        }


class GiftClaimForm(forms.ModelForm):
    class Meta:
        model = GiftClaim
        fields = ['claimant_name', 'claimant_email']
        widgets = {
            'claimant_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'claimant_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
        }
