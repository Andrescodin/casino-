# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:34:25 2024

@author: andre
"""

def casino(tiradas, ruletas):
    rojo = 1
    negro = 2
    beneficios_ruleta = [0] * ruletas
    presupuesto = [80] * ruletas
    cantidad_apostada = [1] * ruletas
    porcentaje_de_colores_por_ruleta = [0] * ruletas
    ruletas = list(range(1, ruletas + 1))

    
    