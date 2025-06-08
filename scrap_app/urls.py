
from django.urls import path
from . import views

urlpatterns = [
    # path('api/save-jobs/', views.save_jobs_view, name='save_jobs'),
    # path('jobs/', views.jobs_list_view, name='jobs_list'),
    # path('debug-jobs/', views.debug_jobs_view, name='debug_jobs'),
    path('job/', views.jobs_list_view, name='home'),  # Optional home page
]