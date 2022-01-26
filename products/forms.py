from django.db.models.fields import BooleanField
from django.forms.widgets import Select, TextInput, Textarea
from products.models import Brands, Category, Order, Product, Service
from django import forms
from django.forms import ModelForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'title', 'category', 'price',
                           'description', 'brand', 'is_published']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),

            'category': forms.Select(attrs={'class': 'form-control'}),

            'brand': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-control'}),

        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BrandsForm(forms.ModelForm):
    class Meta:
        model = Brands
        fields = ['name']
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Creating order forms


class orderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class serviceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'location', 'number',
                  'description', 'fee']


class constForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'location', 'specification_service', 'size', 'number', 'time',
                  'fee']


class plumbForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'location',
                  'description', 'time', 'fee']


class cleanForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'location',
                  'description', 'time', 'number', 'fee']
