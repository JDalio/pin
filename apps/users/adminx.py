import xadmin

from .models import Users, PhoneVerifyCode


class UsersAdmin(object):
    list_display = ['openid', 'nick_name', 'phone', 'gender', 'address', 'pick_code']
    search_fields = ['openid', 'nick_name', 'phone', 'gender', 'address', 'pick_code']
    list_filter = ['openid', 'nick_name', 'phone', 'gender', 'address', 'pick_code']


class PhoneVerifyCodeAdmin(object):
    list_display = ['code', 'phone', 'add_time']
    search_fields = ['code', 'phone']
    list_filter = ['code', 'phone', 'add_time']


xadmin.site.register(Users, UsersAdmin)
xadmin.site.register(PhoneVerifyCode, PhoneVerifyCodeAdmin)
