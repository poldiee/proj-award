from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('users', views.UserViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('project/<post>', views.project, name='project')
] 