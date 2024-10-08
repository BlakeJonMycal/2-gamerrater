from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from raterapi.views import register_user, login_user, GameView
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'game')




urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
