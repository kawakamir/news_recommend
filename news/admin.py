from django.contrib import admin
from .models import Pick

# Register your models here.

@admin.register(Pick)
class Pick(admin.ModelAdmin):
  pass
