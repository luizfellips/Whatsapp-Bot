# Automação de Envios de Mídia/Descrição por Whatsapp Web
![badge](https://img.shields.io/badge/STATUS-APRIMORANDO%20-brightgreen)

<img src ='https://user-images.githubusercontent.com/110192027/184501945-6bed82f8-aad2-464f-a012-ee3518472084.png' alt='print1' width=600>
<img src='https://user-images.githubusercontent.com/110192027/184501944-541994d4-5ad5-439f-a8f7-6e8325d9ad61.png' alt='print2' width=600>

>> Esse mini-projeto funciona utlizando a biblioteca Selenium para interação com elementos do navegador, e originalmente utilizava
classes(POO) para montar um objeto/produto com seu nome, descrição e local de armazenamento da mídia(em string).
Porém agora utiliza Pandas e planilhas Excel para armazenar seus dados.

### UTILIZANDO O PROGRAMA
- Inicialize o interface.py
- Nesta interface você pode adicionar produtos, onde insere a descrição no campo DESCRIPTION, preço no campo PRICE, e procura pela imagem a ser carregada no campo File. Ao adicionar, o produto é automaticamente inserido na planilha products.xlsx.
- Você também pode adicionar contatos, inserindo seu nome exato e adicionando. São inseridos na planilha contatos.xlsx
- Ao clicar em Load(Load Driver), uma nova instância do Google Chrome será inicializada e você precisará conectar na sua conta do Whatsapp Web pelo QR Code.
- Entre em ao menos um grupo que possua mensagens temporárias para remover o aviso, para não conflictar com o algoritmo do robô na hora dos envios.
- Por fim, basta clicar em Start Program, e manter a janela do Whatsapp sempre na frente, para não causar erros.
- Todos os produtos cadastrados serão enviados para cada grupo cadastrado.


