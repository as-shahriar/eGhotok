from django.contrib import admin
from myapp.models import UserInfo
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = UserInfo
admin.site.register(UserInfo,ProductAdmin)
