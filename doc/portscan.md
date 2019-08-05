# PortScan

## Definição

O **PortScan** [^1] TCP online irá procurar portas conhecidas abertas em um endereço IP.

A **API**[^2] usa a ferramenta **NMAP** [^3], uma ferramenta poderosa de varredura de portas, mas em sua versão grátis testa apenas as portas:

* **21  - FTP**
* **22 - SSH**
* **23 - Telnet**
* **80 - HTTP**
* **110 - POP3**
* **143 - IMAP**
* **443 - HTTPS**
* **3389 - RDP**

Pelos resultados do _port scanner_, geralmente é possível determinar se existe um **firewall** [^4] ativo e bloqueando todo o tráfego nas portas não utilizadas. Se algumas portas forem exibidas como _filtered_, indica que o _firewall_ ou _router_ está bloqueando o tráfego mas ela não está necessariamente fechada.


[^1]: [Portscanning](https://en.wikipedia.org/wiki/Port_scanner) *em inglês*
[^2]: [API Portscan](https://hackertarget.com/port-scanner/) *em inglês*
[^3]: [NMAP](https://nmap.org/man/pt_BR/) 
[^4]: [Firewall](https://en.wikipedia.org/wiki/Firewall_(computing)) *em inglês*


