# Import necessary modules from Django and the models to be used in the admin interface.
from django.contrib import admin
from api.models import User,Profile, Todo, ChatMessage

# Define the admin configuration for the User model.
class UserAdmin(admin.ModelAdmin):
    # Specify which fields to display in the list view of the admin interface.
    list_display = ['username', 'email']

# Define the admin configuration for the Profile model.
class ProfileAdmin(admin.ModelAdmin):
    # Allow the 'verified' field to be editable directly in the list view.
    list_editable = ['verified']
    # Specify which fields to display in the list view of the admin interface.
    list_display = ['user', 'full_name' ,'verified']

# Define the admin configuration for the Todo model.
class TodoAdmin(admin.ModelAdmin):
    # Allow the 'completed' field to be editable directly in the list view.
    list_editable = ['completed']
    # Specify which fields to display in the list view of the admin interface.
    list_display = ['user', 'title' ,'completed', 'date']

# Define the admin configuration for the ChatMessage model.
class ChatMessageAdmin(admin.ModelAdmin):
    # Allow the 'read' field to be editable directly in the list view.
    list_editable = ['read']
    # Specify which fields to display in the list view of the admin interface.
    list_display = ['sender', 'reciever' ,'message', 'read']

# Register the admin configurations with the Django admin site.
admin.site.register(User, UserAdmin)
admin.site.register( Profile,ProfileAdmin)
admin.site.register( Todo,TodoAdmin)
admin.site.register( ChatMessage, ChatMessageAdmin)

