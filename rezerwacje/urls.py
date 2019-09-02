"""rezerwacje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from core.views import room_new_view, room_list_view, room_detail_view
from core.views import RoomModifyView, RoomDeleteView
    # Tworzenie formularza do stworzenia nowej sali ( /room/new).
    # Tworzenie nowej sali ( POST formularza na adres /room/new).
    # Tworzenie formularza do modyfikacji sali ( /room/modify/{id}).
    # Modyfikacja sali ( POST formularza na adres /room/modify/{id}).
    # Usunięcie podanej sali ( /room/delete/{id}).
    # Pokazanie danych jednej sali ( /room/{id})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/new', room_new_view),
    path('', room_list_view),
    re_path(r'^room/(?P<id>\d+)$', room_detail_view),
    re_path(r'^room/modify/(?P<id>\d+)$', RoomModifyView.as_view()),
    re_path(r'^room/delete/(?P<id>\d+)$', RoomDeleteView.as_view()),


]
