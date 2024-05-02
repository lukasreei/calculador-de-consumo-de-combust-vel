class Calculo:
    def __init__(self):
        self.__valor_gasolina = 4.55
        self.__valor_alcool = 3.40
        self.__valor_diesel = 3.50
        
    def calcular_gasto(Self, distancia, consumo):
        if (distancia <= 0 or consumo <= 0):
            raise Exception(
                " não tem como calcular o consumo")
            
        gasto_gasolina = round(
            (distancia / consumo) * Self.__valor_gasolina, 2)
        gasto_alcool = round(
            (distancia / consumo) * Self.__valor_alcool, 2)
        gasto_diesel = round(
            (distancia / consumo) * Self.__valor_diesel, 2)
        return """"
        o valor total gasto será de:
        
        gasolina: R${}
        alcool: R${}
        diesel: R${}
        """.format(
            gasto_gasolina, gasto_alcool, gasto_diesel
        )