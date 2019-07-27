from django.urls import path, include
from .views import home_view, post_detail

app_name = "blog"

urlpatterns = [
    path('', view=home_view, name="home_view"),
    path('<int:pk>/', view=post_detail, name="post_detail"),
]