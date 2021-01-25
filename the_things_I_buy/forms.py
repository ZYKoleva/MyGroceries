from django import forms

from the_things_I_buy.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('availability', 'customized_prod',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'section': forms.Select(attrs={
                'class': 'form-control',
            }),
            'brand': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'counter': forms.NumberInput(attrs={
                'class': 'form-control',
            })
        }