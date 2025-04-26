from estrutura import Usuario, CalculadoraImpacto, DicasSustentabilidade
from simulador import Simulador
if __name__ == "__main__":
    # Cria usuário
    usuario = Usuario("Maria", "Sudeste")
    usuario.atualizar_habito(agua=100, energia=200, lixo=5)  # 100L/dia, 200kWh/mês, 5kg/semana

    # Inicializa classes
    calculadora = CalculadoraImpacto()
    dicas = DicasSustentabilidade()
    simulador = Simulador()

    # Calcula impacto
    print(f"{usuario.nome}, seu consumo mensal é:")
    print(f"- Água: {calculadora.calcular_agua_mensal(usuario)} litros")
    print(f"- CO2: {calculadora.calcular_co2_mensal(usuario)} kg")
    print(f"- Lixo: {calculadora.calcular_lixo_mensal(usuario)} kg")

    # Mostra dicas
    print("\nDicas sustentáveis:")
    for dica in dicas.gerar_dicas(usuario, calculadora):
        print(dica)

    # Simula redução
    simulador.simular_reducao(usuario, calculadora, meses=6)