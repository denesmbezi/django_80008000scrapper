from django.contrib import admin
from .models import JobListing

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'location', 'created_at']
    list_filter = ['location', 'created_at']
    search_fields = ['job_title', 'location']
    readonly_fields = ['created_at']