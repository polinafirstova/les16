from django.shortcuts import render, redirect
from .models import Course
from .forms import ContactForm


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            return render(request, 'contact_success.html', {
                'name': name,
                'email': email,
                'message': message
            })
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
