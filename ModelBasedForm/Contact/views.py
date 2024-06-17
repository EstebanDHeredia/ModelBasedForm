from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        # SI ME ESTAN ENVIANDO (POST) LOS DATOS DEL FORMULARIO PARA GUARDARLOS:
        # LLENO LA variable DEL FORM CON LOS DATOS QUE ME ENVIAN
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid(): # Pregunto si el formulario es válido, es decir los datos están ok
            # si es así guardo el form y envío una respuesta indicando que estuvo todo ok
            try:
                contact_form.save()
                return redirect(reverse('contact')+'?ok')
            
            except: #Hubo un problema al almacenar el form
                
                return redirect(reverse('contact')+'?error')
        else: # El form no es válido
            return redirect(reverse('contact')+'?error')
                
                
    return render(request, 'contact/contact.html', {'form': contact_form})
