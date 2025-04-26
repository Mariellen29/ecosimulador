class Simulador:
    def simular_reducao(self, usuario, calculadora, meses=12):
        print(f"\n=== Simulação de Redução para {usuario.nome} ({meses} meses) ===")
        
        agua_inicial = calculadora.calcular_agua_mensal(usuario)
        co2_inicial = calculadora.calcular_co2_mensal(usuario)
        
        # Simula redução de 10% a cada mês
        for mes in range(1, meses + 1):
            usuario.consumo_agua *= 0.9  # Reduz 10% ao mês
            usuario.consumo_energia *= 0.9
            
            agua_atual = calculadora.calcular_agua_mensal(usuario)
            co2_atual = calculadora.calcular_co2_mensal(usuario)
            
            print(f"Mês {mes}: Água = {agua_atual:.1f}L (-{((agua_inicial - agua_atual)/agua_inicial)*100:.1f}%) | CO2 = {co2_atual:.1f}kg")