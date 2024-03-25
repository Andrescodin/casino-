#%%
#buenbuena
def casino(tiradas, ruletas):
    from random import randint
    rojo = 1
    negro = 2
    beneficios_ruleta = [0] * ruletas
    presupuesto = [80] * ruletas
    cantidad_apostada = [1] * ruletas
    porcentaje_de_rojos = [0] * ruletas
    porcentaje_de_negros = [0] * ruletas
    total = [0] * ruletas
     # Valor máximo en cada fila
      
    ntiradas_rule=crear_matriz_numeros(ruletas, tiradas)
    btirada = crear_matriz_ceros(ruletas, tiradas)
    for j in range(tiradas):
        for i in range(ruletas):
            if cantidad_apostada[i] <= presupuesto[i]:  # Verificar si la cantidad apostada es menor o igual al presupuesto
                rd = randint(1, 2)
                if rd == 1:
                    beneficios_ruleta[i] += cantidad_apostada[i]
                    presupuesto[i] += cantidad_apostada[i]
                    cantidad_apostada[i] = 1
                    porcentaje_de_rojos[i] += 1
                    total[i] += 1
                else:
                    beneficios_ruleta[i] -= cantidad_apostada[i]
                    presupuesto[i] -= cantidad_apostada[i]
                    cantidad_apostada[i] *= 1.5
                    porcentaje_de_negros[i] += 1
                    total[i] += 1
                btirada[i][j] =beneficios_ruleta[i]
    
    crear_graficos(ntiradas_rule,btirada)
    rule=[]
    for i in range(ruletas):
        print(f"nruleta:{i+1}, %negros:{round((porcentaje_de_negros[i]/total[i])*100)},%rojos:{round((porcentaje_de_rojos[i]/total[i])*100)}, tiradas:{total[i]}, presu:{round(presupuesto[i])}, beneficio:{round(beneficios_ruleta[i])}")
        rule.append(i)
    sumabeneficios=0
    ben_en_base=[]
    for td in beneficios_ruleta:
        sumabeneficios=sumabeneficios+td
        ben_en_base.append(sumabeneficios)
    import matplotlib.pyplot as plt
    plt.plot(rule, ben_en_base)
    # Agregar etiquetas y título
    plt.xlabel('numero de ruletas')
    plt.ylabel('beneficio')
    plt.title('Gráfico en base a ruletas')
    plt.show()
"""
    # Mostrar el gráfico
   
    "cont=0
    tirar=0
    ft=0
    for i in beneficios_ruleta:
        max_valor = max(beneficios_ruleta)
        pos_max_valor = i
        tirar+=pos_max_valor
        cont+=1
        ft+=max_valor
    tirad_avg_para_pasta=tirar/cont"
    bmedio=max_valor/tirar
    
    print(f"tiradas recomendadas:{tirad_avg_para_pasta},beneficio medio {bmedio}")
       
    
   print(tirad_avg_para_pasta)
   """
# Ejemplo de uso
casino(800, 15)    


    
#%%
#fun aux 1
def crear_matriz_ceros(n, m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(0)
        matriz.append(fila)
    return matriz

#%%
#funcion auxiliar2
def crear_matriz_numeros(n, m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(1, m + 1):  # Empezamos desde 1
            fila.append(j)
        matriz.append(fila)
    return matriz


#%%
#gfunaux3


def crear_graficos(x, y):
    import matplotlib.pyplot as plt
    num_graficos = min(len(x), len(y))

    for i in range(num_graficos):
        grafico_x = x[i]
        grafico_y = y[i]
        plt.figure("Ruleta" + str(i+1))
        plt.plot(grafico_x, grafico_y)
        plt.xlabel('numero de tirada')
        plt.ylabel('Beneficio')
        plt.title('Grafico ' + str(i+1))
        plt.grid(True)

    plt.show()
    
