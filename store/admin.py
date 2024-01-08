from django.contrib import admin

from store.models import Blog, Project, Subscription, Team, Message

admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Team)
admin.site.register(Message)
admin.site.register(Subscription)

