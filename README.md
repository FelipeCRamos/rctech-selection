# Desafio: RCTech - Jan.2019
É por meio deste, que venho propor minha resolução para o desafio proposto.

## Solução utilizada
Como é um problema relativamente simples (capturar noticias de um site somente), 
optei por utilizar uma técnica que já sou familiar que é a do web scraping com 
o `urllib` no `python 3.6`.

Após feito o _scraping_, é armazenado os novos resultados ao banco de dados, na
tabela `home_post`, que posteriormente é usado pelo próprio django para exibição
na interface web da query inicial e de pesquisa.

## Dependências
+ `django 2.1.5`
+ `urllib`
+ `python 3.6`

# Authorship
Código desenvolvido por Felipe Ramos e é aplicada a licença do **MIT**.
