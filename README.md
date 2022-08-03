# Laboratório 7 em Python: Encaixe Perfeito

Sétimo projeto para submissão em Python de MC102 (Algoritmos e Programação de Computadores), curso ministrado pela UNICAMP.

Dando continuidade aos projetos desenvolvidos nos laboratórios de MC102 (explicação no repositório [IniciandoEmPython](https://github.com/laratoledom/IniciandoEmPython/blob/main/README.md)), temos como proposta de desenvolvimento do código o seguinte problema:
_________________________________________________________________________________________________________________________________________________________________________

"O jogo de Encaixe Perfeito é bastante simples e precisamos apenas de duas peças, que podem apresentar regiões com alturas distintas. Além disso, o tamanho da peça 1 é sempre menor ou igual ao tamanho da peça 2. Por exemplo, a imagem seguinte mostra uma possibilidade de peças para o jogo de Encaixe Perfeito.

<p align="center">
  <img src="https://media.discordapp.net/attachments/1004187806345740310/1004410158476169336/2022-08-03_2.png" />
</p>

<br>
O objetivo do jogo consiste em encaixar a peça 1 sobre a peça 2, fazendo com que o espaço entre as duas peças seja o menor possível. 
A pontuação de um encaixe é dada pelos espaços vazios entre as duas peças. Por exemplo, na imagem a seguir temos quatro possibilidades (exemplos a, b, c e d) para encaixar a peça 1 sobre a peça 2. 

Note que os espaços vazios estão representados pelos quadrados em vermelho, sendo que cada quadrado vermelho no encaixe aumenta a pontuação em uma unidade. Além disso, embaixo da peça 2 temos um indicativo numérico que mostra a partir de que posição da peça 2 o encaixe da peça 1 foi realizado. Perceba que dentre as quatro possibilidades, o caso b é o que apresenta a menor pontuação com valor dois, encaixando a peça 1 a partir da posição 2 da peça 2.

<p align="center">
  <img src="https://media.discordapp.net/attachments/1004187806345740310/1004409510393299014/2022-08-03_1.png" />
  
O jogo permite ainda que a peça 1 seja invertida horizontalmente, criando novas possibilidades de encaixe na peça 2. A imagem a seguir mostra como fica a peça 1 invertida.

<p align="center">
  <img src="https://media.discordapp.net/attachments/1004187806345740310/1004412533484036106/2022-08-03_3.png" />
  
Considerando agora a peça 1 invertida, temos mais quatro possibilidades de encaixe exemplificados na imagem a seguir (exemplos a, b, c e d). Note que no exemplo d temos um encaixe perfeito encaixando a peça 1 invertida a partir da posição 4 da peça 2, que resulta na pontuação zero.
  
<p align="center">
  <img src="https://media.discordapp.net/attachments/1004187806345740310/1004412583018766467/2022-08-03_4.png" />
  
Sabendo que você é um(a) ótimo(a) programador(a), seu colega pediu para que você desenvolvesse um programa que determine qual o melhor encaixe possível, dada duas peças do jogo de Encaixe Perfeito. Seu programa receberá como entrada um número inteiro positivo N, indicando a quantidade de partidas do jogo que serão jogadas. Para cada partida, seu programa receberá duas linhas. A primeira linha apresentará P1 números inteiros positivos separados por espaços, indicando a altura em cada região da peça 1 (da esquerda para direita). Na segunda linha, seu programa receberá P2 números inteiros positivos separados por espaços, indicando a altura em cada região da peça 2 (também da esquerda para direita). A seguir, você encontrará a entrada que representa as peças 1 e 2 utilizadas no exemplo anterior, considerando que houve apenas uma partida do jogo.<br>

<b>1 <br>
3 2 1 <br>
2 1 3 3 2 1 </b><br>

Note que ao inverter a peça 1 sua representação também deve mudar. Utilizando como exemplo a peça 1 invertida, temos que sua representação passará a ser 1 2 3.
Como saída, seu programa deverá informar, para cada partida, a melhor pontuação obtida, a partir de que posição da peça 2 o encaixe da peça 1 foi realizado e se a peça 1 foi invertida ou não. Caso seja possível realizar o encaixe perfeito, ou seja, obter uma pontuação igual a zero, então a mensagem Encaixe Perfeito! também deverá ser exibida. Caso existam múltiplos encaixes que resultem na melhor pontuação, a jogada sem inverter a peça 1 tem prioridade sobre a jogada com a peça 1 invertida. Caso o empate ainda persista, então o encaixe na posição mais a esquerda na peça 2 deve ser utilizado como critério de desempate.

Caso não exista um encaixe perfeito, o padrão de impressão que deve ser seguido é:

<b>Pontuacao:</b> ~ P ~ <br>
<b>Posicao de Encaixe:</b> ~ R ~ <br>
<b>Peca 1:</b> ~ Normal|Invertida ~

Caso contrário:
  
<b>Encaixe Perfeito! <br>
Posicao de Encaixe:</b> ~ R ~ <br>
<b>Peca 1:</b> ~ Normal|Invertida ~

Onde <b>P</b>, <b>R</b> e <b>Normal|Invertida</b> representam, respectivamente, a melhor pontuação obtida, a partir de que posição da peça 2 a peça 1 foi encaixada e a forma em que a peça 1 foi encaixada (normal ou invertida)."
_______________________________________________________________________________________________________________________________________________________________________

<b>Observações:</b>
O arquivo foi executado através do PyCharm e no arquivo "testes" podem ser encontrados alguns exemplos de testes que verificam o código.
