# Time Calculator

## Objetivo:

Esse projeto foi feito para a conclusão do curso "Computação Cientifica com Python" da "Free Code Acamp"
>Clique aqui para saber mais sobre este curso: [[`Scientific Computing with Python`](https://www.freecodecamp.org/learn/scientific-computing-with-python/)]<br>
><br>
>Nesse link é possivel ter as informações gerais do projeto: [[`Build a Polygon Area Calculator`](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-polygon-area-calculator-project/build-a-polygon-area-calculator-project)]

## Descrição do projeto e regras:

Neste projeto, você usará programação orientada a objetos para criar uma classe `Rectangle` e uma classe `Square`.  
A classe `Square` deve ser uma subclasse de `Rectangle` e herdar seus métodos e atributos.

Classe `Rectangle`:  

  Quando um objeto `Rectangle` for criado, ele deve ser inicializado com os atributos `width` e `height`.  
  A classe também deve conter os seguintes métodos:

  * `set_width`: define a largura.

  * `set_height`: define a altura.

  * `get_area`: retorna a área (`width * height`).

  * `get_perimeter`: retorna o perímetro (`2 * width + 2 * height`).

  * `get_diagonal`: retorna a diagonal (`(width ** 2 + height ** 2) ** 0.5`).

  * `get_picture`: retorna uma string que representa a forma usando linhas de `'*'`.  
      O número de linhas deve ser igual à altura e o número de `'*'` em cada linha deve ser igual à largura.  
      Deve haver uma nova linha (`\n`) no final de cada linha.  
      Se a largura ou altura for maior que 50, deve retornar a string: `'Too big for picture.'`.

  * `get_amount_inside`: recebe outra forma (quadrado ou retângulo) como argumento.  
      Retorna o número de vezes que a forma passada caberia dentro da forma atual (sem rotações).  
      Por exemplo, um retângulo com largura 4 e altura 8 caberia em dois quadrados com lados 4.

  * Se uma instância de `Rectangle` for representada como string, ela deverá ser exibida assim:  
      `Rectangle(width=5, height=10)`.

Classe `Square`:  

  A classe `Square` deve ser uma subclasse de `Rectangle`.  
  Quando um objeto `Square` for criado, um único comprimento lateral é passado.  
  O método `__init__` deve armazenar o comprimento lateral nos atributos `width` e `height` da classe `Rectangle`.

  * A classe `Square` deve poder acessar os métodos da classe `Rectangle`, mas também deve conter um método `set_side`.  

  * Se uma instância de `Square` for representada como string, ela deverá ser exibida assim:  
    `Square(side=9)`.

  * Os métodos `set_width` e `set_height` na classe `Square` devem definir tanto a largura quanto a altura.


## Exemplo de uso:
<pre> 
Código:
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
</pre>
<pre>  
Retorno do Console:
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
 </pre>






