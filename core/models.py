from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome, self.sobrenome, self.email, self.data_nascimento