from django.db import models

# Create your models here.

class Base(models.Model):
    criado = models.DateField('criado', auto_now_add=True)
    modificado = models.DateField('alterado', auto_now_add=True)
    ativo = models.BooleanField('Ativo?',default=True )

    class Meta:
        abstract = True


class Autores(Base):
    nome = models.CharField('nome', max_length=100)

    def __str__(self):
        return self.nome

class Editoras(Base):
    nome = models.CharField('nome', max_length=150)

    def __str__(self):
        return self.nome

class Livros(Base):
    nome = models.CharField('nome',max_length=100)
    autor = models.ForeignKey('core.autores', on_delete=models.CASCADE)
    editora = models.ForeignKey('core.editoras', on_delete=models.CASCADE)
    preco = models.DecimalField('preco', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
