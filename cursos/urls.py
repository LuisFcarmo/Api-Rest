from django.urls import path
from .genericviews import CursosApiView, AvaliacoesApiView
from .genericviews import CursoApiView, AvaliacaoApiView
from .genericviews import AvalicaoViewSet, CursoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvalicaoViewSet)

urlpatterns = [
    #endpoints for collections
    path("cursos/", CursosApiView.as_view(), name = 'cursos'),
    path("avaliacoes/", AvaliacoesApiView.as_view(), name = 'avaliacoes'),
    #endpoints for objects
    path("cursos/<int:pk>", CursoApiView.as_view(), name = 'cursos'),
    #querys 
    path("cursos/<int:curso_pk>/avaliacoes/", AvaliacoesApiView.as_view(), name = 'curso_avaliacoes'),
    path("cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>", AvaliacaoApiView.as_view(), name = 'curso_avaliacao'),
    path("avaliacoes/<int:pk>", AvaliacaoApiView.as_view(), name = 'avaliacoes')   

    #======================= routes from V2 api ========================#
    #foram gerados dinamicamente
    #===================================================================#

]
