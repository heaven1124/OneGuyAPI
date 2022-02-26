from threading import Thread

from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.mail import send_mail as send_qq_email

from OneGuyAPI import settings
from common.mail import send_mail as my_send_mail


def send_mail(request, email):
    print('send_mail', email)
    subtitle = '用户激活通知'
    message = '<html>dear user shi, please activate firstly</html>'
    # send_qq_email(subtitle, '', html_message=message,
    #               from_email='heaven1124@qq.com',
    #               recipient_list=[email])

    Thread(target=my_send_mail,
           kwargs={
               'title': subtitle,
               'message': message,
               'receivers': [email]
           }).start()

    return JsonResponse({
        'msg': 'send success',
        'info': {
            'email': email
        }
    })


@csrf_exempt
def upload_img(request, user_id):

    # user_id 作为上传头像的文件名
    img1File: InMemoryUploadedFile = request.FILES.get('img1')

    return JsonResponse({
        'code': 200,
        'msg': '上传成功',
        'path': 'users/1.jpg'
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_mail/<email>/', send_mail),
    path('upload_img/<user_id>/', upload_img),
    path('user/', include('user.urls', namespace='user')),
]+static(settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT)
