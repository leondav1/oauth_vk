from django.contrib import admin

# Register your models here.
from .models import Access


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    pass
