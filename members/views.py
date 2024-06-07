import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from PIL import Image
from .models import Member
from django.conf import settings
from .forms import Registration
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import uuid
import logging

logger = logging.getLogger(__name__)
def main(request):
    template = loader.get_template('login.html')
    context = {"base_url": settings.STATIC_ROOT }
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('registration.html')
    
    if request.method == 'POST':
        form = Registration(request.POST, request.FILES)
        logger.info(form.errors)
        if form.is_valid():
            try:
                validate_password(form.cleaned_data.get('password'))
                profile_picture = form.cleaned_data.get('profile')
                
                if profile_picture:
                    unique_filename = handle_uploaded_file(profile_picture)
                    form.instance.profile = unique_filename
                    form.save()
                return redirect('/')
            except ValidationError as e:
                form.add_error('password', e)
    else:
        form = Registration()
    return HttpResponse(template.render({'form': form}, request))
    
def handle_uploaded_file(f):
    unique_filename = str(uuid.uuid4()) + os.path.splitext(f.name)[1]
    file_path = os.path.join(settings.MEDIA_ROOT, 'profile', unique_filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Open the uploaded image
    image = Image.open(f)
    
    # Resize the image
    max_size = (300, 300)  # Define the maximum size
    image.thumbnail(max_size, Image.LANCZOS)
    
    # Save the resized image
    image.save(file_path)
    return unique_filename

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