from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import Reservation, Table
from .forms import ReservationForm
from django.contrib import messages
# Pagination
from django.core.paginator import Paginator

# PDF Imports
from django.http import FileResponse
import io 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def admin_approval(request):
	reservation_list = Reservation.objects.all().order_by('-reserve_date')
	if request.user.is_superuser:
		if request.method == "POST":
			id_list = request.POST.getlist('boxes')

			reservation_list.update(approved=False)
			# Update
			for x in id_list:
				Reservation.objects.filter(pk=int(x)).update(approved=True)

			messages.success(request, ("Reservation Approved"))
			return redirect('reservation-list')

		else:
			return render(request, 'book/admin_approval.html', {'reservation_list': reservation_list, 'title': 'Admin Approval',})

	else:
		messages.success(request, ("You aren't authorized to view this page!"))
		return redirect('book-home')

	


def venues_list(request):
	table = Table.objects.all()
	return render(request, 'book/venues.html', {'table': table, 'title': 'Venues',})

# Generate PDF File of Reservations(for admins only)
def reservation_pdf(request):
	# Bytestream buffer
	buf = io.BytesIO()
	# Canvas
	can = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	# Text Object
	textobject = can.beginText()
	textobject.setTextOrigin(inch, inch)
	textobject.setFont("Helvetica", 14)

	#add line of text
	reservations_list = Reservation.objects.all()

	lines = []

	for reservation in reservations_list:
		lines.append(reservation.name)
		lines.append(str(reservation.reserve_date))
		lines.append(str(reservation.table))
		lines.append(str(reservation.no_guest))
		lines.append(reservation.phone)
		lines.append(str(reservation.payment))
		lines.append("")

	for line in lines:
		textobject.textLine(line)

	can.drawText(textobject)
	can.showPage()
	can.save()
	buf.seek(0)

	return FileResponse(buf, as_attachment=True, filename='Reservation_List.pdf')

# Delete 
def delete_reservation(request, reservation_id):
	reservation = Reservation.objects.get(pk=reservation_id)
	reservation.delete()
	return redirect('reservation-list')

# Update
def update_reservation(request, reservation_id):
	reservation = Reservation.objects.get(pk=reservation_id)
	form = ReservationForm(request.POST or None, instance=reservation)
	if form.is_valid():
		form.save()
		return redirect('reservation-list')

	return render(request, 'book/update_reservation.html', {'reservation': reservation, 'form':form, 'title': 'Update Reservation',})

# Search
def search_reservation(request):
	if request.method == "POST":
		searched = request.POST['searched']
		reservations = Reservation.objects.filter(name__contains=searched)

		return render(request, 'book/search_reservation.html',
			{'searched':searched, 'reservations':reservations})
	else: 
		return render(request, 'book/search_reservation.html',
			{})

# Book/Add-Reservation
def add_reservation(request):
	submitted = False
	if request.method == "POST":
		form = ReservationForm(request.POST)
		if form.is_valid():
			#form.save()
			reservation = form.save(commit=False)
			reservation.name = request.user
			reservation.save()
			return HttpResponseRedirect('/add_reservation?submitted=True')
	else:
		form = ReservationForm
		if 'submitted' in request.GET:
			submitted =  True

	return render(request, 'book/add_reservation.html', {'form': form, 'submitted': submitted, 'title': 'Book',})

# See Reservation-List/History
def all_reservations(request):
	resevation_list = Reservation.objects.all()

	# Set Pagination
	p = Paginator(Reservation.objects.all(), 3)
	page = request.GET.get('page')
	reservations = p.get_page(page)

	return render(request, 'book/reservation_list.html',
		{'reservation_list': resevation_list, 'reservations': reservations, 'title': 'Reservations',})

# Homepage
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	month = month.capitalize()
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	# Calendar
	cal = HTMLCalendar().formatmonth( year, month_number)

	# Get current year
	now = datetime.now()
	current_year = now.year

	# Get current time
	time = now.strftime('%I:%M:%S %p')

	reservation_list = Reservation.objects.filter(
			reserve_date__year = year,
			reserve_date__month = month_number,

		)

	return render(request, 'book/home.html', {
		"year": year,
		"month": month,
		"month_number": month_number,
		"cal": cal,
		"current_year": current_year,
		"time": time,
		"reservation_list": reservation_list,

	})

def about(request):
	return render(request, 'book/about.html', {'title': 'About'})

def contact(request):
	return render(request, 'book/contact.html', {'title': 'Contact-Us'})