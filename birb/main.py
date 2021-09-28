from birb import *

grafico_linha_simples([3, 4, 8, 9], [10, 20, 30, 40])
lista1 = [7, 5, 10]
lista2 = ["Setembro", "Outubro", "Novembro"]
grafico_linha_simples(lista2, lista1, limites=[], nome_do_grafico="Gráfico Teste",
                      cor="amarelo", estilo_marcador="diamante", estilo_linha="pontilhada",
                      definir_nomes_eixos=True, eixox="Meses", eixoy="Notas", definir_plano_de_fundo=True,
                      cor_de_fundo="azul", definir_limites=True, salvar_arquivo=True)

# IMPORTANTE! -> barras e histograma ainda não usam conversão de cor, inserir em notação original

lista3 = [30, 45, 60, 70]
lista4 = [45, 60, 75, 85]
lista5 = ['coluna 1', 'coluna 2', 'coluna 3', 'coluna 4']
grafico_barras(lista3, lista4)

lista6 = [1, 2, 3, 4, 5]
lista7 = [100, 350, 68, 245, 150]
lista8 = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
grafico_barras(lista6, lista7, True, lista8, cor=["red", "blue"], largura_barras=0.9, definir_eixos=True,
               eixox="Dinheiro Ganho", eixoy="Meses", nome_do_grafico="Meus Rendimentos", definir_plano_de_fundo=True,
               cor_de_fundo="amarelo")

lista9 = [10, 14, 23, 67, 50, 44]
tamanho = (0, 50)
grafico_histograma(lista9, tamanho)

lista10 = [3, 4.5, 5.8, 6, 6.5, 7, 7.4, 8.3, 8.6, 9, 9.1, 9.7, 10]
tamanho = (0, 10)
espacos = 15
cor = ['magenta']
grafico_histograma(lista10, tamanho, espacos, orientacao="horizontal", cor=cor, eixox="Notas", eixoy="Frequência",
                   nome_do_grafico="Rendimento Turma", definir_plano_de_fundo=True, cor_de_fundo="ciano")

lista11 = ['esporte', 'jogar', 'estudar', 'dormir', 'comer']
lista12 = [3, 2, 7, 8, 6]
lista13 = ['verde', 'roxo', 'amarelo', 'azul', 'vermelho']
grafico_pizza(lista11, lista12, lista13)

lista14 = ['Programação', 'Design', 'Projeto', 'Analise', 'Testes', 'Requisitos']
lista15 = [9, 6, 8, 7, 9, 8]
lista16 = ['azul', 'roxo', 'ciano', 'verde', 'amarelo', 'vermelho']
grafico_pizza(lista14, lista15, lista16, mostrar_legenda=False, nome_do_grafico="Processo",
              definir_plano_de_fundo=True, cor_de_fundo="branco")
