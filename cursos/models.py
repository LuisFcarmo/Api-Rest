from django.db import models

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add = True)
    atualizacao = models.DateTimeField(auto_now = True)
    ativo = models.BooleanField(default = True)
    
    class Meta:
        abstract = True
    
class Curso(Base):
    titulo = models.CharField(max_length=250)
    url = models.URLField(unique = True)
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['id']
        
    def __str__(self) -> str:
        return self.titulo
        
class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name = 'avaliacoes', on_delete = models.CASCADE)
    nome = models.CharField(max_length = 255)
    email = models.EmailField()
    comentario = models.TextField(blank = True, default = "")
    avaliacao = models.DecimalField(max_digits = 2, decimal_places = 1)
    
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "avliações"
        unique_together = ['email', 'curso']
        #orderar qual a ordem que os elementos seram serializados 
        ordering = ['id']
        
    def __str__(self) -> str:
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'