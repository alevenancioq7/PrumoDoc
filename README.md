# 📑 PrumoDoc

** Reconhecimento de Inclinação e Correção Automática de Documentos Digitalizados (*Deskew*)**

---

## 🏛 Informações Institucionais
* **Instituição:** Universidade Federal de Rondônia (UNIR)
* **Departamento:** Faculdade de Engenharia, Tecnologia e Inovação (FAETI)
* **Curso:** Bacharelado em Ciência da Computação
* **Disciplina:** Cálculo III (DIN00018)
* **Professor:** Prof. Esp. Rodrigo Duarte de Oliveira Tolêdo
* **Projeto de Extensão:** Aplicação do Cálculo como Ferramenta Computacional
* **Linha Temática:** Processamento de Imagens e Visão Computacional

## 👥 Integrantes
* Alessandra Venancio Queiroz - Matrícula: 20241004507
* Sabrina Souza Barros - Matrícula: 20241004525

---

## Visão Geral do Projeto
A digitalização de documentos por meio de dispositivos móveis pode resultar em imagens com diferentes níveis de inclinação, situação que dificulta a leitura humana, a organização de arquivos e, principalmente, o reconhecimento óptico de caracteres (OCR). Este projeto propõe o desenvolvimento de um software para reconhecimento automático do ângulo de inclinação e correção geométrica de documentos digitalizados. Para isso, são aplicados conceitos de Cálculo, como funções de duas variáveis para representar a imagem, projeções (integrais discretizadas) e otimização de uma função objetivo para estimar o ângulo, e matriz de rotação com Jacobiano para a correção geométrica.

---

## 🧮 Conceitos de Cálculo Aplicados

### 1. Representação Matemática de Imagens
Uma imagens digital em escala de cinza pode ser representada por uma função $I(x,y)$, em que $x$ e $y$ identificam a posição do pixel e $I(x,y)$ representa sua intensidade. Em imagens binárias, os pixels podem ser representados por valores associados ao fundo e ao conteúdo do documento.

## 2. Derivadas Parciais e Gradiente
As derivadas parciais $\frac{\partial I}{\partial x}$ e $\frac{\partial I}{\partial y}$ medem a taxa de variação da intensidade em cada direção, e delas se define o gradiente:

$$\nabla I(x,y) = \left(\frac{\partial I}{\partial x}, \frac{\partial I}{\partial y}\right)$$

O gradiente aponta para a direção de maior crescimento local da função e permite associar mudanças de intensidade a bordas.

### 3. Projeção Horizontal e Função Objetivo
Para um ângulo de rotação $\theta$, a quantidade de pixels escuros em cada linha horizontal forma a projeção horizontal $P_\theta(y)$. Em uma formulação contínua, ela seria uma integral; na imagem digital, é uma soma:

$$P_\theta(y) = \sum_x B_\theta(x,y)$$

Quando o texto está alinhado, as linhas escuras e os espaços entre elas ficam bem definidos, e a projeção varia mais. Isso é medido pela variância, que define a função objetivo:

$$J(\theta) = \mathrm{Var}\left[P_\theta(y)\right]$$

A estimativa do ângulo é o valor que a maximiza:

$$\theta^* = \arg\max_{\theta} J(\theta)$$

No software, a maximização é feita por **busca discreta**: testam-se vários ângulos em um intervalo e escolhe-se o de maior $J(\theta)$. Em seguida, a busca pode ser refinada em torno do melhor ângulo.

### 4. Rotação e Transformação Geométricas
A correção é feita por uma rotação. No plano, a matriz de rotação por um ângulo $\theta$ é:

$$R(\theta)=\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}, \qquad \det R(\theta)=1$$

### 5. Discretização, Limites e Refinamento da Busca
A imagem digital e a busca angular são versões discretas de um problema contínuo. O refinamento consiste em começar com passos de $1^\circ$ e, depois de localizar a região mais promissora, repetir a busca com passos de $0{,}1^\circ$. Reduzir o passo aumenta a resolução da estimativa, mas também o número de operações. A precisão final depende da resolução da imagem, do passo angular, da limiarização, do ruído, da qualidade do texto e da presença de elementos gráficos, por isso é necessária a avaliação experimental.

---

## README EM ANDAMENTO, EM BREVE ATUALIZAÇÕES E VERSÃO FINAL
