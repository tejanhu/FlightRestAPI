from django.contrib import admin
from flightapi.models import Flight, Pilot, TravelAgency, Position

# Register your models here.

class FlightAdmin(admin.ModelAdmin):

    list_display = ['flight_number','zone', 'passengers', 'flying_from', 'flying_to', 'terminal_number', 'departure_date', 'arrival_date', 'status','pilot','travelagency']

class PilotAdmin(admin.ModelAdmin):

    list_display = ['id','name']


class TravelAgencyAdmin(admin.ModelAdmin):

    list_display = ['company_name', 'flight_fares', 'baggage_allowance']

class PositionAdmin(admin.ModelAdmin):

    list_display = ['rank', 'badge', 'pilot']


admin.site.register(Flight, FlightAdmin)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(TravelAgency, TravelAgencyAdmin)
admin.site.register(Position, PositionAdmin)
