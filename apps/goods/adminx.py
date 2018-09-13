import xadmin

from .models import Goods


class GoodsAdmin(object):
    list_display=['name','grow_place','delicious_time','price','goods_cost','packing_cost','kind','is_new','add_time']
    search_fields=['name','grow_place','delicious_time','price','goods_cost','packing_cost','kind','is_new']
    list_filter=['name','grow_place','delicious_time','price','goods_cost','packing_cost','kind','is_new','add_time']

xadmin.site.register(Goods,GoodsAdmin)