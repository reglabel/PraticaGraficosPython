from matplotlib import pyplot as plt


def grafico_linha_simples(valores_x, valores_y, limites=None, definir_limites=False,
                          nome_do_grafico="Gráfico Linha Simples", cor="roxo",
                          estilo_marcador="ponto", estilo_linha="solida", definir_nomes_eixos=True,
                          eixox="Eixo X", eixoy="Eixo Y", definir_plano_de_fundo=False, cor_de_fundo="branco",
                          salvar_arquivo=False):
    """Retorna e exibe um gráfico de linha com um único segmento.

        :param valores_x: Valores do eixo x
        :type valores_x: list
        :param valores_y: valores do eixo y
        :type valores_y: list
        :param limites: Lista com limites inferior de x, superior de x, inferior de y, superior de y, respectivamente. Se não tiver esse formato, essa variável será desconsiderada.
        :type limites: list
        :param definir_limites: Indica personalização dos limites dos eixos do gráfico, valor padrão False
        :type definir_limites: bool
        :param nome_do_grafico: Título do gráfico, valor padrão "Gráfico Linha Simples"
        :type nome_do_grafico: str
        :param cor: Código de cor do segmento de linha, valor padrão "roxo"
        :type cor: str
        :param estilo_marcador: Código de símbolo marcador de pontos do segmento, valor padrão "ponto"
        :type estilo_marcador: str
        :param estilo_linha: Código de estilo do segmento de linha, valor padrão "solida"
        :type estilo_linha: str
        :param definir_nomes_eixos: Indica a nomeação dos segmentos, valor padrão True
        :type definir_nomes_eixos: bool
        :param eixox: Nome do segmento x, valor padrão "Eixo X"
        :type eixox: str
        :param eixoy: Nome do segmento y, valor padrão "EIxo Y"
        :type eixoy: str
        :param definir_plano_de_fundo: Indica alteração da cor padrão de plano de fundo do gráfico, valor padrão False
        :type definir_plano_de_fundo: bool
        :param cor_de_fundo: Cor do plano de fundo do gráfico, valor padrão "branco"
        :type cor_de_fundo: str
        :param salvar_arquivo: Salva o gráfico gerado em PNG de fundo transparente, valor padrão False
        :type salvar_arquivo: bool

        :return: lista Line2D (ver documentação de Matplolib para mais detalhes)
        :rtype: Line2D
    """
    if limites is None:
        limites = []

    estilo_grafico = f"{marcador_converter_notacao_birb_para_matplotlib(estilo_marcador)}" \
                     f"{linha_converter_notacao_birb_para_matplotlib(estilo_linha)}" \
                     f"{cor_converter_notacao_birb_para_matplotlib(cor)}"

    plt.title(nome_do_grafico)
    plt.plot(valores_x, valores_y, estilo_grafico)
    if definir_nomes_eixos:
        plt.xlabel(eixox)
        plt.ylabel(eixoy)
    if definir_limites and len(limites) == 4:
        plt.axis(limites)
    if definir_plano_de_fundo:
        objeto_ax = plt.gca()
        objeto_ax.set_facecolor(cor_converter_notacao_birb_para_matplotlib(cor_de_fundo))
    if salvar_arquivo:
        plt.savefig(f'{nome_do_grafico}.png', transparent=True)
    plt.show()


def grafico_barras(coordenadas_x, alturas, definir_tags_barras=False, tags_barras=None, cor=None, largura_barras=0.9,
                   definir_eixos=True, eixox="Eixo X", eixoy="Eixo Y", nome_do_grafico="Gráfico de Barras",
                   definir_plano_de_fundo=False, cor_de_fundo="branco", salvar_arquivo=False):
    # fazer tabela de conversao de cores
    if cor is None:
        cor = ["blue"]

    if tags_barras is None:
        tags_barras = []
    if len(coordenadas_x) == len(alturas):
        if definir_tags_barras:
            if len(coordenadas_x) != len(tags_barras):
                raise ValueError("Uma ou mais condições de execução da função não foram respeitadas",
                                 "compatibilidade de valores")

        # cores = []
        # for i in cor:
        #    novaCor = cor_converter_notacao_birb_para_matplotlib(i)
        #    cores.append(i)

        if definir_tags_barras:
            plt.bar(coordenadas_x, alturas, tick_label=tags_barras, color=cor, width=largura_barras)
        else:
            plt.bar(coordenadas_x, alturas, color=cor, width=largura_barras)

        plt.title(nome_do_grafico)

        if definir_eixos:
            plt.xlabel(eixox)
            plt.ylabel(eixoy)
        if definir_plano_de_fundo:
            objeto_ax = plt.gca()
            objeto_ax.set_facecolor(cor_converter_notacao_birb_para_matplotlib(cor_de_fundo))
        if salvar_arquivo:
            plt.savefig(f"{nome_do_grafico}.png")

        plt.show()
    else:
        raise ValueError("Uma ou mais condições de execução da função não foram respeitadas",
                         "compatibilidade de valores")


def grafico_histograma(frequencias, tamanho_x, espacos=10, orientacao="vertical",
                       cor=None, largura_segmentos=0.9, definir_eixos=True, eixox="Eixo X", eixoy="Eixo Y",
                       nome_do_grafico="Gráfico Histograma", definir_plano_de_fundo=False, cor_de_fundo="branco",
                       salvar_arquivo=False):
    # fazer tabela de conversao de cores
    if cor is None:
        cor = ["blue"]

    # for i in cor:
    #    i = cor_converter_notacao_birb_para_matplotlib(i)

    orientacao = orientacao_converter_notacao_birb_para_matplotlib(orientacao)
    # tipo_de_histograma = tipo_de_histograma_converter_notacao_birb_para_matplotlib(tipo_de_histograma)

    plt.hist(frequencias, espacos, tamanho_x, color=cor, rwidth=largura_segmentos, histtype='bar',
             orientation=orientacao)

    plt.title(nome_do_grafico)

    if definir_eixos:
        plt.xlabel(eixox)
        plt.ylabel(eixoy)
    if definir_plano_de_fundo:
        objeto_ax = plt.gca()
        objeto_ax.set_facecolor(cor_converter_notacao_birb_para_matplotlib(cor_de_fundo))
    if salvar_arquivo:
        plt.savefig(f"{nome_do_grafico}.png")

    plt.show()


def grafico_pizza(setores, tamanho_setores, cores, mostrar_legenda=True, nome_do_grafico="Gráfico Pizza",
                  definir_plano_de_fundo=False, cor_de_fundo="branco", salvar_arquivo=False):
    for i in range(len(cores)):
        cores[i] = cor_converter_notacao_birb_para_matplotlib(cores[i])

    plt.pie(tamanho_setores, labels=setores, colors=cores, autopct='%1.1f%%')

    plt.title(nome_do_grafico)

    if mostrar_legenda:
        plt.legend()
    if definir_plano_de_fundo:
        objeto_ax = plt.gca()
        objeto_ax.set_facecolor(cor_converter_notacao_birb_para_matplotlib(cor_de_fundo))
    if salvar_arquivo:
        plt.savefig(f"{nome_do_grafico}.png")

    plt.show()


def marcador_converter_notacao_birb_para_matplotlib(simbolo_birb_marcador):
    """Converte símbolos de marcador de pontos da notação birb para notação matplotlib. De uso interno do módulo.
        :param simbolo_birb_marcador: Símbolo de marcador de pontos, em notação birb.
        :type simbolo_birb_marcador: str

        :raise ValueError: Erro gerado caso o parâmetro passado não possa ser convertido

        :return: Símbolo de marcador, em notação matplotlib
        :rtype: str
    """

    if simbolo_birb_marcador == "ponto":
        simbolo_matplotlib_marcador = "."
    elif simbolo_birb_marcador == "pixel":
        simbolo_matplotlib_marcador = ","
    elif simbolo_birb_marcador == "circulo":
        simbolo_matplotlib_marcador = "o"
    elif simbolo_birb_marcador == "triangulo_para_baixo":
        simbolo_matplotlib_marcador = "v"
    elif simbolo_birb_marcador == "triangulo_para_cima":
        simbolo_matplotlib_marcador = "^"
    elif simbolo_birb_marcador == "triangulo_esquerdo":
        simbolo_matplotlib_marcador = "<"
    elif simbolo_birb_marcador == "triangulo_direito":
        simbolo_matplotlib_marcador = ">"
    elif simbolo_birb_marcador == "quadrado":
        simbolo_matplotlib_marcador = "s"
    elif simbolo_birb_marcador == "tri_baixo":
        simbolo_matplotlib_marcador = "1"
    elif simbolo_birb_marcador == "tri_cima":
        simbolo_matplotlib_marcador = "2"
    elif simbolo_birb_marcador == "tri_esquerdo":
        simbolo_matplotlib_marcador = "3"
    elif simbolo_birb_marcador == "tri_direito":
        simbolo_matplotlib_marcador = ">"
    elif simbolo_birb_marcador == "octogono":
        simbolo_matplotlib_marcador = "8"
    elif simbolo_birb_marcador == "pentagono":
        simbolo_matplotlib_marcador = "p"
    elif simbolo_birb_marcador == "mais_preenchido":
        simbolo_matplotlib_marcador = "P"
    elif simbolo_birb_marcador == "estrela":
        simbolo_matplotlib_marcador = "*"
    elif simbolo_birb_marcador == "mais":
        simbolo_matplotlib_marcador = "+"
    elif simbolo_birb_marcador == "hexagono1":
        simbolo_matplotlib_marcador = "h"
    elif simbolo_birb_marcador == "hexagono2":
        simbolo_matplotlib_marcador = "H"
    elif simbolo_birb_marcador == "x":
        simbolo_matplotlib_marcador = "x"
    elif simbolo_birb_marcador == "x_preenchido":
        simbolo_matplotlib_marcador = "X"
    elif simbolo_birb_marcador == "diamante":
        simbolo_matplotlib_marcador = "D"
    elif simbolo_birb_marcador == "diamante_fino":
        simbolo_matplotlib_marcador = "d"
    elif simbolo_birb_marcador == "vline":
        simbolo_matplotlib_marcador = "|"
    elif simbolo_birb_marcador == "hline":
        simbolo_matplotlib_marcador = "_"
    else:
        raise ValueError("Valor passado não consta na tabela de conversão de marcador")
    return simbolo_matplotlib_marcador


def linha_converter_notacao_birb_para_matplotlib(simbolo_birb_linha):
    """Converte símbolos de estilo de linha da notação birb para notação matplotlib. De uso interno do módulo.
        :param simbolo_birb_linha: Símbolo de estilo de linha, em notação birb.
        :type simbolo_birb_linha: str

        :raise ValueError: Erro gerado caso o parâmetro passado não possa ser convertido

        :return: Símbolo de linha, em notação matplotlib
        :rtype: str
    """

    if simbolo_birb_linha == "solida":
        simbolo_matplotlib_linha = "-"
    elif simbolo_birb_linha == "tracejada":
        simbolo_matplotlib_linha = "--"
    elif simbolo_birb_linha == "traco_ponto":
        simbolo_matplotlib_linha = "-."
    elif simbolo_birb_linha == "pontilhada":
        simbolo_matplotlib_linha = ":"
    else:
        raise ValueError("Valor passado não consta na tabela de conversão de linha")
    return simbolo_matplotlib_linha


def cor_converter_notacao_birb_para_matplotlib(simbolo_birb_cor):
    """Converte símbolos de cor da notação birb para notação matplotlib. De uso interno do módulo.
        :param simbolo_birb_cor: Símbolo de cor, em notação birb.
        :type simbolo_birb_cor: str

        :raise ValueError: Erro gerado caso o parâmetro passado não possa ser convertido

        :return: Símbolo de cor, em notação matplotlib
        :rtype: str
    """

    if simbolo_birb_cor == "azul":
        simbolo_matplotlib_cor = "b"
    elif simbolo_birb_cor == "verde":
        simbolo_matplotlib_cor = "g"
    elif simbolo_birb_cor == "vermelho":
        simbolo_matplotlib_cor = "r"
    elif simbolo_birb_cor == "ciano":
        simbolo_matplotlib_cor = "c"
    elif simbolo_birb_cor == "roxo":
        simbolo_matplotlib_cor = "m"
    elif simbolo_birb_cor == "amarelo":
        simbolo_matplotlib_cor = "y"
    elif simbolo_birb_cor == "preto":
        simbolo_matplotlib_cor = "k"
    elif simbolo_birb_cor == "branco":
        simbolo_matplotlib_cor = "w"
    else:
        raise ValueError("Valor passado não consta na tabela de conversão de cor")
    return simbolo_matplotlib_cor


def orientacao_converter_notacao_birb_para_matplotlib(simbolo_birb_orientacao):
    if simbolo_birb_orientacao == "vertical":
        simbolo_matplotlib_orientacao = "vertical"
    elif simbolo_birb_orientacao == "horizontal":
        simbolo_matplotlib_orientacao = "horizontal"
    else:
        raise ValueError("Valor passado não consta na tabela de conversão de orientacao")
    return simbolo_matplotlib_orientacao


def tipo_de_histograma_converter_notacao_birb_para_matplotlib(simbolo_birb_histograma):
    if simbolo_birb_histograma == "barra":
        simbolo_matplotlib_histograma = "bar"
    elif simbolo_birb_histograma == "barra_acumulada":
        simbolo_matplotlib_histograma = "barstacked"
    else:
        raise ValueError("Valor passado não consta na tabela de conversão de histograma")
    return simbolo_matplotlib_histograma
