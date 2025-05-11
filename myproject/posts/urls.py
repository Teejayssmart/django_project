from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns = [
   
    path('', views.posts_list),
=======
app_name = 'posts'

urlpatterns = [
   
    path('', views.posts_list, name = "list"),
    path('<slug:slug>', views.post_page, name="page"),
>>>>>>> dfe5f18 (creating admin panel)
    
]