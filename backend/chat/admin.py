from django.contrib import admin
from .models import ChatMessage

# Register your models here.
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_obj', 'sender', 'content', 'timestamp')
    search_fields = ('sender__username', 'content')
    list_filter = ('class_obj', 'timestamp')