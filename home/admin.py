from django.contrib import admin

from .models import Department, Doctors, Booking

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone', 'p_email', 'booking_date', 'booked_on', 'doc_name')
admin.site.register(Booking, BookingAdmin)