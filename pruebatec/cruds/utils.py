from django.core.mail import send_mail


def handlesendemail(email, id):
    urlmessage = f"http://localhost:3000/verify?token={id}"
    send_mail(
        subject="Verificacion de correo",
        message=f"Crea tu contraseña el siguiente link: {urlmessage}",
        from_email="richardg040702@gmail.com",
        recipient_list=[email],
        fail_silently=False,
    )
