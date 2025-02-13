from django.shortcuts import render , HttpResponse , get_object_or_404 , redirect
from .models import Link
from .forms import LinkForm
from django.urls import reverse 

# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        "links":links
    }
    return render(request , 'links/index.html' , context)

def root_link(request , link_slug):
    link = get_object_or_404(Link , slug = link_slug)
    link.click() #this increases the clicked field

    # here we dont render a template we just want to 
    # reirect the user to the specified url that is asociated with this link
    return redirect(link.url)

def add_link(request):
    if request.method == 'POST':
        #form has data
        form = LinkForm(request.POST)
        if form.is_valid():
            #process the data
            # print(form.cleaned_data)

            # save the data and return user to home page
            form.save()
            return redirect(reverse('home'))
    else:
        form = LinkForm()
    context ={
            "form":form
        }
    return render(request , 'links/create.html' , context)
