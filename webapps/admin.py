from django.contrib import admin
from .models import Address, TravelCategory, Comments, Travels

admin.site.register([Address, TravelCategory, Comments, Travels])
