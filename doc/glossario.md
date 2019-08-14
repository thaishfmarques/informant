# GLOSSÁRIO

Dicionário de funções da ferramenta

## informant.py

Importa o módulo local banner que contém os menus da ferramenta

## banner.py

### Módulos de sistema:  
_**platform**:_  módulo utilizado para trazer informações de sistema operacional    
 _**subprocess**:_ chamada para executar shell em python, utilizado para retornar saída do comando como válida  
_**os**:_ import do pacote _system_ para utilizar método exit() - que encerra o processo do programa  
_**time**:_ import do pacote _sleep_ -  suspende a execução do programa por um tempo determinado (usado para criar sensação de carregamento)  
_**socket**:_ import do módulo gethostname - traz nome do host atual  

### Módulos locais:
_**whois**:_ importa o modulo com a função whois  
_**geoip**:_ importa o modulo com a função geoip  
_**portscan**:_ importa o modulo com a função portscan  
_**shodanz**:_ importa o modulo com a função shodan  

### Funções

_**def clean()**:_  função que limpa o console de acordo com o sistema operacional. *** _Não foi
 testado em plataforma Windows_  
 _**def banner()**:_ função traz o banner inicial do programa, com o nome, versão, sistema operacional da máquina do usuário e hostname da máquina  
_**def  menu_splash()**:_ função de menu inicial traz as funcionalidades desenvolvidas na ferramenta  
_**def  menu_online()**:_ função referente à opção #1 do menu_splash. Traz as opções disponíveis para o recolhimento de informações.    
_**def  menu_shodan()**:_ função que acessa o menu da funcionalidade Shodan. (requer chave de API).  

### Variáveis

_**VERSION:**_  versão atual do programa  
_**os_dist:**_ recebe qual a distro linux o usuário utiliza  
_**os:**_ traz informação completa do sistema operaciona + distro (somente Linux)  
_**menu_option:**_ acessa as opções do menu em todas as funções de menu e chama as funções disponíveis  
_**menu:**_ acessa as opções do menu   
_**api_key**_ recebe a chave que habilita a função do shodan. _!important:_ a chave não é armazenada  


## whois.py

### Módulo
_**requests**_ Modulo third-party que permite requisições HTTP  
_**os.path**_ importa do módulo _os_  o pacote _path_ que habilita a funções de percorrer diretórios  

### Funções
 _**def whois():**_ consome a API do hackertarget e traz informações do protocolo whois, com informações de registro do host.  
 Imprime em tela o resultado e tenta salvar o resultado em um arquivo de texto.

### Variáveis
_**hostname:**_ recebe o hostname à recolher informações.  
_**response:**_ armazena as informações da requisição http  
_**whois:**_ armazena as informações da requisição convertida em texto  
_**folder_path + save_to_folder:**_ recebe informações do caminho onde os dados serão gravados  


## geoip.py

### Módulo
_**requests**_ Modulo third-party que permite requisições HTTP  

### Funções
 _**def geoip():**_ consome a API do hackertarget e traz informações de geolocalização do host.  

### Variáveis
_**hostname:**_ recebe o hostname à recolher informações.  
_**response:**_ armazena as informações da requisição http  


## portscan.py

### Módulo
_**requests**_ Modulo third-party que permite requisições HTTP  

### Funções
 _**def portscan():**_ consome a API do hackertarget e realiza um escaneamento de porta no host alvo

### Variáveis
_**hostname:**_ recebe o hostname à recolher informações.  
_**response:**_ armazena as informações da requisição http  
_**scan:**_ armazena as informações da requisição convertida em texto  


## shodan.py
A funcionalisdade do shodan está disponivel na ferramenta pela API python do Shodan e a chave deve ser resgatada em https://account.shodan.io.  
A funcionalidade não está acessiível pela ferramenta, mas o codigo fonte está disponível.

### Módulo
_**shodan**_ Modulo third-party que permite pesquisar por dispositivos na rede  
_**os.path**_ importa do módulo _os_  o pacote _path_ que habilita a funções de percorrer diretórios  

### Funções
 _**def shodanz():**_ realizada buscas por dispositivos na rede.  
 Na versão free aceita apenas buscas simples.   
 
### Variáveis
_**search:**_ pesquisa parâmetros simples no shodan    
_**results:**_ retorna o resultado da busca pela API
_**folder_path + save_to_folder:**_ recebe informações do caminho onde os dados serão gravados  

> Written with [StackEdit](https://stackedit.io/).
