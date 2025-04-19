from django.shortcuts import render, redirect
from .models import Seat

def seat_booking(request):
    seats = Seat.objects.all().order_by('row', 'column')
    return render(request, 'booking/seat_booking.html', {'seats': seats})

def book_seats(request):
    if request.method == 'POST':
        seat_ids = request.POST.get('seats', '')
        seat_ids = seat_ids.split(',')

        for seat_id in seat_ids:
            try:
                seat = Seat.objects.get(id=int(seat_id))
                if not seat.is_booked:
                    seat.is_booked = True
                    seat.save()
            except (ValueError, Seat.DoesNotExist):
                pass

    return redirect('seat_booking')
