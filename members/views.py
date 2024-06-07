from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.conf import settings
from .forms import Registration
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

def main(request):
    template = loader.get_template('login.html')
    context = {"base_url": settings.STATIC_ROOT }
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('registration.html')
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            try:
                validate_password(form.cleaned_data.get('password'))
                form.save()
                return redirect('/')
            except ValidationError as e:
                form.add_error('password', e)
    else:
        form = Registration()
    return HttpResponse(template.render({'form': form}, request))
    


def view_allmembers(request):
    allmembers = Member.objects.all().values()
    template = loader.get_template('members.html')
    context = {'allmembers':allmembers}
    return HttpResponse(template.render(context,request))
def view_details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember':member
    }
    return HttpResponse(template.render(context,request))
def testing(request):
    template = loader.get_template('testing.html')
    context = {
        'fruits':['banana','orange','apple']
    }
    return HttpResponse(template.render(context, request))