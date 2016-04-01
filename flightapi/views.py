from flightapi.models import Flight, Pilot, TravelAgency, Position
from rest_framework import viewsets
from flightapi.serializers import FlightSerializer, PilotSerializer, TravelAgencySerializer, PositionSerializer

# Create your views here.

class FlightSet(viewsets.ModelViewSet):

    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PilotSet(viewsets.ModelViewSet):

    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer

class TravelAgencySet(viewsets.ModelViewSet):

    queryset = TravelAgency.objects.all()
    serializer_class = TravelAgencySerializer

class PositionSet(viewsets.ModelViewSet):

    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    

    
