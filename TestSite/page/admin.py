from django.contrib import admin
from .models import slider
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
# Register your models here.


@admin.register(slider)
class sliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['order_field', 'description', 'photo_display']

    def photo_display(self, obj):
        return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % obj.photo.url)
