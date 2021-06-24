from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}


@admin.register(Player)
class PlayAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}