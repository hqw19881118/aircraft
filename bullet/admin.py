from django.contrib import admin
from bullet.models import BulletInfo


# Register your models here.
admin.site.register(BulletInfo)
#
# class BulletInfoAdmin(admin.ModelAdmin):
#     search_fields = ['made_in', 'bullet_model']
#     list_filter = ('made_date', 'made_in')
#     list_display = ('made_date', 'made_in', 'bullet_model', 'bullet_num', 'bullet_price')
#     ordering = ('-made_date', 'bullet_price')
#
# admin.site.register(BulletInfo, BulletInfoAdmin)
