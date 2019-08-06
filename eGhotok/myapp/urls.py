from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [

    path('', views.login_view,name='login_page'),
    path('home',views.home,name='home'),
    path('home/male',views.home_male,name='home_male'),
    path('home/female',views.home_female,name='home_female'),
    path('logout/',views.logout_view,name='logout_page'),
    path('complete_profile',views.complete_profile_view,name='complete_profile'),
    path('edit',views.edit_profile_view,name="edit_profile"),
    path('profile/<slug:slugtxt>',views.profile,name="profile"),
    path('delete_account',views.deleteAc_view,name="deleteAc")

]
