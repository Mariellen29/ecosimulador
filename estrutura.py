class Usuario:
    def __init__(self, nome, regiao):
        self.nome = nome
        self.regiao = regiao
        self.consumo_agua = 0  # litros/dia
        self.consumo_energia = 0  # kWh/mês
        self.lixo_produzido = 0  # kg/semana
    
    def atualizar_habito(self, agua, energia, lixo):
        self.consumo_agua = agua
        self.consumo_energia = energia
        self.lixo_produzido = lixo

    

class CalculadoraImpacto:
   
    def calcular_agua_mensal(self, usuario):
        return usuario.consumo_agua * 30  # litros/mês

    def calcular_co2_mensal(self, usuario):
        # Fórmula simplificada: kWh * fator de emissão regional
        return usuario.consumo_energia * 0.5  # kg CO2/mês

    def calcular_lixo_mensal(self, usuario):
        return usuario.lixo_produzido * 4  # kg/mês (considerando 4 semanas)

class DicasSustentabilidade:
    def gerar_dica_agua(self, usuario):
        if usuario.consumo_agua > 100:
            return f"{usuario.nome}, você pode economizar 20% de água reduzindo o tempo no banho!"
        else:
            return "Seu consumo de água está dentro da média sustentável!"
        
    def gerar_dicas(self, usuario, calculadora):
        dicas = []
        
        # Dicas para água
        agua_mensal = calculadora.calcular_agua_mensal(usuario)
        if agua_mensal > 3000:  # Se gastar mais de 3 toneladas/mês
            dicas.append("💧 Reduza seu tempo no banho! Cada minuto a menos economiza 6 litros.")
        
        # Dicas para energia
        co2_mensal = calculadora.calcular_co2_mensal(usuario)
        if co2_mensal > 100:  # Se emitir mais de 100kg CO2/mês
            dicas.append("⚡ Desligue aparelhos em standby e troque lâmpadas por LED.")
        
        # Dicas para lixo
        lixo_mensal = calculadora.calcular_lixo_mensal(usuario)
        if lixo_mensal > 20:  # Se produzir mais de 20kg de lixo/mês
            dicas.append("🗑️ Separe o lixo reciclável e composte resíduos orgânicos.")
        
        return dicas if dicas else ["✅ Seus hábitos estão dentro da média sustentável!"]

# Exemplo de uso:
usuario1 = Usuario("João", "Sudeste")
usuario1.consumo_agua = 150
calculadora = CalculadoraImpacto()
dicas = DicasSustentabilidade()

print(f"Consumo mensal de água: {calculadora.calcular_agua_mensal(usuario1)} litros")
print(dicas.gerar_dica_agua(usuario1))