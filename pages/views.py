from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def Home(request):

    return render(request,"template_Hola")

def Hola(request):
    return HttpResponse("Hola")


# 1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

class HomePageView(TemplateView):

    template_name="home.html"
