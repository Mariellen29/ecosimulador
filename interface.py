import tkinter as tk
from tkinter import messagebox
import json
import matplotlib.pyplot as plt # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type: ignore
from estrutura import Usuario, CalculadoraImpacto, DicasSustentabilidade

class EcoSimuladorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EcoSimulador")
        
        # Frame de entrada de dados
        self.frame_entrada = tk.Frame(root, padx=10, pady=10)
        self.frame_entrada.pack()
        
        # Campos do usuário
        tk.Label(self.frame_entrada, text="Nome:").grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.frame_entrada)
        self.entry_nome.grid(row=0, column=1)
        
        tk.Label(self.frame_entrada, text="Região:").grid(row=1, column=0)
        self.entry_regiao = tk.Entry(self.frame_entrada)
        self.entry_regiao.grid(row=1, column=1)
        
        tk.Label(self.frame_entrada, text="Água (L/dia):").grid(row=2, column=0)
        self.entry_agua = tk.Entry(self.frame_entrada)
        self.entry_agua.grid(row=2, column=1)
        
        tk.Label(self.frame_entrada, text="Energia (kWh/mês):").grid(row=3, column=0)
        self.entry_energia = tk.Entry(self.frame_entrada)
        self.entry_energia.grid(row=3, column=1)
        
        tk.Label(self.frame_entrada, text="Lixo (kg/semana):").grid(row=4, column=0)
        self.entry_lixo = tk.Entry(self.frame_entrada)
        self.entry_lixo.grid(row=4, column=1)
        
        # Botões
        self.btn_calcular = tk.Button(root, text="Calcular Impacto", command=self.calcular_impacto)
        self.btn_calcular.pack(pady=5)
        
        self.btn_simular = tk.Button(root, text="Simular Redução", command=self.simular_reducao)
        self.btn_simular.pack(pady=5)
        
        self.btn_salvar = tk.Button(root, text="Salvar Dados", command=self.salvar_dados)
        self.btn_salvar.pack(pady=5)
        
        # Área de resultados
        self.frame_resultados = tk.Frame(root, padx=10, pady=10)
        self.frame_resultados.pack()
        
        self.label_resultados = tk.Label(self.frame_resultados, text="", justify=tk.LEFT)
        self.label_resultados.pack()
    
    def calcular_impacto(self):
        try:
            usuario = Usuario(
                self.entry_nome.get(),
                self.entry_regiao.get()
            )
            usuario.atualizar_habito(
                float(self.entry_agua.get()),
                float(self.entry_energia.get()),
                float(self.entry_lixo.get())
            )
            
            calculadora = CalculadoraImpacto()
            dicas = DicasSustentabilidade()
            
            resultado = f"""
            {usuario.nome}, seu impacto mensal é:
            - Água: {calculadora.calcular_agua_mensal(usuario):.1f} litros
            - CO2: {calculadora.calcular_co2_mensal(usuario):.1f} kg
            - Lixo: {calculadora.calcular_lixo_mensal(usuario):.1f} kg
            
            Dicas sustentáveis:
            """
            for dica in dicas.gerar_dicas(usuario, calculadora):
                resultado += f"\n{dica}"
            
            self.label_resultados.config(text=resultado)
            
        except ValueError:
            messagebox.showerror("Erro", "Preencha todos os campos com números válidos!")
    
    def simular_reducao(self):
        try:
            usuario = Usuario(
                self.entry_nome.get(),
                self.entry_regiao.get()
            )
            usuario.atualizar_habito(
                float(self.entry_agua.get()),
                float(self.entry_energia.get()),
                float(self.entry_lixo.get())
            )
            
            calculadora = CalculadoraImpacto()
            simulador = Simulador()
            
            # Criar uma nova janela para a simulação
            janela_simulacao = tk.Toplevel(self.root)
            janela_simulacao.title("Simulação de Redução")
            
            fig, ax = plt.subplots(figsize=(8, 4))
            simulador.simular_com_grafico(usuario, calculadora, ax, meses=6)
            
            canvas = FigureCanvasTkAgg(fig, master=janela_simulacao)
            canvas.draw()
            canvas.get_tk_widget().pack()
            
        except ValueError:
            messagebox.showerror("Erro", "Preencha todos os campos com números válidos!")
    
    def salvar_dados(self):
        try:
            dados = {
                "nome": self.entry_nome.get(),
                "regiao": self.entry_regiao.get(),
                "agua": float(self.entry_agua.get()),
                "energia": float(self.entry_energia.get()),
                "lixo": float(self.entry_lixo.get())
            }
            
            with open("dados_usuario.json", "w") as arquivo:
                json.dump(dados, arquivo)
            
            messagebox.showinfo("Sucesso", "Dados salvos em 'dados_usuario.json'!")
        except ValueError:
            messagebox.showerror("Erro", "Dados inválidos para salvar!")

# Adicionando o método de simulação com gráfico à classe Simulador
class Simulador:
    def simular_com_grafico(self, usuario, calculadora, ax, meses=12):
        agua_mensal = []
        co2_mensal = []
        
        agua_inicial = calculadora.calcular_agua_mensal(usuario)
        co2_inicial = calculadora.calcular_co2_mensal(usuario)
        
        for mes in range(meses):
            usuario.consumo_agua *= 0.9
            usuario.consumo_energia *= 0.9
            
            agua_mensal.append(calculadora.calcular_agua_mensal(usuario))
            co2_mensal.append(calculadora.calcular_co2_mensal(usuario))
        
        ax.plot(range(meses), agua_mensal, label="Água (L)")
        ax.plot(range(meses), co2_mensal, label="CO2 (kg)")
        ax.set_xlabel("Meses")
        ax.set_ylabel("Consumo")
        ax.set_title("Redução do Impacto Ambiental")
        ax.legend()
        ax.grid()

# Classes anteriores (Usuario, CalculadoraImpacto, DicasSustentabilidade) permanecem iguais

# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = EcoSimuladorApp(root)
    root.mainloop()