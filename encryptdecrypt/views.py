from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import Note
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from textwrap import wrap
from pyperclip import copy
import os, hashlib
from . import aes
from colorama import Fore

# Create your views here.


def index(request):
    user = request.user

    if request.user.is_authenticated:
        return render(request, 'encryptdecrypt/index.html', context={'type':2})
    else:
        return render(request, 'encryptdecrypt/index.html', context={'type':3})


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("Hello")
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account Created')
            return redirect('encryptdecrypt:home')
    cxt = {'form': form}
    return render(request, 'encryptdecrypt/signup.html', cxt)



def home(request):

    if request.user.is_authenticated:
        user = request.user
        username = request.user.username
        print("Hello")
        notes_data = Note.objects.filter(author=user)
        return render(request, 'encryptdecrypt/showall.html', context={'notes_data': notes_data, 'type': 2, 'username' : username})
    else:
        print("Hello")
        # notes_data = Note.objects.filter(author=user)
        # return render(request, 'encryptdecrypt/index.html', context={'type': 3})
        return redirect('../')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('../')

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def clear(request):
    if request.user.is_authenticated:
        user = request.user
        username = request.user.username
        notes = Note.objects.filter(author = user)
        for note in notes:
            note.delete()
        notes_data = Note.objects.filter(author=user)
        return render(request, 'encryptdecrypt/showall.html', context={'notes_data': notes_data, 'type': 2, 'username' : username})
    else:
        print("Hello")
        # notes_data = Note.objects.filter(author=user)
        # return render(request, 'encryptdecrypt/index.html', context={'type': 3})
        return redirect('../')
    

def encryptor(request):
    user = request.user

    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('encrypt'):

                note = Note()
                fer = aes.FernetCipher()
                encrypted = fer.encrypt(request.POST.get('encrypt'))


                # encrypted = aes.AES(key).encrypt_ctr(bytes(, encoding='utf8'), iv)
                note.data = str(encrypted)[2:-1]
                note.author = user

                note.save()

                notes_data = str(encrypted)[2:-1]
                return render(request, 'encryptdecrypt/encryptor.html', context={'notes_data': notes_data, 'type': 2})
        else:
            print("Hello")
            notes_data = Note.objects.filter(author=user)
            return render(request, 'encryptdecrypt/encryptor.html', context={'type': 2})

    else:
        if request.method == 'POST':
            if request.POST.get('encrypt'):

                note = Note()
                fer = aes.FernetCipher()
                encrypted = fer.encrypt(request.POST.get('encrypt'))
                # encrypted = encrypted.slice()
                notes_data = str(encrypted)[2:-1]
                return render(request, 'encryptdecrypt/encryptor.html', context={'notes_data': notes_data, 'type': 3})
        else:
            print("Hello")
            return render(request, 'encryptdecrypt/encryptor.html', context={'type': 3})


def decryptor(request):
    user = request.user

    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('decrypt'):

                fer = aes.FernetCipher()
                try:
                    encrypted = fer.decrypt(request.POST.get('decrypt'))
                except:
                    return render(request, 'encryptdecrypt/decryptor.html', context={'msgs': "Incorrect Data..!!", 'type': 2})
                    
                notes_data = str(encrypted)[2:-1]
                return render(request, 'encryptdecrypt/decryptor.html', context={'notes_data': notes_data, 'type': 2})
        else:
            print("Hello")
            notes_data = Note.objects.filter(author=user)
            return render(request, 'encryptdecrypt/decryptor.html', context={'type': 2})

    else:
        if request.method == 'POST':
            if request.POST.get('decrypt'):

                note = Note()
                fer = aes.FernetCipher()
                try:
                    encrypted = fer.decrypt(request.POST.get('decrypt'))
                except:
                    return render(request, 'encryptdecrypt/decryptor.html', context={'msgs': "Incorrect Data..!!", 'type': 2})
                
                notes_data = str(encrypted)[2:-1]
                return render(request, 'encryptdecrypt/decryptor.html', context={'notes_data': notes_data, 'type': 3})
        else:
            print("Hello")
            return render(request, 'encryptdecrypt/decryptor.html', context={'type': 3})