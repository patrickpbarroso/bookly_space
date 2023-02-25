from django.contrib import admin
from biblioteca.models import Resenha

class ListandoResenhas(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'legenda')
    list_display_links = ('id','titulo')
    search_fields = ('titulo',)

admin.site.register(Resenha, ListandoResenhas)
