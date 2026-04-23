from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('domains/', views.domains, name='domains'),
    path('hire-me/', views.hire_me, name='hire_me'),
    # path('test-email/', views.test_email, name='test_email'),
]