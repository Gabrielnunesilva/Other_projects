# Time Calculator

## Objetivo:

Esse projeto foi feito para a conclusão do curso "Computação Cientifica com Python" da "Free Code Acamp"
>Clique aqui para saber mais sobre este curso: [[`Scientific Computing with Python`](https://www.freecodecamp.org/learn/scientific-computing-with-python/)]
><br>
>Nesse link é possivel ter as informações gerais do projeto: [[`Build na Arithmetic Formatter Project`](https://www.freecodecamp.org/learn/scientific-computing-with-python/#build-a-time-calculator-project)]

## Descrição do projeto e regras:

* Escreva uma função chamada `add_time` que receba dois parâmetros obrigatórios e um parâmetro opcional:

* Uma hora de início no formato de relógio de 12 horas (terminando em AM ou PM).

* Um tempo de duração que indique o número de horas e minutos.

* (Opcional) Um dia de início da semana, sem distinção entre maiúsculas e minúsculas.

* A função deve adicionar o tempo de duração ao tempo de início e retornar o resultado.

* Se o resultado for no dia seguinte, ele deverá exibir `(next day)` após o horário.

* Se o resultado for mais de um dia depois, ele deverá exibir `(n days later)` após o horário, onde "n" é o número de dias decorridos.

* Se a função receber o parâmetro opcional "dia inicial da semana", a saída deverá exibir o dia da semana do resultado.

* O dia da semana na saída deverá aparecer após a hora e antes da informação de dias decorridos.

* Abaixo estão alguns exemplos de diferentes casos que a função deve tratar. Preste muita atenção ao espaçamento e à pontuação dos resultados.

* Não importe nenhuma biblioteca Python. Suponha que os horários de início sejam válidos. Os minutos no tempo de duração serão um número inteiro menor que 60, mas a hora pode ser qualquer número inteiro.


## Exemplos:
add_time('3:00 PM', '3:10')
>Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
>Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
>Returns: 12:03 PM

add_time('10:10 PM', '3:30')
>Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
>Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
>Returns: 7:42 AM (9 days later)

<br />

