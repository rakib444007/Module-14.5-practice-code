from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta
# Create your models here.
import datetime
def comma_separated_validator(value):
    items = value.split(',')
    for item in items:
        if not item.strip():
            raise ValidationError("Each item must be a non-empty string.")

class Student(models.Model):
    # id = models.AutoField()
    
    roll = models.IntegerField(primary_key=True)
    name= models.CharField(max_length=20)
    boolean_field = models.BooleanField(default=True)
    # big_val =models.BigAutoField(primary_key=True)
    big_int_val = models.BigIntegerField(default=121323)
    binary = models.BinaryField(default=b'\x00\x00\x00\x00') 
    comma_separated_field = models.CharField(
        validators=[comma_separated_validator],
        max_length=255,default='Rakib,Korim',
    )
    date = models.DateField(default=datetime.date.today)
    date_time = models.DateTimeField(default=datetime.datetime.now)

    decimal = models.DecimalField(max_digits=5, decimal_places=2, default=22.00)  # Specify decimal_places
    duration = models.DurationField(default=timedelta(days=1, hours=5, minutes=30))
    email = models.EmailField(default='rh44007@gmail.com')

    
    float = models.FloatField(default=1.22)
    IpAddress = models.GenericIPAddressField(default='127.0.0.1')
    
    def __str__(self):
        return self.name

    
