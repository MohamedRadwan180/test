from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name = "index"),
    path('finder/', views.finder, name='finder'),
    path('<int:event_id>/', views.details, name='details'),
    path('<int:event_id>/offer', views.offer, name='offer'),
    path('profile-page/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name = "events/login-page.html"), name='login'),
    path('logout/', views.logout_view, name = "logout"),
    path('<int:offer_id>/submit', views.submit_offer, name='submit_offer'),

]