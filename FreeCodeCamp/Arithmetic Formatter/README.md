# Arithmetic Formatter

## Objetivo:

Esse projeto foi feito para a conclusão do curso "Computação Cientifica com Python" da "Free Code Acamp"
>Clique aqui para saber mais sobre este curso: [[`Scientific Computing with Python`](https://www.freecodecamp.org/learn/scientific-computing-with-python/)]<br>
><br>
>Nesse link é possivel ter as informações gerais do projeto: [[`Build na Arithmetic Formatter Project`](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-an-arithmetic-formatter-project/build-an-arithmetic-formatter-project)]

## Descrição do projeto:

Você vai desenvolver uma função (geralmente chamada de arithmetic_arranger) que recebe uma lista de operações aritméticas em formato de texto (como strings de adição ou subtração) e retorna uma única string formatada, exibindo-as verticalmente lado a lado. A ideia é que essas operações fiquem alinhadas e apresentáveis, com espaços e traços posicionados corretamente. Opcionalmente, a função também pode mostrar os resultados das operações se for ativado esse comportamento.
<br >

Recebe entradas como "32 + 698" ou "3801 - 2" — várias operações em uma lista.

Retorna um texto organizado, montado com múltiplas linhas, uma para cada parte (os operandos, os operadores e os resultados, se solicitado), tudo alinhado.

Finalidade:
Praticar manipulação de strings em Python: padding, alinhamentos e concatenação.

Ganhar familiaridade com funções que trabalham com múltiplas entradas e retornam saídas formatadas — algo bastante útil para gerar relatórios ou imprimir dados visualmente organizados.

<br />

## Regras:

<br>
A função retornará a conversão correta se os problemas fornecidos estiverem formatados adequadamente; caso contrário, retornará uma string que descreve um erro relevante para o usuário.

* Situações que retornarão um erro:

  * Se houver muitos problemas fornecidos à função. O limite é cinco; qualquer valor acima disso retornará: 'Error: Too many problems.'

  * Os únicos operadores aceitos pela função são adição e subtração. Multiplicação e divisão retornarão um erro. Outros operadores não mencionados neste tópico não precisam ser testados. O erro     retornado será: "Error: Operator must be '+' or '-'."

  * Cada número (operando) deve conter apenas dígitos. Caso contrário, a função retornará: 'Error: Numbers must only contain digits.'

  * Cada operando (número em cada lado do operador) pode ter, no máximo, quatro dígitos. Caso contrário, a string de erro retornada será: 'Error: Numbers cannot be more than four digits.'

* Se o usuário fornecer o formato correto dos problemas, a conversão seguirá estas regras:

  * Deve haver um único espaço entre o operador e o maior dos dois operandos. O operador estará na mesma linha que o segundo operando, e ambos os operandos devem ser exibidos na mesma ordem em que foram fornecidos (o primeiro em cima e o segundo embaixo).

  * Os números devem estar alinhados à direita.

  * Deve haver quatro espaços entre cada problema.

  * Deve haver traços na parte inferior de cada problema. Os traços devem cobrir todo o comprimento de cada problema individualmente. 
<br />

