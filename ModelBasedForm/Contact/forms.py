from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        # fields = "__all__" # ME MUESTRA TODOS LOS CAMPOS DECLARADOS EN EL MODEL, EN EL ORDEN EN QUE LOS DECLARÉ EN EL MODELO
        fields = ['name', 'email', 'message', 'contact_type', 'subscription'] # EL FORM SOLO ME MOSTRARÁ LOS CAMPOS DEL MODELO QUE INDICO AQUÍ, Y EN EL ORDEN EN QUE LOS INDICO EN LA LISTA
