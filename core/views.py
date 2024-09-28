from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import ScannedQR
import json
from django.http import JsonResponse




# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')


def logout_view(request):
    if request.method == 'GET':
        auth_logout(request)
        return render(request, 'login.html', {'success': 'Logout successful'})
    else:
        return render(request, 'login.html', {'error': 'Invalid request method'})

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, 'login.html', {'success': 'Login successful'})
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html', {'error': 'Invalid request method'})

@login_required
def register_qr(request):
    if request.method == 'GET':
        return render(request, 'register_qr.html')
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            country = data.get('country')
            role = data.get('role')
            
            # Check if the record already exists
            if ScannedQR.objects.filter(name=name, country=country, role=role).exists():
                return JsonResponse({'error': 'QR code already registered'}, status=400)
            
            # Create the record if it doesn't exist
            ScannedQR.objects.create(name=name, country=country, role=role)
            return JsonResponse({'success': 'QR code registered successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)