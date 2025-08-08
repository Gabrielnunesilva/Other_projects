# Time Calculator

## Objetivo:

Esse projeto foi feito para a conclusão do curso "Computação Cientifica com Python" da "Free Code Acamp"
>Clique aqui para saber mais sobre este curso: [[`Scientific Computing with Python`](https://www.freecodecamp.org/learn/scientific-computing-with-python/)]<br>
><br>
>Nesse link é possivel ter as informações gerais do projeto: [[`Build a Budget App Project`](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-budget-app-project/build-a-budget-app-project)]

## Descrição do projeto e regras:

Complete a classe `Category`. Ela deve ser capaz de instanciar objetos com base em diferentes categorias de orçamento, como alimentação, vestuário e entretenimento.  
Quando os objetos são criados, eles recebem o nome da categoria.

  * A classe deve ter uma variável de instância chamada `ledger`, que é uma lista.

  * A classe deve conter os seguintes métodos:

  * `deposit`: aceita um valor e uma descrição. Se nenhuma descrição for fornecida, o padrão deve ser uma string vazia. O método deve adicionar um objeto à lista do razão no formato `{'amount': amount, 'description': description}`.

  * `withdraw`: semelhante ao método `deposit`, mas o valor passado deve ser armazenado no livro-razão como um número negativo.
  * Se não houver fundos suficientes, nada deve ser adicionado ao livro-razão. Este método deve retornar `True` se o saque ocorreu e `False` caso contrário.

  * `get_balance`: retorna o saldo atual da categoria de orçamento com base nos depósitos e retiradas.

  * `transfer`: aceita um valor e outra categoria de orçamento como argumentos.  
    O método deve adicionar um saque com o valor e a descrição `"Transferir para [Categoria de Destino]"`.  
    Depois, deve adicionar um depósito na outra categoria de orçamento com o valor e a descrição `"Transferir de [Categoria de Origem]"`.  
    Se não houver fundos suficientes, nada deve ser adicionado a nenhum dos livros-razão.  
    Este método deve retornar `True` se a transferência ocorreu e `False` caso contrário.

  * `check_funds`: aceita um valor como argumento e retorna `False` se o valor for maior que o saldo da categoria de orçamento, e `True` caso contrário.  
    Este método deve ser usado tanto pelo método `withdraw` quanto pelo método `transfer`.

  Quando o objeto de orçamento for impresso, ele deverá exibir:
  - Uma linha de título de 30 caracteres, onde o nome da categoria é centralizado, cercado por caracteres `*`.
  - Uma lista dos itens do livro-razão. Cada linha deve mostrar a descrição (primeiros 23 caracteres) e o valor (alinhado à direita, com duas casas decimais e no máximo 7 caracteres).
  - Uma linha exibindo o total da categoria.

 Além da classe `Category`, crie uma função (fora da classe) chamada `create_spend_chart` que receba uma lista de categorias como argumento e retorne uma string representando um gráfico de barras.

  O gráfico deve mostrar a porcentagem gasta em cada categoria, considerando apenas saques (não depósitos).  
  A porcentagem deve ser calculada em relação ao total gasto em todas as categorias.  
  A altura de cada barra deve ser arredondada para baixo para a dezena mais próxima.

* No lado esquerdo do gráfico, devem haver rótulos de 0 a 100.  
As barras devem ser feitas com o caractere `"o"`.  
A linha horizontal abaixo das barras deve passar dois espaços da barra final.  
O nome de cada categoria deve ser escrito verticalmente abaixo da barra.  
Deve haver um título na parte superior que diga `"Porcentagem gasta por categoria"`.

* A função será testada com até quatro categorias.

* O espaçamento e a formatação da saída devem corresponder exatamente ao exemplo fornecido.

## Exemplo de uso:
<pre> 
Código:
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(create_spend_chart([food, clothing]))
</pre>
<pre>  
Retorno do Console:
*************Food*************
deposit                1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
Percentage spent by category
100| o     
 90| o     
 80| o     
 70| o     
 60| o     
 50| o     
 40| o     
 30| o     
 20| o     
 10| o     
  0| o  o  
    -------
     F  C  
     o  l  
     o  o  
     d  t  
        h  
        i  
        n  
        g
 </pre>






