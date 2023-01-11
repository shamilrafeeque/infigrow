from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('index/',views.index,name='index'),
    path('',views.home,name='home'),
    path('update_profile/<int:pk>/', views.update_profile, name='update_profile'),
    path('logout/',views.user_logout,name="logout"),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('ajax/check_email/', views.check_email, name='check_email'),

    

]



