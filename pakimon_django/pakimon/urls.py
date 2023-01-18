from django.urls import path
from . import views

app_name = "pakimon"
urlpatterns = [
    #ex: /pakimon/
    path("", views.IndexView.as_view(), name="index")
]