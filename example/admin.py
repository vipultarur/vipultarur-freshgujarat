from django.contrib import admin
from .models import Banner, Classcis, Events, Gallary, Masessage,Services , About, Title, links , Profile
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('username',)
    
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

class BannerAdmin(admin.ModelAdmin):
    list_display=('name','status')
    
class EventAdmin(admin.ModelAdmin):
    list_display=('name','status')

class ServicesAmin(admin.ModelAdmin):
    list_display=('name','status')

class ClasscisAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=('name','slug','price','status')

class AboutAmin(admin.ModelAdmin):
    list_display=('name','location','status')

class MasessageAdmin(admin.ModelAdmin):
    list_display=('name','des','status')

class GallaryAdmin(admin.ModelAdmin):
    list_display=('name','status')

class linksAdmin(admin.ModelAdmin):
    list_display=('name','url','status')
    
class TitleAdmin(admin.ModelAdmin):
    list_display=('name','url','status')

class ProfileAdmin(admin.ModelAdmin):
    list_display=('Enrollment','user','cource','number')

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Title,TitleAdmin)
admin.site.register(Banner,BannerAdmin)
admin.site.register(Events,EventAdmin)
admin.site.register(Services,ServicesAmin)
admin.site.register(About,AboutAmin)
admin.site.register(Masessage,MasessageAdmin)
admin.site.register(Gallary,GallaryAdmin)
admin.site.register(links,linksAdmin)
admin.site.register(Classcis,ClasscisAdmin)
admin.site.register(Profile,ProfileAdmin)
