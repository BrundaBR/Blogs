from django.shortcuts import render
from .models import BlogData
from .forms import Blogger
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)





class PostListView(ListView):
    model = BlogData
    template_name = 'homepage.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'blog'
    ordering = ['-date_posted']
    


class PostDetailView(DetailView):
    model = BlogData
        


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogData
    fields = ['blog_title', 'blog']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)





# Create your views here.
def backend(request):
    form=Blogger()
    if request.method=="POST":
        author=request.POST['author']
        blog_title=request.POST['blog_title']
        date=request.POST['date']
        blog=request.POST['blog']
        tags=request.POST['tags']
        images=request.POST['image']
        blogsave=BlogData(date=date,author=author,blog_title=blog_title,blog=blog,tags=tags,image=images)
        blogsave.save()
        
    else:
        form=Blogger()
    return render(request,"adminpanel.html",{'form':form})
def homepage(request):
    obj=BlogData.objects.all()
    return render(request,'homepage.html',{'obj':obj})
    
