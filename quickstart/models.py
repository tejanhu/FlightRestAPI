from django.db import models

# Create your models here.

#class Position(models.Model):
#    id = models.AutoField(primary_key = True)    
 #   rank=models.CharField(max_length=96, unique=True, blank=True)
  #  badge=models.CharField(max_length=96, unique=True, blank=True)
    
#class Pilot(models.Model):
#    id = models.AutoField(primary_key = True)
#    name=models.CharField(max_length=96, unique=True, blank=True)
#    position=models.ForeignKey(Position)

#class TravelAgency(models.Model):
#    id = models.AutoField(primary_key = True)    
#    company_name=models.CharField(max_length=96, unique=True, blank=True)
#    flight_fares=models.CharField(max_length=96, unique=True, blank=True)
#    baggage_allowance=models.IntegerField(unique=True, blank=True)


#class Flight(models.Model):
#    id = models.AutoField(primary_key = True)
#    flight_number=models.IntegerField(unique=True, blank=True)
#    zone=models.CharField(max_length=96, unique=True, blank=True)
#    passengers=models.IntegerField(unique=True, blank=True)
#    flying_from=models.CharField(max_length=96, unique=True, blank=True)
#    flying_to=models.CharField(max_length=96, unique=True, blank=True)
#    terminal_number=models.IntegerField(unique=True, blank=True)
#    departure_date=models.DateField(max_length=96, unique=True, blank=True)
#    arrival_date=models.DateField(max_length=96, unique=True, blank=True)
#    status=models.CharField(max_length=96, unique=True, blank=True)
#    pilot=models.ForeignKey(Pilot)
#    travelagency=models.ForeignKey(TravelAgency)