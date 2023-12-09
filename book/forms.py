from django import forms
from django.forms import ModelForm
from .models import Reservation

# Super Account
class AdminReservationForm(ModelForm):
	class Meta:
		model = Reservation
		fields = {'name', 'reserve_date', 'table', 'no_guest', 'phone', 'payment',}
		labels = {
			'name': '',
			'reserve_date': 'YYYY-MM-DD HH:MM:SS',
			'table': 'Table Number',
			'no_guest': 'Number of Guest', 
			'phone': '',
			'payment': 'Method of Payment',
		}

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Reservation Name'}),
			'reserve_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Reservation Date' }), 
			'table': forms.Select(attrs={'class':'form-select', 'placeholder':'Table'}),
			'no_guest': forms.Select(attrs={'class':'form-select', 'placeholder':'Number of Guests'}), 
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
			'payment': forms.Select(attrs={'class':'form-select', 'placeholder':'Mode of Payment'}),
		}
# User
class ReservationForm(ModelForm):
	class Meta:
		model = Reservation
		fields = {'reserve_date', 'table', 'no_guest', 'phone', 'payment',}
		labels = {
			'reserve_date': 'YYYY-MM-DD HH:MM:SS',
			'table': 'Table Number',
			'no_guest': 'Number of Guest', 
			'phone': '',
			'payment': 'Method of Payment',
		}

		widgets = {
			'reserve_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Reservation Date' }), 
			'table': forms.Select(attrs={'class':'form-select', 'placeholder':'Table'}),
			'no_guest': forms.Select(attrs={'class':'form-select', 'placeholder':'Number of Guests'}), 
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
			'payment': forms.Select(attrs={'class':'form-select', 'placeholder':'Mode of Payment'}),
		}