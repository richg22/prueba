from django.http import HttpResponse
from django.shortcuts import render
from nuevapp.tasks import send_async_email, send_winner_email


# Create your views here.
def home(request):
    return render(request, "index.html")


def send_example_email(request):
    try:
        send_async_email.delay()
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {str(e)}")


def send_email_winner(email):
    try:
        send_winner_email.delay()
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {str(e)}")
