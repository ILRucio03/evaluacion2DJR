from django import forms
from persona_app.models import proyecto

class FormProyecto(forms.ModelForm):
    class Meta:
        model = proyecto
        fields = '__all__'