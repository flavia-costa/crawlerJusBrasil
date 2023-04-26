from flask import Flask, request, jsonify
import json
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def consultar_processo():

    numero_processoCeara = request.json['numero_processoCeara']

    url1Grau = f'https://esaj.tjce.jus.br/cpopg/show.do?processo.codigo=01Z081I9T0000&processo.foro=1&processo.numero={numero_processoCeara}'
    url2Grau = f'https://esaj.tjce.jus.br/cposg5/search.do?conversationId=&paginaConsulta=0&cbPesquisa=NUMPROC&numeroDigitoAnoUnificado=0624478-78.2023&foroNumeroUnificado=0000&dePesquisaNuUnificado={numero_processoCeara}&dePesquisaNuUnificado=UNIFICADO&dePesquisa=&tipoNuProcesso=UNIFICADO'

    response1Grau = requests.get(url1Grau)
    bsobj1Grau = BeautifulSoup(response1Grau.text, 'html.parser')


    listaProcessos = []
    numeroProcesso_element1Grau = bsobj1Grau.find_all(id="numeroProcesso")
    classe_element1Grau = bsobj1Grau.find_all(id="classeProcesso")
    area_element1Grau = bsobj1Grau.find_all(id="areaProcesso")
    assunto_element1Grau = bsobj1Grau.find_all(id="assuntoProcesso")
    dataDistribuicao_element1Grau = bsobj1Grau.find_all(id="dataHoraDistribuicaoProcesso")
    juiz_element1Grau = bsobj1Grau.find(id="juizProcesso")
    valorDaAcao_element1Grau = bsobj1Grau.find_all(id="valorAcaoProcesso")
    partesProcesso_element1Grau = bsobj1Grau.find_all(id="tableTodasPartes")
    ultimasMovimentacoes_element1Grau = bsobj1Grau.find_all(class_=["dataMovimentacao", "descricaoMovimentacao"])

    if numeroProcesso_element1Grau:
        numeroProcesso = numeroProcesso_element1Grau[0].text.strip()
        info = {"Numero do Processo": numeroProcesso}    
    else:
        info = {"Numero do Processo": "Processo não encontrado"}
    listaProcessos.append(info)

    if classe_element1Grau:
        classe = classe_element1Grau[0].text.strip()
        info = {"Classe": classe}    
    else:
        info = {"Classe": "Não tem Classe"}
    listaProcessos.append(info)

    if area_element1Grau:
        area = area_element1Grau[0].text.strip()
        info = {"Área": area}
    else:
        info = {"Área": "Não tem area"}
    listaProcessos.append(info)

    if assunto_element1Grau:
        assunto = assunto_element1Grau[0].text.strip()
        info = {"Assunto": assunto}
    else:
        info = { "Assunto": "Não tem assunto"}
    listaProcessos.append(info)

    if dataDistribuicao_element1Grau:
        dataDistribuicao = dataDistribuicao_element1Grau[0].text.strip()
        info = { "Data de Distribuição": dataDistribuicao}
    else:
        info = {"Data de Distribuição": "Não tem data de distribuição"}
    listaProcessos.append(info)

    if juiz_element1Grau:
        juiz = juiz_element1Grau.text.strip()
        info = {"Juiz": juiz}
    else:
        info = {"Juiz": "Não tem juiz"}
    listaProcessos.append(info)

    if valorDaAcao_element1Grau:
        valorDaAcao = valorDaAcao_element1Grau[0].text.strip().replace('\n', '').replace('\t', '')
        info = { "Valor da Ação": valorDaAcao}
    else:
        info = {"Valor da Ação": "Não tem valor da ação"}
    listaProcessos.append(info)

    if partesProcesso_element1Grau:
        partesProcesso = partesProcesso_element1Grau[0].text.strip().replace('\n', '').replace('\t', '')
        info = {"Partes do Processo": partesProcesso}
    else:
        info = {"Partes do Processo": "Não tem partes do processo"}
    listaProcessos.append(info)

    movimentacoes = []

    for i in range(0, len(ultimasMovimentacoes_element1Grau), 2):
        data = ultimasMovimentacoes_element1Grau[i].text.strip().replace('\n', '').replace('\t', '')
        descricao = ultimasMovimentacoes_element1Grau[i].find_next_sibling(class_="descricaoMovimentacao").text.strip().replace('\n', '').replace('\t', '').replace('\r', '')

        movimentacoes.append({
            'Data': data,
            'Descricao': descricao
        })

    if movimentacoes:
        info = {"Ultimas Movimentacoes": movimentacoes }
    else:
        info = { "Ultimas Movimentacoes": "Não foi possível encontrar as Ultimas Movimentacoes"}
    listaProcessos.append(info)

    #Começa a pesquisa para o 2 Grau do Processo

    response2Grau = requests.get(url2Grau)
    bsobj2Grau = BeautifulSoup(response2Grau.text, 'html.parser')

    numeroProcesso_element2Grau = bsobj2Grau.find_all(id="numeroProcesso")
    classe_element2Grau = bsobj2Grau.find_all(id="classeProcesso")
    area_element2Grau = bsobj2Grau.find_all(id="areaProcesso")
    assunto_element2Grau = bsobj2Grau.find_all(id="assuntoProcesso")
    dataDistribuicao_element2Grau = bsobj2Grau.find_all(id="dataHoraDistribuicaoProcesso")
    juiz_element2Grau = bsobj2Grau.find(id="juizProcesso")
    valorDaAcao_element2Grau = bsobj2Grau.find_all(id="valorAcaoProcesso")
    partesProcesso_element2Grau = bsobj2Grau.find_all(id="tableTodasPartes")
    ultimasMovimentacoes_element2Grau = bsobj2Grau.find_all(class_=["dataMovimentacao", "descricaoMovimentacao"])

    if numeroProcesso_element2Grau:
        numeroProcesso = numeroProcesso_element2Grau[0].text.strip()
        info = {"Numero do Processo 2 Grau": numeroProcesso}    
    else:
        info = {"Numero do Processo 2 Grau": "Processo não encontrado"}
    listaProcessos.append(info)

    if classe_element2Grau:
        classe = classe_element2Grau[0].text.strip()
        info = {"Classe 2 Grau": classe}    
    else:
        info = {"Classe2 Grau": "Não tem Classe"}
    listaProcessos.append(info)

    if area_element2Grau:
        area = area_element2Grau[0].text.strip()
        info = {"Área 2 Grau": area}
    else:
        info = {"Área 2 Grau": "Não tem area"}
    listaProcessos.append(info)

    if assunto_element2Grau:
        assunto = assunto_element2Grau[0].text.strip()
        info = {"Assunto 2 Grau": assunto}
    else:
        info = { "Assunto 2 Grau": "Não tem assunto"}
    listaProcessos.append(info)

    if dataDistribuicao_element2Grau:
        dataDistribuicao = dataDistribuicao_element2Grau[0].text.strip()
        info = { "Data de Distribuição 2 Grau": dataDistribuicao}
    else:
        info = {"Data de Distribuição 2 Grau": "Não tem data de distribuição"}
    listaProcessos.append(info)

    if juiz_element2Grau:
        juiz = juiz_element2Grau.text.strip()
        info = {"Juiz 2 Grau": juiz}
    else:
        info = {"Juiz 2 Grau": "Não tem juiz"}
    listaProcessos.append(info)

    if valorDaAcao_element2Grau:
        valorDaAcao = valorDaAcao_element2Grau[0].text.strip().replace('\n', '').replace('\t', '')
        info = { "Valor da Ação 2 Grau": valorDaAcao}
    else:
        info = {"Valor da Ação 2 Grau": "Não tem valor da ação"}
    listaProcessos.append(info)

    if partesProcesso_element2Grau:
        partesProcesso = partesProcesso_element2Grau[0].text.strip().replace('\n', '').replace('\t', '')
        info = {"Partes do Processo 2 Grau": partesProcesso}
    else:
        info = {"Partes do Processo 2 Grau": "Não tem partes do processo"}
    listaProcessos.append(info)

    movimentacoes = []

    for i in range(0, len(ultimasMovimentacoes_element2Grau), 2):
        data = ultimasMovimentacoes_element2Grau[i].text.strip().replace('\n', '').replace('\t', '')
        descricao = ultimasMovimentacoes_element2Grau[i].find_next_sibling(class_="descricaoMovimentacao").text.strip().replace('\n', '').replace('\t', '').replace('\r', '')

        movimentacoes.append({
            'Data 2 Grau': data,
            'Descricao 2 Grau': descricao
        })

    if movimentacoes:
        info = {"Ultimas Movimentacoes 2 Grau": movimentacoes }
    else:
        info = { "Ultimas Movimentacoes 2 Grau": "Não foi possível encontrar as Ultimas Movimentacoes"}
    listaProcessos.append(info)

    return jsonify(listaProcessos)

if __name__ == '__main__':
    app.run()
