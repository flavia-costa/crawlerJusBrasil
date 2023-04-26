<h1> Crawler JusBrasil</h1>

Este é um código é uma API simples em Python que contém uma função que consulta informações sobre processos judiciais em dois graus diferentes, e retorna essas informações em formato JSON.

A função é definida como "consultar_processo()". A função espera receber um JSON na solicitação POST, com a chave "numero_processoAlagoas" ou "numero_processoCeara", que é o número do processo que se deseja consultar.

O código utiliza as bibliotecas "Flask", "requests" e "BeautifulSoup" para fazer a solicitação às páginas da web, analisar as respostas e extrair as informações relevantes do HTML.

A função cria uma lista de dicionários chamada "listaProcessos", em que cada dicionário representa uma informação específica sobre o processo. Em seguida, essa lista é convertida em um dicionário principal chamado "resultado", que é retornado como JSON na resposta. Se alguma informação não puder ser encontrada, a função adiciona um valor padrão ao dicionário correspondente.

<h2> Funcionalidade </h2>

Para utilizar essa API deve:
- Ter o Python instalado em sua máquina;
- Abra o terminal ou prompt de comando e instale as bibliotecas necessárias (pip install flask requests beautifulsoup4);
- Salve todos os arquivos na mesma pasta;
- Primeiro rode "apiAlagoas.py" ou "apiCeara.py";
- Se tudo estiver configurado corretamente, você deverá ver a mensagem "Running on http://127.0.0.1:5000/". Isso significa que o servidor Flask está em execução em seu computador;
- Depois abre outro terminal e digite: "python consultaProcessoAlagoas.py" ou  "python consultaProcessoCeara.py";
- Com isso o número do processo informado no arquivo JSON "numero_processoAlagoas.json" ou "numero_processoCeara.json" irá ser consultado;
- No final um arquivo em formato JSON ira retornar contendo todas as informações pesquisadas;


