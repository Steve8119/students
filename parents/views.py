from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ParentSignInForm
from administration.models import Message
from authentication.models import Student, Unit, SchoolFees

def parent_sign_in(request):
    if request.method == 'POST':
        form = ParentSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            admission_number = form.cleaned_data['admission_number']
            student = Student.objects.get(username=username, admission_number=admission_number)
            request.session['student_id'] = student.id
            return redirect('parent_dashboard')
    else:
        form = ParentSignInForm()
    return render(request, 'parents/parent_sign_in.html', {'form': form})

@login_required
def parent_dashboard(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)
    return render(request, 'parents/parent_dashboard.html', {'student': student})

@login_required
def student_information(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    units = Unit.objects.filter(student=student)
    school_fees = SchoolFees.objects.filter(student=student).first()
    return render(request, 'parents/student_information.html', {
        'student': student,
        'units': units,
        'school_fees': school_fees,
    })



from django.shortcuts import render, get_object_or_404, redirect
from authentication.models import Student
from django import forms

class ReplyForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, max_length=500, required=True)

def parent_messages(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    messages = Message.objects.filter(student=student)

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            # Create a new message instance (reply)
            Message.objects.create(
                sender='Parent',  # You might want to replace this with actual parent info
                receiver='Administration',  # Adjust as necessary
                student=student,
                content=content,
            )
            return redirect('parent_messages', student_id=student_id)  # Redirect to the messages page
    else:
        form = ReplyForm()

    context = {
        'student': student,
        'messages': messages,
        'form': form,
    }
    
    return render(request, 'parents/parent_messages.html', context)
