from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import subprocess
from django.http import JsonResponse


import sys
sys.path.append('../')


# Create your views here.
def get_emailpage(request):
    return render(request, 'emails.html', {'email_id': 'beijiezhang@microsoft.com'})

def summarize_emails(request):
    result = subprocess.check_output(['python', '../semantic_kernel/summarize_emails.py'])
    return HttpResponse(result)

def generate_email_reply(request):
    input_text = request.POST.get('input_email', 'no input')
    result = subprocess.check_output(['python', '../semantic_kernel/reply_email.py', input_text])
    return HttpResponse(result)

def process_input(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        
        return JsonResponse({'result': input_text})
    else:
        return JsonResponse({'error': 'Invalid request method'})