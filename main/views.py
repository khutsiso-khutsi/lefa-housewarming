from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import GiftClaimForm, RSVPForm
from .models import GiftClaim


GIFT_OPTIONS = [
    {'slug': 'kitchenware', 'name': 'Kitchenware', 'description': 'A thoughtful addition for the heart of the home.', 'capacity': 3, 'claimed': 0},
    {'slug': 'decor', 'name': 'Home Décor', 'description': 'Elegant pieces to soften and style the rooms.', 'capacity': 3, 'claimed': 0},
    {'slug': 'plants', 'name': 'Garden Plants', 'description': 'Fresh greenery for a calm and welcoming home.', 'capacity': 3, 'claimed': 0},
    {'slug': 'books', 'name': 'Books', 'description': 'A refined collection for quiet evenings and study.', 'capacity': 3, 'claimed': 0},
    {'slug': 'cash', 'name': 'Cash Gift', 'description': 'A gracious contribution toward the new home.', 'capacity': 3, 'claimed': 0},
    {'slug': 'vouchers', 'name': 'Gift Vouchers', 'description': 'Flexible and practical for furnishing the home.', 'capacity': 3, 'claimed': 0},
]


def home(request):
    return render(request, 'home.html')


def event_details(request):
    return render(request, 'event_details.html')


def rsvp(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your RSVP has been received.')
            return redirect('thank_you')
    else:
        form = RSVPForm()
    return render(request, 'rsvp.html', {'form': form})


def gifts(request):
    gift_options = []
    for gift in GIFT_OPTIONS:
        claimed_count = GiftClaim.objects.filter(gift_name=gift['name']).count()
        gift_options.append({
            **gift,
            'claimed_count': claimed_count,
            'remaining': max(gift['capacity'] - claimed_count, 0),
            'available': claimed_count < gift['capacity'],
        })
    if request.method == 'POST':
        form = GiftClaimForm(request.POST)
        gift_name = request.POST.get('gift_name')
        if form.is_valid() and gift_name:
            current_count = GiftClaim.objects.filter(gift_name=gift_name).count()
            if current_count >= 3:
                messages.error(request, 'That gift option is no longer available.')
            else:
                claim = form.save(commit=False)
                claim.gift_name = gift_name
                claim.save()
                messages.success(request, 'Your gift claim has been recorded.')
                return redirect('thank_you')
    else:
        form = GiftClaimForm()
    return render(request, 'gifts.html', {'gifts': gift_options, 'form': form})


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    return render(request, 'contact.html')


def thank_you(request):
    return render(request, 'thank_you.html')
