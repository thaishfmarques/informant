# WHOIS

## Definição

**Whois** [^1] é um protocolo que busca informações de contato e domínio de um host. Pode revelar seu dono, o dominio, endereço IP e outras informações de contato, como email, nome de responsáveis e números de telefone.  

O protocolo possui um componente que escuta a porta 43 - **TCP** [^2]. O cliente estabelece uma conexão a essa porta e retorna as informações em texto simples.

Muitos serviços de registro de domínio permitem que as informações sejam marcadas como privadas e ocultas ou públicas 

O protocolo whois foi baseado no protocolo finger em 1977, durante a era inicial da internet conhecida como **ARPANET** [^3].

Para o projeto foi utilizada a **API** whois do **HackerTarget** [^4].


[^1]: [Whois](https://en.wikipedia.org/wiki/WHOIS) *(em inglês)*
[^2]: [TCP](https://www.ietf.org/rfc/rfc0793) *(em inglês)*
[^3]: [ARPANET](https://pt.wikipedia.org/wiki/ARPANET)
[^4]: [API whois](https://hackertarget.com/whois-lookup/) *(em inglês)*
