from django.core.mail import send_mail as dj_send_mail


def send_mail(title, message, receivers):
    print('------begin send mail')
    dj_send_mail(title, '', html_message=message,
                 from_email='heaven1124@qq.com',
                 recipient_list=receivers)
    print('------ send mail completely')
