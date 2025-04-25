from django.urls import path
from .views import BookCreateView , BookListView , BookDeleteView , BookEditView

urlpatterns = [
    path('post/' , BookCreateView.as_view() , name="post"),
    path('get/' , BookListView.as_view() , name="get"),
    path('posts/<int:pk>/delete/', BookDeleteView.as_view(), name='delete'),
    path('posts/<int:pk>/update', BookEditView.as_view() , name="update" )

]