imovel = str(input("Digite seu tipo de imóvel:\n-> ")) # Entrada do tipo de imóvel do usuário.
consumo = float(input("Digite o consumo mental em metros cúbicos:\n-> ")) # Entrada da quantidade de consumo, em metros cúbicos.

# Opções válidas para a entrada do usuário e suas condições
match imovel:
    case "comercial":
        print ("Tarifa comercial aplicada - consulte o plano corporativo.")
        
    case "apartamento":
        if consumo < 10:
            print ("Consumo econômico - excelente controle de água!")
            
    case "apartamento" | "casa":
        if consumo <= 25:
            print("Consumo moderado - dentro do padrão residencial.")
            
    case _:
        print("Consumo excessivo - adote medidas de economia e verifique vazamentos.") # Caso seja uma opção diferente das outras.
