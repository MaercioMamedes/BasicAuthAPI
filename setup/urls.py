from django.contrib import admin
from django.urls import path, include
from core.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
