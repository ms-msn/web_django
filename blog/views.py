from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Hh_vacancy, Vacancy, Responsibility, Vendors_technologies

def index(request):
    latest_vacancy_list = Hh_vacancy.objects.order_by('id')[:100]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_vacancy_list': latest_vacancy_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    try:
        vacancy = Vacancy.objects.get(vacancy_id=id)
        competences = Responsibility.objects.filter(vacancy_id=id).first()
        list_competences = competences.name_list.replace('[','').replace(']','')
        list_competences = list_competences.split(',')
        list_associated = competences.associated.split(',')

    except Vacancy.DoesNotExist:
        raise Http404("Vacnacy does not exist")
    return render(request, 'blog/detail.html', {'vacancy': vacancy, 'competences': list_competences , 'associated': list_associated})


def listing(request):
    vacancy_list =Hh_vacancy.objects.all()
    paginator = Paginator(vacancy_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    vacancy_p = paginator.get_page(page)
    return render(request, 'blog/index.html', {'vacancy_p': vacancy_p})

def vend_teh(request, name):
    try:
        vendors_technologies = Vendors_technologies.objects.get(name=name)
    except Vendors_technologies.DoesNotExist:
        raise Http404("DoesNotExist")
    return render(request, 'blog/vendor_tehn.html', {'vendors_technologies': vendors_technologies})