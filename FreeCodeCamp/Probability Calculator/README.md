# Time Calculator

## Objetivo:

Esse projeto foi feito para a conclusão do curso "Computação Cientifica com Python" da "Free Code Acamp"
>Clique aqui para saber mais sobre este curso: [[`Scientific Computing with Python`](https://www.freecodecamp.org/learn/scientific-computing-with-python/)]<br>
><br>
>Nesse link é possivel ter as informações gerais do projeto: [[`Build a Probability Calculator`](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-probability-calculator-project/build-a-probability-calculator-project)]

## Descrição do projeto e regras:

Suponha que haja um chapéu contendo 5 bolas azuis, 4 vermelhas e 2 verdes.  
Qual é a probabilidade de que um sorteio aleatório de 4 bolas contenha pelo menos 1 vermelha e 2 verdes?  
Embora seja possível calcular a probabilidade usando matemática avançada, uma maneira mais fácil é escrever um programa que realize um grande número de experimentos para estimar uma probabilidade aproximada.

Para este projeto, você escreverá um programa para determinar a probabilidade aproximada de tirar certas bolas aleatoriamente de um chapéu.

Primeiro, crie uma classe `Hat` em `main.py`.  
A classe deve receber um número variável de argumentos que especifiquem o número de bolas de cada cor que estão no chapéu.  
Por exemplo, um objeto da classe pode ser criado de qualquer uma destas maneiras:
<pre>
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
</pre>

Um chapéu sempre será criado com pelo menos uma bola.  
Os argumentos passados para o objeto chapéu na criação devem ser convertidos em uma variável de instância `contents`.  
`contents` deve ser uma lista de strings contendo um item para cada bola do chapéu.  
Cada item na lista deve ser um nome de cor representando uma única bola daquela cor.  
Por exemplo, se o seu chapéu for `{'red': 2, 'blue': 1}`, `contents` deve ser `['red', 'red', 'blue']`.

A classe `Hat` deve ter um método `draw` que aceite um argumento indicando o número de bolas a serem retiradas do chapéu.  
Este método deve remover bolas aleatoriamente de `contents` e retorná-las como uma lista de strings.  
As bolas não devem retornar ao chapéu durante o sorteio, semelhante a um experimento com urna sem reposição.  
Se o número de bolas a serem retiradas exceder a quantidade disponível, retorne todas as bolas.

Em seguida, crie uma função `experiment` em `main.py` (não dentro da classe `Hat`).  
Essa função deve aceitar os seguintes argumentos:

  - `hat`: um objeto da classe `Hat` contendo bolas que devem ser copiadas dentro da função.

  - `expected_balls`: um objeto que indica o grupo exato de bolas a serem retiradas do chapéu para o experimento.  
    Por exemplo, para determinar a probabilidade de retirar 2 bolas azuis e 1 bola vermelha, defina `expected_balls` como `{'blue': 2, 'red': 1}`.

  - `num_balls_drawn`: o número de bolas a serem retiradas do chapéu em cada experimento.

  - `num_experiments`: o número de experimentos a serem realizados. (Quanto mais experimentos forem realizados, mais precisa será a probabilidade aproximada.)

A função `experiment` deve retornar uma probabilidade.

 Por exemplo, se você quiser determinar a probabilidade de obter pelo menos duas bolas vermelhas e uma verde ao tirar cinco bolas de um chapéu contendo seis pretas, quatro vermelhas e três verdes, você realizará N experimentos, contará quantas vezes M você obtém pelo menos duas bolas vermelhas e uma verde, e estimará a probabilidade como M/N.  
Cada experimento consiste em começar com um chapéu contendo as bolas especificadas, tirar várias bolas e verificar se você acertou as bolas que estava tentando tirar.

## Exemplo de uso:
<pre> 
Código:
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
</pre>
<pre>  
Retorno do Console (algo parecido):
0.356
</pre>






