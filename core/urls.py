from rest_framework import routers
from core.views import UserAppView


router = routers.DefaultRouter()
router.register('usuario', UserAppView, basename='UserApp')

