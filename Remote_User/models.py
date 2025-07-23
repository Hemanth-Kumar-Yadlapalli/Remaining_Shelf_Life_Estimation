from django.db import models


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=100)       # Changed from TextField
    email = models.EmailField(max_length=100)         # Increased max_length for safety
    password = models.CharField(max_length=100)       # Changed from TextField
    phoneno = models.CharField(max_length=15)         # Changed from TextField
    country = models.CharField(max_length=50)         # Changed from TextField
    state = models.CharField(max_length=50)           # Changed from TextField
    city = models.CharField(max_length=50)            # Changed from TextField


class shelf_life_estimation(models.Model):
    Fid = models.CharField(max_length=100)
    Datesk = models.CharField(max_length=100)
    Item_Name = models.CharField(max_length=100)
    Departure_Date = models.CharField(max_length=100)
    From_Source = models.CharField(max_length=100)
    To_Destination = models.CharField(max_length=100)
    Logistics_Name = models.CharField(max_length=100)
    Temp = models.FloatField()
    Oxygen = models.FloatField()
    Carbon_Dioxide = models.FloatField()
    ethylene = models.FloatField()
    damage_due_to_vibration = models.FloatField()
    Humidity = models.FloatField()
    Prediction = models.CharField(max_length=255)


class detection_accuracy(models.Model):
    names = models.CharField(max_length=100)  # Changed from TextField
    ratio = models.CharField(max_length=50)   # Changed from TextField


class detection_ratio(models.Model):
    names = models.CharField(max_length=100)  # Changed from TextField
    ratio = models.CharField(max_length=50)   # Changed from TextField
