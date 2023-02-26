from django.db import models
from datetime import datetime

class Resenha(models.Model):

    OPCOES_CATEGORIA = [
        ("Clássicos", "CLÁSSICOS"),
        ("Filosofia", "FILOSOFIA"),
        ("Ciência", "CIÊNCIA"),
        ("Biografias", "BIOGRAFIAS"),
        ("Fantasia", "FANTASIA"),
        ("Romance", "ROMANCE"),
        ("Terror", "TERROR")
    ]

    titulo = models.CharField(max_length=150, null=False, blank=False)
    autor = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default="")
    descricao = models.TextField(null=False, blank=False)
    imagem = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_postagem = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"Resenha [titulo={self.titulo}]"
    

