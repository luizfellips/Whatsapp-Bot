# Automação de Envios de Mídia/Descrição por Whatsapp Web
![badge](https://img.shields.io/badge/STATUS-APRIMORANDO%20-brightgreen)

<img src ='https://user-images.githubusercontent.com/110192027/184501945-6bed82f8-aad2-464f-a012-ee3518472084.png' alt='print1' width=600>
<img src='https://user-images.githubusercontent.com/110192027/184501944-541994d4-5ad5-439f-a8f7-6e8325d9ad61.png' alt='print2' width=600>

>> Esse mini-projeto funciona utlizando a biblioteca Selenium para interação com elementos do navegador, e originalmente utilizava
classes(POO) para montar um objeto/produto com seu nome, descrição e local de armazenamento da mídia(em string).
Porém agora utiliza Pandas e planilhas Excel para armazenar seus dados.

### UTILIZANDO O PROGRAMA
- Inicialize o código e logue na sua conta do WhatsWeb com o código QR do celular
- é importante que você entre em pelo menos um grupo antes de começar os envios, para fechar banners do próprio Whatsapp que podem entrar em conflito com o funcionamento.
- No terminal aparecerá a mensagem "Continuar?", Ao apertar enter, ele irá percorrer pelos grupos listados na variável list_of_contacts e enviar todos os produtos cadastrados na database.


### COMO FUNCIONA
```
O programa abre uma nova instância do navegador do Google Chrome e redireciona automaticamente para o site do Whatsapp Web, 
onde o usuário deve logar com sua conta pelo QR code,
durante esse processo o programa estará em standby no terminal até que você esteja conectado.
.
De acordo com uma lista de grupos pré-determinada,
para cada grupo nessa lista o programa irá percorrer por um grupo de cada vez,
onde  em cada grupo ele enviará todos os produtos respeitando um tempo-limite para evitar banimento, 
e ao terminar o envio de todos produtos, irá automaticamente seguir para o próximo grupo.
.
O envio dos produtos funciona selecionando elementos interativos do navegador(CSS selector, XPATH, ID, Classes), 
enviando keys(textos ou imagens) como argumentos, onde os campos de envio serão preenchidos automaticamente e 
enviados automaticamente.
```
