from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from registration import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('', views.home, name='home'),
    path('profile/', views.profile_page, name='profile'),
    path('about/', views.about_page, name='about')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



