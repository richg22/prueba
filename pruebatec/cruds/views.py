from django.shortcuts import render
from cruds.utils import handlesendemail
from nuevapp.tasks import test
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def send_example_email(request):
    try:        
        test.delay()
        return HttpResponse('Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Failed to send email: {str(e)}')