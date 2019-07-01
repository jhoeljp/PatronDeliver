# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
from imageupload.settings import MEDIA_ROOT, MEDIA_URL


class Home(TemplateView):
    template_name = 'home.html'
class AboutPageView(TemplateView):
    template_name = 'about.html'
class PaymentPageView(TemplateView):
    template_name = 'payment.html'
def main(request):
    imgs = Image.objects.all()
    return render_to_response('index.html', {'images': imgs, 'media_root': MEDIA_ROOT, 'media_url': MEDIA_URL})
