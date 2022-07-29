# Automação de Envios de Mídia/Descrição por Whatsapp Web
![badge](https://img.shields.io/badge/STATUS-EM%20DESENVOLVIMENTO-brightgreen)

>> Esse mini-projeto funciona utlizando a biblioteca Selenium para interação com elementos do navegador e
utlização de classes(POO) para montar um objeto/produto com seu nome, descrição e local de armazenamento da mídia(em string).

### UTILIZANDO O PROGRAMA
- Inicialize o código e logue na sua conta do WhatsWeb com o código QR do celular
- é importante que você entre em pelo menos um grupo antes de começar os envios, para fechar banners do próprio Whatsapp que podem entrar em conflito com o funcionamento.
- No terminal aparecerá a mensagem "Continuar?", Ao apertar enter, ele irá percorrer pelos grupos listados na variável list_of_contacts e enviar todos os produtos cadastrados na database.


### COMO FUNCIONA
```
O programa abre uma nova instância do navegador do Google Chrome e redireciona automaticamente para o site do Whatsapp Web, onde o usuário deve logar com sua conta pelo QR code, durante esse processo o programa estará em standby no terminal até que você esteja conectado.
De acordo com uma lista de grupos pré-determinada, para cada grupo nessa lista o programa irá percorrer por um grupo de cada vez, onde  em cada grupo ele enviará todos os produtos respeitando um tempo-limite para evitar banimento, e ao terminar o envio de todos produtos, irá automaticamente seguir para o próximo grupo.
O envio dos produtos funciona selecionando elementos interativos do navegador(CSS selector, XPATH, ID, Classes), enviando keys(textos ou imagens) como argumentos, onde os campos de envio serão preenchidos automaticamente e enviados automaticamente.
```
