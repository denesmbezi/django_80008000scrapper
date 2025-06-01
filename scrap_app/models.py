from django.db import models
from django.utils import timezone

class JobListing(models.Model):
    job_title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    link_to_apply = models.URLField(max_length=1000)  # Increased for long LinkedIn URLs
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['job_title', 'location', 'link_to_apply']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.job_title} - {self.location}"