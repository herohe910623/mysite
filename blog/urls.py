from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    # path('', views.index),FBV 방식 주석처리 CBV로 진행할 것이다.
    # path('<int:pk>/', views.single_post_page), FBV 방식 주석처리 CBV로 진행할 것이다.


]