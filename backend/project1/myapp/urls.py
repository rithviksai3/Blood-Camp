from django.urls import path
from . import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('delete/<int:id>',views.delete,name='delete')
]
