from calculo import Calculo

def main():
    print(
        """
        projeto com finalidade de demonstrar o valor gasto com combustivel de um veiculo
        """
        )
    
    print("os combustiveis disponiveis são: ")
    print("\t° alcool")
    print("\t° diesel" )
    print("\t° gasolina")
    
    print(" ")
    
    try:
        distancia = float(input("distancia em quilometros: "))
        consumo = float(input("consumo de combustivel por veiculo: "))
        calculo = Calculo()
        print(
            calculo.calcular_gasto(distancia, consumo)
        )
    except ValueError as erro:
        print(" o valor recebido não é valido")
        
        
if __name__ == "__main__":
    main()