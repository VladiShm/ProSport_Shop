from django import forms
from .models import Items

class OrderForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_box', 'placeholder': 'Имя'}),
        label=''
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_box', 'placeholder': 'Фамилия'}),
        label=''
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'input_box', 'placeholder': 'Email'}),
        label=''
    )
    city = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_box', 'placeholder': 'Город'}),
        label=''
    )
    street = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_box', 'placeholder': 'Улица'}),
        label=''
    )
    house = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_box', 'placeholder': 'Дом'}),
        label=''
    )
    apartment = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input_box', 'placeholder': 'Квартира'}),
        label=''
    )
    delivery_method = forms.ChoiceField(
        choices=[
            ('post', 'Почта России'),
            ('courier', 'Курьер'),
            ('pickup', 'Пункт выдачи')
        ],
        required=True,
        widget=forms.Select(attrs={'name': 'list1'}),
        label=''
    )
    product = forms.ModelChoiceField(
        queryset=Items.objects.all(),
        required=True,
        widget=forms.Select(attrs={'id': 'product-select', 'name': 'list2'}),
        label=''
    )
    quantity = forms.IntegerField(
        min_value=1,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'input_box', 'placeholder': 'Количество'}),
        label=''
    )