
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employee', views.EmployeeViewSet,basename='employee')

urlpatterns = [
    path('student/', views.studentAPI,name='studentAPI'),
    path('student/<int:pk>/', views.studentIDAPI,name='studentidAPI'),
    
    path('', include(router.urls)),
]
