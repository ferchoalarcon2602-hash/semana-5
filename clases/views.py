
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import aprendiz
from .forms import aprendizform
import pokebase as pb 


def buscar_pokemon(request):

    pokemon = None
    error = None

    if request.method == "POST":

        nombre = request.POST.get("nombre", "").strip().lower()

        if nombre:

            try:
                # Consultar Pokémon mediante Pokebase
                pokemon_api = pb.pokemon(nombre)

                pokemon = {
                    "nombre": pokemon_api.name,
                    "id": pokemon_api.id,
                    "altura": pokemon_api.height / 10,
                    "peso": pokemon_api.weight / 10,
                    "imagen": pokemon_api.sprites.front_default,
                    "experiencia": pokemon_api.base_experience,
                    "tipos": [
                        tipo.type.name
                        for tipo in pokemon_api.types
                    ],
                }

            except Exception:
                error = "No se encontró el Pokémon. Intenta nuevamente."

        else:
            error = "Escribe el nombre de un Pokémon."

    return render(request, "clases/mapa.html", {
        "pokemon": pokemon,
        "error": error
    })



def mapa_interactivo(request):

    return render(
        request,
        'clases/mapa_interactivo.html'
    )








 
def listar(request):
    aprendices = aprendiz.objects.all()
    contexto = {
        'aprendices' : aprendices
    }

    return render(request, 'clases/index.html', contexto)




def crear_aprendiz(request):
    forms = aprendizform(request.POST or None)

    if request.method == 'POST' and forms.is_valid():
        forms.save()
        messages.success(request, 'El aprendiz fue creado correctamente.')
        return redirect('listar')

    return render(request, 'clases/crear_aprendiz.html', {'forms': forms})


def editar_aprendiz(request, documento):
    aprendiz_editar = get_object_or_404(aprendiz, documento=documento)

    form = aprendizform(request.POST or None, instance=aprendiz_editar)
    form.fields['documento'].disabled = True

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Usted editó de manera correcta.')
        return redirect('listar')

    return render(request, 'clases/crear_aprendiz.html', {
        'forms': form,
        'titulo': f'Editar {aprendiz_editar.nombre} - {aprendiz_editar.apellido}'
    })




def eliminar(request,documento):
    aprendiz_eliminar  = get_object_or_404(aprendiz, documento=documento)
    if request.method == 'POST':
        aprendiz_eliminar.delete()


        messages.success(request, 'Usted elimino de manera correcta.')
        return redirect('listar')
       
       
    
    return render(request, 'clases/crear_aprendiz.html', {'aprendiz_eliminar':aprendiz })



def buscar_aprendiz(request):

    resultado = None

    if request.method == 'POST':

        documento = request.POST.get('documento', '').strip()

        resultado = aprendiz.objects.filter(
            documento=documento
        ).first()

        if resultado is None:
            messages.error(
                request,
                f'No se encontró ningún aprendiz con el documento {documento}'
            )

    return render(
        request,
        'clases/buscar.html',
        {'aprendiz': resultado}
    )