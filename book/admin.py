from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # list_display = ('name', 'start_date', 'end_date', 'created_at')
    list_display = ('name', 'created_at')
    # list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'description')
    # date_hierarchy = 'start_date'
    ordering = ('-created_at',)