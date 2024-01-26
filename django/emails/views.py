from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import subprocess

import sys
sys.path.append('../')


# Create your views here.
def get_emailpage(request):
    return render(request, 'emails.html', {'name': 'Beijie'})

def summarize_emails(request):
    # Call your Python function here
    result = subprocess.check_output(['python', '../semantic_kernel/summarize_emails.py'])
    return HttpResponse(result)

# def generate_email_reply(request):
#     # Call your Python function here
#     result = subprocess.check_output(['python', '../semantic_kernel/summarize_emails.py'])
#     return HttpResponse(f"Python function executed: {result}")