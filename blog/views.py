from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Hh_vacancy, Vacancy, Responsibility, Vendors_technologies, Post,Basic

def index(request):
    vacancy_p = Hh_vacancy.objects.order_by('id')[:6]
    post = Post.objects.order_by('id')[:3]
    return render(request, 'blog/index.html', {'vacancy_p': vacancy_p,'post': post})


def detail(request, id):
    try:
        vacancy = Vacancy.objects.get(vacancy_id=id)
        competences = Responsibility.objects.filter(vacancy_id=id).first()
        list_competences = competences.name_list.replace('[','').replace(']','').replace("'","")
        list_competences = list_competences.split(',')
        list_associated = competences.associated.split(',')
        vend_tehn = Vendors_technologies.objects.filter(name__in=[associated for associated in list_associated])
    except Vacancy.DoesNotExist:
        raise Http404("Vacnacy does not exist")
    return render(request, 'blog/detail.html', {'vacancy': vacancy, 'competences': list_competences , 'associated' : vend_tehn })


def listing(request):
    vacancy_list =Hh_vacancy.objects.all()
    paginator = Paginator(vacancy_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    vacancy_p = paginator.get_page(page)
    return render(request, 'blog/listing.html', {'vacancy_p': vacancy_p})

def vend_teh(request, name):
    try:
        vendors_technologies = Vendors_technologies.objects.get(name=name)
    except Vendors_technologies.DoesNotExist:
        raise Http404("DoesNotExist")
    return render(request, 'blog/vendor_tehn.html', {'vendors_technologies': vendors_technologies})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def detail_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail_post.html', {'post': post})

def basic(request, pk):
    basic = get_object_or_404(Basic, pk=pk)
    return render(request, 'blog/basic_detail.html', {'basic': basic})