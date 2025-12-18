from django.core.mail import send_mail

def handlesendemail():  
        urlmessage='http://localhost:3000/verify'
        send_mail(
            subject='Verificacion de correo',
            message=f'Crea tu contraseña el siguiente link: {urlmessage}',
            from_email='richardg040702@gmail.com',
            recipient_list=['rich.gutierrez@duocuc.cl'],
            fail_silently=False,
        )