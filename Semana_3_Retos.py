from fractions import Fraction
import fractions
def simulador_financiacion_yo_le_fio(datos_venta: dict) -> dict:

      Valor_Venta = datos_venta["venta"]
      Valor_Cuota_Inicial = datos_venta["cuotainicial"]
      Numero_Cuotas = datos_venta["cuotas"]
      Porcentaje_Interes_Anual = datos_venta["interesAnual"]
      '''
      Porcentaje_Interes_Anual = %EA
      TMV=(1+%EA)^(1/12)-1
      '''
      EA = Porcentaje_Interes_Anual/100
      TMV = ((1+EA)**(1/12))-1 #Tasa de interes mes vencido

      '''
                        Saldo_Financiado
      Cuota=--------------------------------------------
                       1-(1+TMV)^-Nomeses
                    ---------------------  (Denominador)
                               TMV
      '''
      Saldo_Financiado = Valor_Venta-Valor_Cuota_Inicial

      variable = (1-(1+TMV)**-Numero_Cuotas)

      Denominador =variable/TMV #Fraction(variable,TMV)
      
      Valor_Cuota_Mensual = round((Saldo_Financiado/Denominador),2)
      
      #amortización de la deuda 
      i=1
      
      amortizacion2=[]
      Valor_Interes = round ((Saldo_Financiado*TMV),2)
      Capital_Abonado =round ((Valor_Cuota_Mensual-Valor_Interes),2)
      Nuevo_Saldo = round ((Saldo_Financiado - Capital_Abonado),2)
      while i <= Numero_Cuotas:

          tupla = i,Capital_Abonado,Valor_Interes,Valor_Cuota_Mensual,Nuevo_Saldo
          amortizacion2.append((tupla))
          Valor_Interes = round ((Nuevo_Saldo*TMV),2)
          Capital_Abonado = round ((Valor_Cuota_Mensual-Valor_Interes),2)
          Nuevo_Saldo =round ((Nuevo_Saldo - Capital_Abonado),2)

          i+=1
          
          
          
      return{"saldo financiar":Saldo_Financiado,"cuota":round(Valor_Cuota_Mensual,0),"amortizacion":amortizacion2}
      



datos = {
    "venta":2000000,
    "cuotainicial":0,
    "cuotas":6,
    "interesAnual":28.99,
    "saldo financiar":0.0,
    "cuota":0.0,
}


simulador_financiacion_yo_le_fio(datos)
print(simulador_financiacion_yo_le_fio(datos))