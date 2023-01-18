from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pakidex/', include("pakidex.urls")),
    path('pakimon/', include("pakimon.urls")),
]
