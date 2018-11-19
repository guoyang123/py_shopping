import xadmin

from .models import EmaiVerfyRecord


class EmailVerifyRecordAdmin(object):
    # 定义后台列表显示字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 定义搜索字段
    search_fields = ['code', 'email', 'send_type']
    # 定义过滤字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmaiVerfyRecord, EmailVerifyRecordAdmin)