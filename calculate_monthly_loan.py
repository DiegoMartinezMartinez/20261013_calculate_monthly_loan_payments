# Obtener capital
capital = int(input("Introduce capital en euros: "))

# Tipo de interes
EURIBOR = 3.354
SALARIO_FISICO = 34750
interes = EURIBOR + 1

# Obtener numero de cuotas
numero_años = int(input("¿En cuantos años lo quieres pagar?: "))
numero_cuotas = numero_años * 12
interes_mensual = interes / 12 / 100

# Calcular cuota mensual
cuota_mensual = capital * (interes_mensual * (1 + interes_mensual)**numero_cuotas) / ((1 + interes_mensual)**numero_cuotas - 1)
cuota_mensual = round(cuota_mensual, 2)

# Calcular salario necesario
# La cuota supone como maximo el 25% del sueldo neto
salario_neto_mensual_minimo = cuota_mensual * 4
salario_neto_anual_minimo = salario_neto_mensual_minimo * 12

# Calcular salario bruto aproximado
salario_anual_bruto = salario_neto_anual_minimo / 0.75
salario_anual_bruto = round(salario_anual_bruto, 2)

print(f"La cuota mensual es {cuota_mensual} €")
print(f"Para pagar esta casa de {capital} € necesitas cobrar {salario_anual_bruto} € brutos anuales")
print(f"Un fisico en España gana de media {SALARIO_FISICO} € brutos al año")