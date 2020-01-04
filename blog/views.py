from django.shortcuts import render, get_object_or_404
from .models import blog
# Create your views here.
def allblog(request):
    blogs = blog.objects
    return render(request,'blog/allblog.html',{'blogs':blogs})

def detail(request,blog_id):
    blogdetail = get_object_or_404(blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blogdetail})
