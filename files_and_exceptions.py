ventas_agrupadas = {}

    try:
        with open(filename, 'r') as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue

                partes_venta = linea_limpia.split(';')

                for parte in partes_venta:
                    if not parte:
                        continue
                    
                    datos_producto_valor = parte.split(':')

                    if len(datos_producto_valor) == 2:
                        producto = datos_producto_valor[0].strip()
                        valor_str = datos_producto_valor[1].strip()

                        try:
                            valor_de_venta = float(valor_str)
                            if producto not in ventas_agrupadas:
                                ventas_agrupadas[producto] = []
                            ventas_agrupadas[producto].append(valor_de_venta)
                        except ValueError:
                            pass
                    else:
                        pass

    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{filename}' no fue encontrado.")
    except Exception as e:
        raise Exception(f"Ocurrió un error inesperado: {e}")

    return ventas_agrupadas

def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    pass
