from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import ContactSubmission

class ContactAdmin(ModelAdmin):
    model = ContactSubmission
    menu_label = 'Submission'
    menu_icon = 'pilcrow'
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('email', 'message',)
    list_filter = ('email',)
    search_fields = ('email',)

modeladmin_register(ContactAdmin)
