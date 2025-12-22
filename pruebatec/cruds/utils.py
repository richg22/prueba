from django.core.mail import send_mail


def handlesendemail(email, id):
    urlmessage = f"http://localhost:3000/verify?id={id}"
    send_mail(
        subject="Verificacion de correo",
        message=f"Crea tu contraseña el siguiente link: {urlmessage}",
        from_email="richardg040702@gmail.com",
        recipient_list=[email],
        fail_silently=False,
    )


def handlesendwinneremail(email):
    send_mail(
        subject="GANADOR DEL SORTEO",
        message="FELICIDADES HAZ GANDO EL SORTEO DE SAN VALENTIN",
        from_email="richardg040702@gmail.com",
        recipient_list=[email],
        fail_silently=False,
    )
