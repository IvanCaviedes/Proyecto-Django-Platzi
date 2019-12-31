from django import forms

class banco(forms.Form):
    Datos = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Digite el numero de clientes'}),max_length=100,label='',required=True)