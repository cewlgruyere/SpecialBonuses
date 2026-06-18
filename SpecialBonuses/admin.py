from django.contrib import admin
from .models import SpecialBonuses

# Register your models here.
@admin.register(SpecialBonuses)
class SpecialBonusesAdmin(admin.ModelAdmin):
    list_display = ("special", "bonus")