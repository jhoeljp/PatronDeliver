from django.urls import path

from .views import Home, AboutPageView, PaymentPageView
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/',AboutPageView.as_view(),name = 'about'),
    path('payment/',PaymentPageView.as_view(),name = 'payment'),
    # path('test/',js_components.as_view(),name ='js')
]
