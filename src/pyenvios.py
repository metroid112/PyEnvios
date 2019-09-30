import os

valid_units = ('kg', 'oz', 'lb', 'g')


def shipping_price(items):
    price = 0
    for item in items:
        price += item.price
    return price


def return_price(item):
    return item.price


def optimize_shipping(items):
    items.sort(key=return_price, reverse=True)
    remaining_price = 200
    shipping = 1
    optimized_shipping = [[shipping, remaining_price, []]]
    for item in items:
        add_to_shipping = 0
        for shipment in optimized_shipping:
            if shipment[1] >= item.price:
                add_to_shipping = shipment[0]
        if add_to_shipping == 0:
            shipping += 1
            optimized_shipping.append([shipping, 200, []])
            add_to_shipping = shipping
        optimized_shipping[add_to_shipping - 1][2].append(item)
        optimized_shipping[add_to_shipping - 1][1] -= item.price
    return optimized_shipping


class Item:
    def __init__(self, description, price, weight, unit):
        self.description = description
        self.price = price
        self.weight = weight
        self.unit = unit

    def __repr__(self):
        return f'{self.description} - ${self.price} - {self.weight}{self.unit}'


def main():
    os.system('cls')
    salir = False
    items = [Item('A', 200, 1, 'kg'), Item('B', 20, 1, 'kg'), Item('C', 100, 1, 'kg'), Item('D', 50, 1, 'kg'), Item('E', 170, 1, 'kg'), Item('F', 30, 1, 'kg'), Item('G', 20, 1, 'kg')]
    while not salir:
        if items:
            print('Items:')
            for item in items:
                print(item)
        print('Ingrese opción:')
        print('[1] Ingresar nuevo item')
        print('[2] Calcular envíos')
        print('[3] Salir')
        option = input('Opción: ')
        if option == '1':
            item_created = False
            item_description = ''
            item_unit = ''
            item_weight = 0
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
                        if item_unit != '':
                            print(f'Unidad: {item_unit}')
                        else:
                            print(f'Unidades: {valid_units}')
                            item_unit = input('Ingrese unidad: ')
                            if item_unit not in valid_units:
                                print('Ingrese una unidad válida!')
                            else:
                                if item_weight != 0:
                                    print(f'Peso: {item_weight}{item_unit}')
                                else:
                                    try:
                                        item_weight = float(input('Ingrese peso: '))
                                        item = Item(item_description, item_price, item_weight, item_unit)
                                        items.append(item)
                                        item_created = True
                                        os.system('cls')
                                    except ValueError:
                                        print('Error en conversion, porfavor ingrese nuevamente')
                except ValueError:
                    print('Error en conversion, porfavor ingrese nuevamente')
        elif option == '2':
            os.system('cls')
            if items:
                shipments = optimize_shipping(items)
                for shipment in shipments:
                    weight = 0.00
                    weight_price = 0.00
                    print(f'Shipping {shipment[0]}')
                    for item in shipment[2]:
                        if item.unit == 'kg':
                            weight += item.weight
                        elif item.unit == 'g':
                            weight += item.weight / 1000
                        elif item.unit == 'oz':
                            weight += item.weight / 35.274
                        elif item.unit == 'lb':
                            weight += item.weight / 2.205
                        if weight <= 0.5:
                            weight_price = 12
                        else:
                            weight_price = 12 + (3.5 * ((weight - 0.5) / 0.5))
                        print(item)
                    print(f'Total: ${200 - shipment[1]}, {weight}kg (${weight_price}) - Total ${200 - shipment[1] + weight_price}')
                    print('---------------')
            else:
                print('No se cargó ningun item.')
        elif option == '3':
            os.system('cls')
            exit()
        else:
            os.system('cls')
            print('Opción no válida\n')


main()
