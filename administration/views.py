from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
from authentication.models import Student

def dashboard(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MessageForm()
    messages = Message.objects.all()
    students = Student.objects.all()
    return render(request, 'administration/dashboard.html', {'form': form, 'messages': messages, 'students': students})
