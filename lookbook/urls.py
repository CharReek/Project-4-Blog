from . import views
from django.urls import path

urlpatterns = [
    path('lookbook/', views.PostList.as_view(), name='lookbook'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='lookbook_post_detail'),
]
