from django.contrib import admin
from app.models import Tweet, State

class StateAdmin(admin.ModelAdmin):
	ordering = ('name',)

admin.site.register(Tweet)
admin.site.register(State, StateAdmin)
