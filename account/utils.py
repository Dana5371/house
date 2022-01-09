from django.core.mail import send_mail
from house.celery import app


@app.task
def send_confirmation_code(email, activation_code):

    message = f"""Спасибо за регистрацию.
    Активируйте свой аккаунт по ссылке:
    http://127.0.0.1:3000/v1/api/account/activate/{activation_code}"""
    send_mail(
        'Активация аккаунта',
        message,
        'test@myproject.com',
        [email, ],
        fail_silently=False
    )