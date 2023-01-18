from django.urls import path
from . import views

app_name = "pakidex"
urlpatterns = [
    #ex: /pakidex/
    path("", views.IndexView.as_view(), name="index")
]