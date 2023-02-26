from django.contrib import admin
from biblioteca.models import Resenha

class ListandoResenhas(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'legenda', 'publicada')
    list_display_links = ('id','titulo')
    search_fields = ('titulo',)
    list_filter = ("categoria",)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Resenha, ListandoResenhas)
