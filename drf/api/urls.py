
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'employee', views.EmployeeViewSet,basename='employee')

urlpatterns = [
    path('student/', views.studentAPI,name='studentAPI'),
    path('student/<int:pk>/', views.studentIDAPI,name='studentidAPI'),
    
    path('blog/', views.blogAPI.as_view(),name='blogAPI'),
    path('comment/', views.commentapi.as_view(),name='commentAPI'),
    path('', include(router.urls)),
]
