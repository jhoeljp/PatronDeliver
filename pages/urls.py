from django.urls import path

from .views import Home, AboutPageView
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/',AboutPageView.as_view(),name = 'about'),
    # path('test/',js_components.as_view(),name ='js')
]
