from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import JobListing

@csrf_exempt
@require_http_methods(["POST"])
def save_jobs_view(request):
    """Receive jobs from FastAPI and save to database"""
    print(f"=== Django received {request.method} request ===")
    
    try:
        data = json.loads(request.body)
        jobs_data = data.get('jobs', [])
        print(f"=== Processing {len(jobs_data)} jobs ===")
        
        created_count = 0
        existing_count = 0
        
        for job_data in jobs_data:
            job, created = JobListing.objects.get_or_create(
                job_title=job_data['job_title'],
                location=job_data['location'],
                link_to_apply=job_data['link_to_apply']
            )
            
            if created:
                created_count += 1
                print(f"Created: {job.job_title}")
            else:
                existing_count += 1
                print(f"Already exists: {job.job_title}")
        
        result = {
            'success': True,
            'message': f'Processed {len(jobs_data)} jobs',
            'created': created_count,
            'existing': existing_count,
            'total': len(jobs_data)
        }
        
        print(f"=== Django response: {result} ===")
        return JsonResponse(result)
        
    except Exception as e:
        error_result = {
            'success': False,
            'error': str(e)
        }
        print(f"=== Django error: {error_result} ===")
        return JsonResponse(error_result, status=400)

def jobs_list_view(request):
    """Display all saved jobs in a template"""
    jobs = JobListing.objects.all().order_by('-created_at')
    return render(request, 'jobs/jobs_list.html', {'jobs': jobs})

def debug_jobs_view(request):
    """Debug view to see raw job data"""
    jobs = JobListing.objects.all()[:10]  # Get first 10 jobs
    debug_data = []
    
    for job in jobs:
        debug_data.append({
            'id': job.id,
            'job_title': job.job_title,
            'location': job.location,
            'link_to_apply': job.link_to_apply,
            'link_length': len(job.link_to_apply),
            'created_at': str(job.created_at)
        })
    
    return JsonResponse(debug_data, safe=False)