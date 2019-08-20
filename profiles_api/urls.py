from django.urls import path
from django.urls import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewset)
router.register('feed', views.ProfileFeedItemViewSet)

urlpatterns = [
    path('hello-view/',views.HelloAPIView.as_view()),
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]
