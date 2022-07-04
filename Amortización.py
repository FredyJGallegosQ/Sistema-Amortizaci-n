import numpy_financial as npf
import tabulate as tab

def Menu():
  print("**************SISTEMA DE AMORTIZACIÓN**************")
  print("***************************************************")
  print("1. Generar tabla de amortización")
  print("2. Salir")
  op = int(input("Ingrese opción --> "))
  print(" ")
  if(op == 1):
    Amortizacion()
    Menu()
  if(op == 2):
    print("Gracias por usar nuestro sistema!!!") 
    input()
  if(op != 1 and op != 2):
    print("Error ingreso de opciones")
    print("")
    Menu()

def Amortizacion():
  print("Ingresar datos para generar tabla")
  capital = float(input("Ingrese monto de préstamo --> "))
  tasa = float(input("Ingrese tasa de interes --> "))
  tasa = tasa/100
  plazo = int(input("Ingrese número de periodos --> "))
  cuota = round(npf.pmt(tasa, plazo, -capital, 0), 2)
  datos = []
  saldo = capital
  linea = [0, "", "", "", capital]
  datos.append(linea)
  for i in range(1, plazo+1):
    pago_capital = npf.ppmt(tasa, i, plazo, -capital, 0)
    pago_int = cuota - pago_capital
    saldo -= pago_capital  
    linea = [i, format(pago_capital, '0,.2f'), format(pago_int, '0,.2f'), 
    format(cuota, '0,.2f'), format(saldo, '0,.2f')]
    datos.append(linea)
  print(tab.tabulate(datos, headers=['Periodo', 'Amortización', 
    'Pago Interes', 'Pago Mensual', 'Saldo Capital'], tablefmt='psql'))
  print("")
Menu()