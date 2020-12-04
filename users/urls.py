from users import views
from django.urls import path

app_name="users"
urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('', views.index.as_view(), name="index"),

]
