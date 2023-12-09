from django.db import models

class Table(models.Model):
	number_table = models.CharField(max_length=150)
	table_image = models.ImageField(null=True, blank=True, upload_to='images/')

	def __str__(self):
		return self.number_table
 
class Payment(models.Model):
	mehthod_payment = models.CharField(max_length=20)

	def __str__(self):
		return self.mehthod_payment


class Guest(models.Model):
	no_of_guest = models.CharField(max_length=20)

	def __str__(self):
		return self.no_of_guest

class Reservation(models.Model):
	name = models.CharField('Guest Name', max_length=120)
	reserve_date = models.DateTimeField('Guest Date')
	table = models.ForeignKey(Table, blank=True, null=True, on_delete=models.SET_NULL)
	no_guest = models.ForeignKey(Guest, blank=True, null=True, on_delete=models.SET_NULL)
	phone = models.CharField(max_length=20)
	payment = models.ForeignKey(Payment, blank=True, null=True, on_delete=models.SET_NULL)
	approved = models.BooleanField('Approved', default=False)


	def __str__(self):
		return self.name

class MemberUser(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField('User Email')
	phone = models.CharField(max_length=20)

	def __str__(self):
		return self.first_name + '' + last_name