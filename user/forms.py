from django import forms
import re

from django.core.exceptions import ValidationError

from .models import AppUser
from .widgets import SendEmailButton, ImgWidget, IDWidget


class AppUserForm(forms.ModelForm):
    id = forms.CharField(widget=IDWidget, disabled=True)
    name = forms.CharField(min_length=8,
                           max_length=20,
                           required=True,
                           error_messages={
                               'required': '账号不能为空',
                               'max_length': '账号长度不能超过20个字符',
                               'min_length': '账号长度不能少于8个字符'
                           })
    auth_key = forms.CharField(widget=forms.PasswordInput,
                               label='口令',
                               min_length=6,
                               error_messages={
                                   'required': '口令不能为空',
                                   'min_length': '口令不少于6位'
                               })
    phone = forms.CharField(max_length=11,
                            min_length=11,
                            required=False)
    # 通过widget属性指定自定义widget组件
    email = forms.CharField(required=False,
                            widget=SendEmailButton)
    img1 = forms.CharField(max_length=100, widget=ImgWidget)

    class Meta:
        model = AppUser
        # fields = '__all__'
        fields = ('id', 'img1', 'name', 'auth_key', 'phone', 'email')


    def is_valid(self):
        return super().is_valid()

    # 以上验证通过后，进入这个方法继续验证
    # 必须包含大写、小写和数字
    def clean_auth_key(self):
        auth_key = self.cleaned_data.get('auth_key')
        if all((
           re.search(r'\d+', auth_key),
           re.search(r'[a-z]+', auth_key),
           re.search(r'[A-Z]+', auth_key),
        )):
            return auth_key
        raise ValidationError('口令必须包含大写、小写和数字')



