from miapp.services import search_youtube
from miapp.services import search_birthday_by_separated_names
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def search_youtube_view(request):
    search = request.GET.get('search')
    response = search_youtube(search)
    return response

@csrf_exempt
def search_birthday_by_separated_names_view(request):
    name = request.GET.get('name')
    father_last_name = request.GET.get('father_last_name')
    mother_last_name = request.GET.get('mother_last_name')
    response = search_birthday_by_separated_names(name, father_last_name, mother_last_name)
    return response

@csrf_exempt
def search_birthday_by_full_name_view(request):
    fullname = request.GET.get('fullname')
    name, father_last_name, mother_last_name = separate_name(fullname)

    response = search_birthday_by_separated_names(name, father_last_name, mother_last_name)

    return response

def separate_name(fullname):
    prepositions = ["de", "del", "la", "las", "los", "y"]
    parts = fullname.split()
    
    name = []
    father_last_name = []
    mother_last_name = []
    
    # Procesar desde el final
    i = len(parts) - 1
    
    # Apellido materno
    mother_last_name = [parts[i]]
    i -= 1
    
    # Apellido paterno
    while i >= 0 and (parts[i].lower() in prepositions or not father_last_name):
        father_last_name.insert(0, parts[i])
        i -= 1
    
    # Resto es el nombre
    name = parts[:i+1]
    
    # Convertir listas a strings
    name = " ".join(name)
    father_last_name = " ".join(father_last_name)
    mother_last_name = " ".join(mother_last_name)
    
    return name, father_last_name, mother_last_name