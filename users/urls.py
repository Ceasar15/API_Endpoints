from django.conf.urls import url
from django.urls import path
from .views import UserList, UserDetail


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:id>', UserDetail.as_view()),
    # url(r'^api/profile/', views.ProfileAPIView.as_view()),
]
