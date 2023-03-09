from django.urls import path, include

from app.views import *
from django.db import router
from django.conf import settings
from .views import *
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("fanlar",FanlarViewSet)
router.register("level", LevelViewSet)
router.register("test", TestViewSet)
urlpatterns = [
    path('api', include(router.urls)),
    path('home', all, name="fann"),
    path('', home ,name="object"),
    path('quiz/<int:test_id>', index ,name="quiz"),
    path('final/', TestView.as_view() ,name="finall"),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)