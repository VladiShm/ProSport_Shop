from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect

from ProSport.forms import OrderForm
from ProSport.models import Items


def index(request):
    products = Items.objects.all()
    form = OrderForm()
    context = {
        'products': products,
        'form': form,
    }
    return render(request, 'Backend/main_page.html', context)


def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            house = form.cleaned_data['house']
            apartment = form.cleaned_data['apartment']
            delivery_method = form.cleaned_data['delivery_method']
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            total_price = product.price * quantity
            products = Items.objects.all()

            print(f'Имя: {first_name}')
            print(f'Фамилия: {last_name}')
            print(f'Email: {email}')
            print(f'Город: {city}')
            print(f'Улица: {street}')
            print(f'Дом: {house}')
            print(f'Квартира: {apartment}')
            print(f'Способ доставки: {delivery_method}')
            print(f'Товар: {product}')
            print(f'Количество: {quantity}')
            print(f'Итоговая стоимость: {total_price}')
            # Формирование сообщения
            message = f"""
            Ваш заказ успешно оформлен!
            Имя: {first_name}
            Фамилия: {last_name}
            Email: {email}
            Город: {city}
            Улица: {street}
            Дом: {house}
            Квартира: {apartment}
            Способ доставки: {delivery_method}
            Товар: {product}
            Количество: {quantity}
            Итоговая стоимость: {total_price}
            """
            # Отправка email
            email_message = EmailMessage(
                'Новый заказ',
                message,
                'prosport1337@mail.ru',  # Здесь укажите ваш email
                [email],  # Email клиента
            )
            email_message.send()
            context = {
                'products': products,
                'form': form,
            }
        else:
            print("Форма не прошла валидацию. Ошибки формы:", form.errors)
    else:
        form = OrderForm()

    return render(request, 'Backend/main_page.html', context)
