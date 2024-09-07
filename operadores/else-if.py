valor_usd_informal = 330
ingreso_mensual_usd = 1000
gasto_mensual_usd = 3000
ingreso_mensual_cup = ingreso_mensual_usd * valor_usd_informal
gasto_mensual_cup = gasto_mensual_usd * valor_usd_informal
ahorro_mensual = ingreso_mensual_usd - gasto_mensual_usd

if ingreso_mensual_usd > 4000:
    print("Eres millonario en Cuba")
    print(f"Estas ganando {ingreso_mensual_cup} cup actualmente")
    if ingreso_mensual_usd > gasto_mensual_usd:
        print("No haz gastado mas de lo que ingresas")
        print(f"Felicidades haz logrado ahorrar {ahorro_mensual} este mes")
    elif ingreso_mensual_usd == gasto_mensual_usd:
        print("Estas totalmente en cero, te gastaste todos tus ingresos")
elif ingreso_mensual_usd <= 4000:
    print("No llegas a la categoria millonario")        
        