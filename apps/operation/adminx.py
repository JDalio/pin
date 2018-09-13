import xadmin

from .models import Operation


class OperationAdmin(object):
    list_display=['userid','goodsid','state','number','operation_time']
    search_fields=['userid','goodsid','state','number']
    list_filter=['userid','goodsid','state','number','operation_time']

xadmin.site.register(Operation,OperationAdmin)