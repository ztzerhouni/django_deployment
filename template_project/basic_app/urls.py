from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('relative_url_templates/', views.relative_url_templates, name='relative_url_templates'),
    path('other/', views.other, name='other'),
    path('registration/', views.registration, name='registration'),
    path('user_login/',views.user_login,name='user_login'),

]