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

def detect_email_tone(request):
    input_text = request.POST.get('input_email_tone', 'no input')
    result = subprocess.check_output(['python', '../semantic_kernel/detect_email_tone.py', input_text])
    return HttpResponse(result)