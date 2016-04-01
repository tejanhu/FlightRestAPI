from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#Position class providing Pilot ranking system i.e.: Pilot, Co-pilot and badges represented in stars

class Position(models.Model):
    id = models.AutoField(primary_key = True)    
    rank=models.CharField(max_length=96, unique=True, blank=True)
    badge=models.CharField(max_length=96, unique=True, blank=True)
    
#Pilot class providing Pilot's name and position in terms of rank coming as a foreign key from class Position
    
class Pilot(models.Model):
    id = models.AutoField(primary_key = True)
    name=models.CharField(max_length=96, unique=True, blank=True)
    position=models.ForeignKey(Position)
    
#Travel Agency class providing information regarding the travel company name, flight fares and baggage allowance permitted by the travel agency

class TravelAgency(models.Model):
    id = models.AutoField(primary_key = True)    
    company_name=models.CharField(max_length=96, unique=True, blank=True)
    flight_fares=models.CharField(max_length=96, unique=True, blank=True)
    baggage_allowance=models.CharField(max_length=96, unique=True, blank=True)

#Flight class providing information regarding the flight number, zone number, number of passengers, flight destination, flight origin, terminal number, departure date, arrival date, status and pilot and travel agency both foreign keys from their distinct classes

class Flight(models.Model):
    id = models.AutoField(primary_key = True)
    flight_number=models.IntegerField(unique=True, blank=True)
    zone=models.CharField(max_length=96, unique=True, blank=True)
    passengers=models.IntegerField(unique=True, blank=True)
    flying_from=models.CharField(max_length=96, unique=True, blank=True)
    flying_to=models.CharField(max_length=96, unique=True, blank=True)
    terminal_number=models.IntegerField(unique=True, blank=True)
    departure_date=models.DateField(max_length=96, unique=True, blank=True)
    arrival_date=models.DateField(max_length=96, unique=True, blank=True)
    status=models.CharField(max_length=96, unique=True, blank=True)
    pilot=models.ForeignKey(Pilot)
    travelagency=models.ForeignKey(TravelAgency)