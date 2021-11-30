from django.urls import path, include
from .views import PersonViewSet, ProgramViewSet, ProgramInfoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'person_info', PersonViewSet)
router.register(r'program_info', ProgramViewSet)
router.register(r'program_bugs', ProgramInfoViewSet)


urlpatterns = [
    # TODO person_info 路由设置
    path('', include(router.urls)),
    path('api-person/', include('rest_framework.urls'), name="person_info_page"),
]
