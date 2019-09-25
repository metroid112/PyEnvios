import os


def shipping_price(items):
    price = 0
    for item in items:
        price += item.price
    return price


def return_price(item):
    return item.price


def optimize_shipping(items):
    items.sort(key=return_price, reverse=True)
    optimized_shipping = []
    remaining_price = 200
    shipments = 1
    for item in items:
        x = 2
    return optimized_shipping


class Item:
    def __init__(self, description, price):
        self.description = description
        self.price = price

    def __repr__(self):
        return f'{self.description} - ${self.price}'


def main():
    salir = False
    items = []
    while not salir:
        for item in items:
            print(item)
            print('---------------')
        print('Ingrese opción:')
        print('[1] Ingresar nuevo item')
        print('[2] Calcular envíos')
        print('[3] Salir')
        option = input('Opción: ')
        if option == '1':
            item_created = False
            item_description = ''
            while not item_created:
                os.system('cls')
                if item_description != '':
                    print(f'Descripción: {item_description}')
                else:
                    item_description = input('Ingrese descripción: ')
                try:
                    item_price = float(input('Ingrese precio: '))
                    if item_price > 200:
                        print('El item no puede superar el valor de 200!')
                    else:
                        item = Item(item_description, item_price)
                        items.append(item)
                        item_created = True
                        os.system('cls')
                except ValueError:
                    print('Error en conversion, porfavor ingrese nuevamente')
        elif option == '2':
            if items:
                shipments = optimize_shipping(items)
                for shipment in shipments:
                    print(f'Shipping {shipment[0]}')
                    for item in shipment[1]:
                        print(item)
            else:
                print('No se cargó ningun item.')
        elif option == '3':
            exit()
        else:
            os.system('cls')
            print('Opción no válida')
            print()


main()
