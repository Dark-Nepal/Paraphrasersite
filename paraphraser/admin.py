from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.models import Group
from .models import Contact, Site

class SiteAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'description',
        'image',
    )

    fieldsets = (
        ('Site',{
            'fields':(
                'title',
                'description',
                'link',

            )
        }),
        ('Image',{
            'fields':(
                'img',
            )
        }),
    )
     
    def image(self,obj):
        return mark_safe(
            f'<img src="{obj.img.url}" width"100" height="100" />'
        )


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'fullname',
        'email',
        'phone',
        'message'
    )



admin.site.register(Site, SiteAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)


