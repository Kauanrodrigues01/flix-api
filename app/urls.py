from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', include('genres.urls')),
    path('actors/', include('actors.urls')),
    path('movies/', include('movies.urls'))
]