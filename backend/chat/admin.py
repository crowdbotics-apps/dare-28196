from django.contrib import admin
from .models import (
    Message,
    Thread,
    ForwardedMessage,
    ThreadAction,
    MessageAction,
    ThreadMember,
)

admin.site.register(Thread)
admin.site.register(ThreadMember)
admin.site.register(Message)
admin.site.register(MessageAction)
admin.site.register(ThreadAction)
admin.site.register(ForwardedMessage)

# Register your models here.
