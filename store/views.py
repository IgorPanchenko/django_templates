from django.shortcuts import render
from tg_message import send_message
from django.contrib import messages
from store.models import Blog, Project, Subscription, Team, Message
from store.forms import MessageForm, SubscriptionForm

def index(request):
    blog = Blog.objects.all()[:4]
    projects = Project.objects.all()[:2]
    context = {
        'projects': projects,
        'path': request.path,
        'blog': blog

    }
    return render(request, 'store/index.html', context)


def about(request):
    team = Team.objects.all()
    context = {
        'path': request.path,
        'team': team,
    }
    return render(request, 'store/about.html', context)

def blog(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            Subscription.objects.create(email=form.cleaned_data['email'])
    form = SubscriptionForm()
    blog = Blog.objects.all()
    context = {
        'form': form,
        'path': request.path,
        'blog': blog
    }
    return render(request, 'store/blog.html', context)    

def blog_detaile(request, id):
    post = Blog.objects.get(pk=id)
    context = {
        'path': request.path,
        'post': post
    }
    return render(request, 'store/blog_detaile.html', context) 

def contact(request):
    if request.method == "POST":
        form = MessageForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            send_message(form.cleaned_data['first_name'], form.cleaned_data['last_name'], form.cleaned_data['email'], form.cleaned_data['message'])
            messages.success(request, 'Сообщение отправлено!')
            return render(request, 'store/contact.html')
    else:
        form = MessageForm()
    context = {
            'form': form,
            }
    return render(request, 'store/contact.html', context)  


def project(request):
    projects = Project.objects.all()
    context = {
        'path': request.path,
        'projects': projects,
        }
    return render(request, 'store/project.html', context)

def services(request):
    context = {
        'path': request.path,
        }
    return render(request, 'store/services.html', context)


def single(request):
    context = {
        'path': request.path,
        }
    return render(request, 'store/single.html', context)