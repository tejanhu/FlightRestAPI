from flightapi.models import Flight, Pilot, TravelAgency, Position
from rest_framework import serializers

class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = ('id', 'flight_number', 'zone', 'passengers', 'flying_from', 'flying_to', 'terminal_number', 'departure_date', 'arrival_date', 'status', 'pilot', 'travelagency')

class PilotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pilot
        fields = ('id', 'name', 'position')

class TravelAgencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TravelAgency
        fields = ('id', 'company_name', 'flight_fares', 'baggage_allowance')

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'rank', 'badge')
