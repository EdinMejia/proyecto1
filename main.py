def calcular_vuelto(precio, cantidad_recibida):
# Calcula el vuelto restando el precio del producto del dinero recibido
 vuelto = cantidad_recibida - precio
 return vuelto

def desglosar_cambio(vuelto): 
  # Lista de los diferentes tipos de billetes y monedas disponibles en el pais 
  billetes = [200, 100, 50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.05]
  desglose = {} # Para almacenar la cantidad de cada billete o moneda en el vuelto

   # Itera sobre cada billete o moneda para determinar su cantidad en el vuelto
  for billete in billetes:
     # Calcula la cantidad de billetes o monedas necesarios para el vuelto
      cantidad = int(vuelto // billete)
      if cantidad > 0:
         # Si la cantidad es mayor que cero, agrega el billete o moneda al desglose
           desglose[billete] = cantidad
         # Actualiza el valor del vuelto restante después de considerar un billete o moneda
      vuelto %= billete

  return desglose

def main():
  print("\nBIENVENIDO A LA CALCULADORA DE CAMBIO")
  precio = float(input("\nIngrese el precio del producto: "))
  cantidad_recibida = float(input("\nIngrese la cantidad recibida: "))
  # Calcular el vuelto llamando a la función calcular_vuelto
  vuelto = calcular_vuelto(precio, cantidad_recibida)
  # Mostrar el vuelto calculado
  print(f"\n Cambio por devolver: Q{vuelto:.2f}")
  # Desglosar el vuelto en diferentes denominaciones de billetes y monedas
  desglose = desglosar_cambio(vuelto)
  print("\n deglose del vuelto:")
  # Mostrar el desglose del vuelto
  for billete, cantidad in desglose.items():
    print(f"Q{billete:}: {cantidad}")


if __name__ == "__main__":
  # Esta condición verifica si el programa se está ejecutando como el programa principal
  # Si es así, se llama a la función main() para iniciar el programa.
  main()