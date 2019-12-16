from django.contrib import admin
from . models import childrens, game_playing, parents
# Register your models here.
admin.site.register(childrens)
admin.site.register(game_playing)
admin.site.register(parents)