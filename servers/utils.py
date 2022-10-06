from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_mail_fn(request, sender, subject, message, to_email, user):
    sender = sender
    subject = subject
    message = message
    to_email = to_email
    store_name = request.META['HTTP_HOST']
    msg_html = render_to_string('mail_template/email.html', {
        'user': user,
        'subject': subject,
        'message': message,
        'sender': sender,
        'store': store_name,
    })
    send_mail(
        subject,
        message,
        sender,
        [to_email],
        html_message=msg_html,
    )
