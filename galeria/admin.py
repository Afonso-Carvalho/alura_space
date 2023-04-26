from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografia(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id","nome")
    search_fields = ("nome",) # é um tupla por isso o uso obrigatorio da ","

admin.site.register(Fotografia,ListandoFotografia)