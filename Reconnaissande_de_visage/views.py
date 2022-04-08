from django.shortcuts import render
from .forms import FormSaveForms
from django.contrib import  messages


def template_view(request):
    return render(request, 'template.html')

def home_view(request):
    return render(request, 'home.html')

def ajouter_view(request):

    """if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        telephone = request.POST['telephone']
        date_Naissance = request.POST['date_Naissance']
        nni = request.POST['nni']
        email = request.POST['email']
        photo = request.FILES['photo']
        niveau_id = request.POST['niveau_id']
        filiere_id = request.POST['filiere_id']
        etudiant = etudiants(nom=nom,prenom=prenom,telephone=telephone,nni=nni,date_Naissance=date_Naissance,
                             email=email,photo=photo,niveau_id=niveau_id,filiere_id=filiere_id)
        etudiant.save()"""
    if request.method == 'POST':
        form = FormSaveForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Insertion avec success")
            return render(request, 'home.html',)
        else:
            return render(request, 'ajouter.html',{"form":form})
    else:
        form = FormSaveForms(None)
        return render(request, 'ajouter.html',{"form":form})

