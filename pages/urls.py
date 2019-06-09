from django.urls import path

from .views import Home, AboutPageView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/',AboutPageView.as_view(),name = 'about'),
]
