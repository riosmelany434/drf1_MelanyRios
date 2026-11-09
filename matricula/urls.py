from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudianteViewSet, CursoViewSet, MatriculaViewSet

router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'crud', MatriculaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]