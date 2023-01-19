from django.urls import path
from . import views
app_name='credentials'
urlpatterns=[

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('newpage',views.newpage,name='newpage'),
    path('logout',views.logout,name='logout'),
    path('application',views.application,name='application'),
    path('logout',views.logout,name='logout'),
    path('form', views.person_create_view, name='form'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]