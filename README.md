Calculador de Tempo de Vida
Este projeto é uma ferramenta de linha de comandos desenvolvida em Python que calcula com precisão o tempo decorrido desde uma data de nascimento (ou qualquer data inicial) até à data atual. O programa detalha o tempo vivido em anos, meses e dias, considerando anos bissextos e a variabilidade dos dias em cada mês.

Funcionalidades
Cálculo Preciso: Calcula a idade exata em anos, meses e dias.

Validação de Dados: Verifica se a data inserida é válida, respeitando o número de dias de cada mês e anos bissextos.

Interface Interativa: Permite realizar múltiplos cálculos numa única execução através de um ciclo de interação.

Feedback Visual: Utiliza cores no terminal para destacar informações importantes e erros.

Mensagens Personalizadas: Exibe mensagens especiais caso a data coincida com o aniversário do utilizador.

Estrutura do Projeto
calculador_de_tempo_de_vida.py: O script principal que contém a lógica do calculador e a interface de utilizador.

praticas_e_anotacoes.py: Um ficheiro contendo rascunhos de código e anotações de estudo, incluindo exemplos de formatação de strings e manipulação de datas.

requirements.txt: Lista as bibliotecas Python presentes no ambiente de desenvolvimento.

.gitignore: Ficheiro de configuração para exclusão de ficheiros desnecessários no controlo de versões (ex: ambientes virtuais, cache).

Pré-requisitos
Python 3.x instalado.

Bibliotecas listadas no requirements.txt (embora o script principal utilize maioritariamente a biblioteca padrão datetime).

Instalação
Clone este repositório para a sua máquina local.

(Opcional) Crie e ative um ambiente virtual.

Instale as dependências listadas no ficheiro requirements.txt:

Bash

pip install -r requirements.txt
Nota: O ficheiro requirements.txt inclui requests e pandas. Certifique-se de que pretende instalar estas bibliotecas, caso planeie expandir o projeto, embora o script principal funcione com as bibliotecas padrão.

Como Utilizar
Navegue até ao diretório do projeto no seu terminal.

Execute o script principal:

Bash

python calculador_de_tempo_de_vida.py
Siga as instruções no ecrã e introduza a data de nascimento no formato dd/mm/aaaa (exemplo: 15/04/1990).

O programa exibirá o tempo vivido. Pode optar por realizar um novo cálculo ou sair digitando S ou N quando solicitado.

Autor
Desenvolvido por Leonardo Broinizi.
