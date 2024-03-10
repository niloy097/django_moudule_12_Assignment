from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.show_item, name = 'show_item'),
    path('about_us/', include('about_us.urls'))
]