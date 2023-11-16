from django.contrib import admin
from .models import slider
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(slider)
class sliderAdmin(admin.ModelAdmin):
    list_display = ['photo_display', 'description']

    def photo_display(self, obj):
        return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % obj.photo_url)
