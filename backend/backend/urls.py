from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo.views import TodoView

router = routers.DefaultRouter()
router.register(r'todos', TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
