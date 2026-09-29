# Sistema de Automação de Cadastro de Produtos

## Sobre o Sistema
Este projeto consiste em uma solução de automação robótica de processos (RPA) desenvolvida em Python para otimizar e agilizar o cadastro de produtos em sistemas web. O script interage de forma autônoma com o ambiente operacional e interfaces web, simulando ações de digitação, navegação por teclado e cliques de mouse baseados em coordenadas de tela. 

A aplicação importa uma base de dados estruturada em formato tabular (`produtos.csv`) e realiza o preenchimento automatizado de múltiplos campos (código, marca, tipo, categoria, preço unitário, custo e observações), eliminando a necessidade de inserção manual repetitiva, reduzindo erros operacionais e aumentando expressivamente a produtividade da equipe.

---

## Bibliotecas Utilizadas
Abaixo estão listadas as bibliotecas presentes no `requirements.txt` que são ativamente utilizadas no código do notebook, acompanhadas de suas respectivas versões e links para a documentação oficial:

* [pandas](https://pandas.pydata.org/docs/) - Versão: `3.0.6` *(Biblioteca presente no requirements e utilizada no notebook)*
* [PyAutoGUI](https://pyautogui.readthedocs.io/) - Versão: `0.9.54` *(Biblioteca presente no requirements e utilizada no notebook)*
* **time** *(Módulo nativo da biblioteca padrão do Python utilizado para controle de fluxo e pausas de carregamento)*

*(Nota: As demais bibliotecas presentes no arquivo `requirements.txt` que servem como dependências internas do PyAutoGUI mas não são chamadas diretamente no código do notebook foram omitidas conforme solicitado).*

---

## Autor
* **Autor:** Moisés Santos
* **GitHub:** [IMoisasZ](https://github.com/IMoisasZ)
* **E-mail:** mopri08@gmail.com