from django.urls import path
<<<<<<< HEAD
=======

>>>>>>> desenvolvendo
from usuarios.views import login, cadastro, logout

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
<<<<<<< HEAD
    path('logout', logout, name='logout')
]
=======
    path('logout', logout, name='logout'),
]
>>>>>>> desenvolvendo
