import base64
from io import BytesIO

from libercom.models import Quizz


def get_graphs():
    graph = {}  # variavel para guardar todos os gráficos

    # pegando dados para construir o gráficos #

    po = {
        1: {
            0: "1- Qual o significado de www?",
            1: [
                "world wide web",
                "wide world web",
                "when wide web",
                "what wide web",
            ]
        },
        2: {
            0: "2- Quem criou o telégrafo?",
            1: [
                "Júlio Cezar",
                "Abraham Lincoln",
                "Thomas Edison",
                "Samuel Morse",
            ]

        },
        3: {
            0: "3- O primeiro protótipo de telefone foi criado por?",
            1: [
                "Graham Bell",
                "Guglielmo Marconi",
                "Landell de Moura",
                "Antonio Meucci",
            ]

        },
        4: {
            0: "4- Quem foi o inventor do rádio?",
            1: [
                "Gilberto Gil",
                "Johann-Philipp",
                "Ventura",
                "Antonio Meucci",
            ]

        },
        5: {
            0: "5- O que significa GPS?",
            1: [
                "global position...",
                "geral position...",
                "general positio...",
                "universal posit... ",
            ]

        },
        6: {
            0: "6- Qual opção esta correcta?",
            1: [
                "Thomas Edison foi...",
                "As antenas de tel...",
                "O palmeiras não t...",
                "O sistema android...",
            ]

        },
        7: {
            0: "7- A televisão no Brasil surgiu em?",
            1: [
                "1965",
                "2000",
                "1800",
                "1970",
            ]

        },
        8: {
            0: "8- Qual opção esta correcta?",
            1: [
                "A internet surgiu a...",
                "O primeiro protótipo...",
                "O Wi-fi foi inventado...",
                "O primeiro computador...",
            ]

        },
        9: {
            0: "9- O que é cabo coaxial?",
            1: [
                "Uma espécie de cabo ...",
                "Cabo utilizado para ...",
                "É utilizado para fins...",
                "É uma espécie de cabo...",
            ]

        },
        10: {
            0: "10- O que significa IP?",
            1: [
                "Internet Protocol",
                "Internet Process",
                "Interface Protocol",
                "Internet Program",
            ]
        },
    }  # para montar os gráficos por pergunta

    perguntas = [("Pergunta " + str(x)) for x in range(1, 11)]  # montando label x para o grafico principal

    answer = [0] * 10  # lista para guardar a quantidade de respostas certas por pergunta

    quizz = Quizz.objects.all()  # pegando todos os quizzes respondidos

    sum_answer = {x: [0] * 4 for x in range(1, 11)}  # contando respostas em cada opcao

    # separando dados #
    for q in quizz:
        if q.p1 == 1:
            answer[0] += 1

        if q.p2 == 4:
            answer[1] += 1

        if q.p3 == 1:
            answer[2] += 1

        if q.p4 == 4:
            answer[3] += 1

        if q.p5 == 1:
            answer[4] += 1

        if q.p6 == 2:
            answer[5] += 1

        if q.p7 == 1:
            answer[6] += 1

        if q.p8 == 1:
            answer[7] += 1

        if q.p9 == 1:
            answer[8] += 1

        if q.p10 == 1:
            answer[9] += 1

        # pegar as informações
        # sum_answer[index da pergunta][qual a opção que ele escolheu]
        # exemplo {1 : [ 0, 4, 5, 2]} neste exemplo a primeira questão teve 4 votos na segunda opção...
        sum_answer[1][q.p1 - 1] += 1
        sum_answer[2][q.p2 - 1] += 1
        sum_answer[3][q.p3 - 1] += 1
        sum_answer[4][q.p4 - 1] += 1
        sum_answer[5][q.p5 - 1] += 1
        sum_answer[6][q.p6 - 1] += 1
        sum_answer[7][q.p7 - 1] += 1
        sum_answer[8][q.p8 - 1] += 1
        sum_answer[9][q.p9 - 1] += 1
        sum_answer[10][q.p10 - 1] += 1

    graph['geral'] = {'x': perguntas, 'y': answer}
    for i in range(1, 11):
        graph[('p' + str(i))] = {'x': po[i][1], 'y': sum_answer[i]}

    # criando gráfico geral

    # get_plot(dados de x,nome da label x,
    #           dados de y, nome da label y,
    #           nome do gráfico , tamanho do gráfico em x,tamanho do gráfico em y, rotação das labels em x
    # graph['geral'] = get_plot(perguntas, 'Perguntas',
    #                         answer, 'Quantidade de acertos',
    #                        'Respostas Certas vs Pergunta', 10, 5, 45)  # gráfico geral

    # for i in range(1, 11):
    #   graph[('p' + str(i))] = get_plot(po[i][1], 'Opções',
    #                                   sum_answer[i], 'Nº de pessoas ',
    #                                  po[i][0], 4, 5, 60)  # gráfico de cada pergunta

    return graph
