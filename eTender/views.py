from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import User, Need, Contract
from django import forms

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'user_type', 'district', 'province', 'gender', 'primary_id']

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def dashboard(request):
    if request.user.user_type == 'citizen':
        needs = Need.objects.all()
        contracts = Contract.objects.filter(status='advertised')
        return render(request, 'citizen_dashboard.html', {'needs': needs, 'contracts': contracts})
    elif request.user.user_type == 'agency':
        needs = Need.objects.filter(agency=request.user)
        return render(request, 'agency_dashboard.html', {'needs': needs})
    elif request.user.user_type == 'npc':
        needs = Need.objects.all()
        contracts = Contract.objects.filter(npc=request.user)
        return render(request, 'npc_dashboard.html', {'needs': needs, 'contracts': contracts})
    return render(request, 'dashboard.html')

@login_required
def add_need(request):
    if request.user.user_type == 'agency' and request.method == 'POST':
        description = request.POST['description']
        Need.objects.create(description=description, agency=request.user)
        return redirect('dashboard')
    return render(request, 'add_need.html')

@login_required
def advertise_contract(request):
    if request.user.user_type == 'npc' and request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Contract.objects.create(title=title, description=description, npc=request.user)
        return redirect('dashboard')
    return render(request, 'advertise_contract.html')