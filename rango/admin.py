from django.contrib import admin
from rango.models import Category, Page, PageAdmin, UserProfile

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')

