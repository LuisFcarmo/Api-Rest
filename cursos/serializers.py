from rest_framework import serializers
from .models import Curso, Avaliacao
        
class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = [
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        ]
        
class CursoSerializer(serializers.ModelSerializer):
    #nestedRelationShip menos performatica recomendado para poucos registros
    #avaliacoes = AvaliacaoSerializer(many = True, read_only = True)
    
    #hyperlinked related fild mais performatica recomendada para muitos registros
    #avaliacoes  = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name = "avaliacao-detail")
    
    #primary key related fild gera um campo com a chave primaria da avaliação
    avaliacoes = serializers.PrimaryKeyRelatedField(many = True, read_only = True) 
    
    class Meta:
        model = Curso
        fields = [
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        ]
