from django import forms
from .models import productDetails, productPath

class productForm(forms.ModelForm):
    class Meta:
        model = productDetails
        fields ="__all__"
        labels ={
            'Product Name':'Name of Product',
        }
    def __init__(self, *args, **kwargs):
        super(productForm,self).__init__(*args, **kwargs)
        self.fields['category_Id'].empty_label ="Select"
        self.fields['manufacturer_Id'].empty_label ="Select"

class pathForm(forms.ModelForm):
    class Meta:
        model = productPath
        fields="__all__"