from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, FileUploadForm
from .models import UserFile

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    files = UserFile.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'home.html', {'files': files})

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            return redirect('home')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def delete_file(request, file_id):
    file = get_object_or_404(UserFile, id=file_id, user=request.user)
    file.file.delete()  # delete actual file
    file.delete()       # delete record from DB
    return redirect('home')
