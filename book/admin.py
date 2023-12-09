from django.contrib import admin
from .models import Table
from .models import Payment
from .models import Reservation
from .models import MemberUser
from .models import Guest

admin.site.register(Payment)
admin.site.register(MemberUser)
admin.site.register(Guest)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = ('name', 'reserve_date', 'table',)
	list_filter = ('reserve_date',)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
	list_display = ('number_table',)


