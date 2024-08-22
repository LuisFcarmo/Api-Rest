from django.contrib import admin
from django.urls import path, include
from cursos.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('cursos.urls')),
    path('auth/', include('rest_framework.urls')),    
    #======================= routes from V2 api ========================#
    path('api/v2/', include(router.urls))
    #===================================================================#
]
