from django.shortcuts import render, HttpResponse, redirect
from .models import Post, BlogComment
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    posts = Post.objects.all()
    comments = BlogComment.objects.all()
    context = {'posts' : posts , 'comments' : comments, 'user':request.user}
    return render(request, 'blog/blogindex.html', context) 


def blog(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.all()
    context = {'post': post , 'comments' : comments, 'user':request.user}
    return render(request, 'blog/blogpost.html', context)

def signup(request):
    print('till save')

    if request.method=="POST":
        print('till save')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['spass']
        email = request.POST['email']
        myuser = User.objects.create_user(username, email, password)
       
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        messages.success(request, "You have successfully signed up!!")
        return redirect('home')

    else: 
        return HttpResponse('404 NOT FOUND')

def handlelogin(request):
    if request.method == "POST":
        username = request.POST['luser']
        password = request.POST['lpass']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged in ")
            return redirect('home')
        else:
            messages.success(request, "Invalid credentials")
            return redirect('home')
    else:
        return HttpResponse('404 not found')

def handlelogout(request):
    logout(request)
    return redirect('home')


def blogComment(request):
    if request.method == "POST":
        user = request.user
        postno = request.POST['postno']
        comment = request.POST['comment']
        post = Post.objects.get(id=postno)

        postcomment = BlogComment(comment= comment, post= post, user=user)
        postcomment.save()
        messages.success(request, "Comment Posted successfully")

    return redirect(f"/blog/{post.slug}")

def handlesearch(request):
    query = request.GET['query']
    title = Post.objects.filter(title__icontains=query)
    content = Post.objects.filter(content__icontains=query)
    author = Post.objects.filter(author__icontains=query)
    allPosts = title.union(content, author)

    if allPosts.count() <= 0:
        messages.success(request, "No search results found")
    context = {'allPosts':allPosts, 'query':query}
    return render(request, 'blog/search.html', context)



        