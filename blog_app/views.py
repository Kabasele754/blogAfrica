from django.shortcuts import render

from .models import CultureAfrica

# Create your views here.
def index_view(request, templat_name="blog/index.html"):
    blog_africa = CultureAfrica.objects.all()
    context = {}
    context['blog_africas']= blog_africa
    return render(request, templat_name, context)

def about_view(request, templat_name="blog/about.html"):
    return render(request, templat_name)

def contact_view(request, templat_name="blog/contact.html"):
    return render(request, templat_name)