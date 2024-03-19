from django.contrib import admin
from django.urls import path
from .views import my_login_view, nova_view, sistema_view, sistema2_view, sistema3_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_login_view, name='login'),  # URL para a página de login
    path('index/', nova_view, name='nova_view'),  # URL para a nova view
    path('sistema/', sistema_view, name='sistema_view'),  # URL para a página "sistema"
    path('sistema2/', sistema2_view, name='sistema2_view'),  # URL para a página "sistema2"
    path('sistema3/', sistema3_view, name='sistema3_view')  # URL para a página "sistema2"
]
