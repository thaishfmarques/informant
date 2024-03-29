# Informant

![enter image description here](https://lh3.googleusercontent.com/SrjQSw5ODItBgAylNuAlQo54Q2vT5DPhclMIbKmZfnbPIyJQ41MZ6TNaVO9R4RQFtXckiuTv0GGQ6C4Mhj8tdN2FzaEXhTHv_YNFlljtFJ-TmCTMnYJW1tIy_1QwQMroJnYRCbKUGfAzaC7ZHgPueDxxy0l43BfrgwcH8NWYRLt_6GJnCF4DJu19HpkTvEoGqPhfWBO1CCYTFXrDshx--oFCnRMrvgSd4igO1eAOmiOpprj5q9n4XNrYR_9JXEdIx-Qe7pmSv0gh7Hw_n-eaKXpq9DuWGfgzWifE03cnQY6hjjGomQV324GqNlGZNsVnS628Au-hgRpBoTaCMnRal7mCpByGIVPbeEekNOIXX5dqJCZCZuGUz5EmRQJZoPI-XLFHmLu4YAwm33Q1J4o_FStAM0IMd6kHF06KeMTBYb1gE0yY7JYtkqF4BUvUekRIyWzIU7LkL7s4eLANoW8ONTJ9kiiNI60MoWJTuY5svUwpQPT1nXAzHgOVqzs3J5wU41yLzlKO1r8CED4n77lIBYo29B4d4VITBX0xB2-Mmh9x6JUxnEQsB0pLW-M7366xeJ8t9H46NRwLXOmAKVaPrtmaxHmHpa1du3alIgzkWt61guxLXBiJCMii74AF5zNKIw2LZyvGKp1bvSIfvHUiOBz6Eoj2pZPyszFsODP4kMJcCsggPiHKRGwr0ZvuJPZkuXZDhk9LYtywYQx9enfraKyeKg=w480-h280-no)

## Introdução

**Informant** é uma ferramenta open source desenvolvida em python3
para auxiliar na fase de reconhecimento do pentest.  
Também em desenvolvimento a função de auditoria para checklist de diretório padrão de instalação.    

A ferramenta funciona online e consome as APIs do [Hacker Target](https://hackertarget.com/).  As APIs são de uso limitado a 100 chamadas por dia para cada IP.


## Funções

### Tela Inicial

-  **Online Tools**
	* Ferramentas para coleta de informações
		+  [_whois_](https://github.com/thaishfmarques/informant/blob/master/doc/whois.md)
		+  [_geoip_](https://github.com/thaishfmarques/informant/blob/master/doc/geoip.md)
		+  [_portscan_](https://github.com/thaishfmarques/informant/blob/master/doc/portscan.md)

	* Ferramenta de varredura de dispositivos conectados a rede
		+  [_shodan search_](https://github.com/thaishfmarques/informant/blob/master/doc/shodan.md) *** _IN DEVELOPMENT_


## Instalação

**Opcional:** Recomendável a instalação do virtualenv, uma ferramenta utilizada para criar ambientes isolados de Python.  
```
$ pip install virtualenv
```


```
$ git clone https://github.com/thaishfmarques/informant.git ./informant
$ cd informant
$ virtualenv <environment> **_opcional_
$ source /path/to/ENV/bin/activate **_opcional_
$ pip install -r requirements.txt
$ python3 informant.py
```

Para desabilitar o virtualenv  
```
$ deactivate
```


## Utilização


[Glossário](https://github.com/thaishfmarques/informant/blob/master/doc/glossario.md) de utilização da ferramenta.  
Possui informações de funções, variáveis utilizadas e módulos instalados.

## Compatibilidade

A ferramenta foi desenvolvida em python3, porém, irá funcionar inicialmente só em sistemas *GNU/Linux*
  

**OS testados:**

* Ubuntu 18.04

## Versão

* v0.9
	+  _in development (08/2019)_
	+  _adding shodan search (09/08/2019)_
	+  _adding glossary (12/08/2019)_
	+  _final changes (13/08/2019)_


## License

A ferramenta foi desenvolvida sob a licença MIT  
Detalhes: [LICENSE](https://github.com/thaishfmarques/informant/blob/master/LICENSE)

  

## Disclaimer

O intuito desse script é acadêmico e deve ser utilizado exclusivamente para este fim. Invasão de dispositivos é crime e está previso no Art. 154-A do Decreto-Lei nº 2.848.  
A utilização da ferramenta deve ser feita somente em rede local própria.  

## Author

: @thaishfmarques

## Contributed
- Adner Souza  
- Deovanir  

> Written with [StackEdit](https://stackedit.io/).
