from django.shortcuts import render
from .models import BlogData
from .forms import Blogger

# Create your views here.
def backend(request):
    form=Blogger()
    if request.method=="POST":
        author=request.POST['author']
        blog_title=request.POST['blog_title']
        date=request.POST['date']
        blog=request.POST['blog']
        tags=request.POST['tags']
        image=request.POST['image']
        blogsave=BlogData(date=date,author=author,blog_title=blog_title,blog=blog,tags=tags,image=image)
        blogsave.save()
    else:
        form=Blogger()
    return render(request,"adminpanel.html",{'form':form})
def homepage(request):
    obj=BlogData.objects.all()
    return render(request,'homepage.html',{'obj':obj})
    
