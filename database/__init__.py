class Product:
    def __init__(self, name, loc, description):
        self.name = name
        self.loc = loc
        self.description = description


RiomartecR8 = Product('RiomartecR8', 'C:\\Users\\fellip\\PycharmProjects\\interface\\images\\RiomartecR8.jpeg',
                        'Fone De Ouvido Headphone Riomartec'
                        ' R872 na cor branca com preço promocional de R$ 55,00')

AirD2 = Product('AirD2', 'C:\\Users\\fellip\\PycharmProjects\\interface\\images\\AirD2.jpeg',
                'Fone de ouvido Xiaomi Redmi AirDots 2 wireless Bluetooth'
                ' de ótima qualidade na promoção por apenas R$ 150,00')

ADots3 = Product('ADots3', 'C:\\Users\\fellip\\PycharmProjects\\interface\\images\\ADots3.jpeg',
                 'Fone de ouvido bluetooth Xiaomi Redmi AirDots Pro 3 '
                 'AirDots de ótima qualidade com preço promocional de R$ 150,00')

Tesoura = Product('Tesoura', 'C:\\Users\\fellip\\PycharmProjects\\interface\\images\\Tesoura.jpeg', 'Tesoura R$10,00')

Sw120 = Product('Smartwatch120', 'C:\\Users\\fellip\\PycharmProjects\\interface\\images\\Sw120.jpeg',
                        'Smartwatch relógio inteligente w8 com tela colorida à prova dágua / '
                        'frequência cardíaca, monitor de batimento cardíaco,'
                        ' monitor pressão arterial, pedômetro, lembrete de chamadas,'
                        ' alarme, monitor, esportes, '
                        'lembrete sedentarismo,'
                        ' monitor do sono por um preço promocional de R$ 120,00')

BombaEletronica = Product('BombaEletronica', 'C:\\Users\\fellip\\PycharmProjects\\interface\\images\\BombaEletronica.jpeg',
                          'Bomba eletrônica de água para garrafão de '
                          'excelente qualidade na promoção imperdível por apenas R$ '
                          '45,00')

Y30 = Product('Y30', "C:\\Users\\fellip\\PycharmProjects\\interface\\images\\Y30.jpeg",
              'Novo Y30 Mini Fone De Ouvido Sem Fio 5.0 Estéreo Binaural Para '
              'Esportes Ao Ar Livre com preço promocional de lançamento por apenas R$ 75,00')

XB450 = Product('XB450', 'C:\\Users\\fellip\\PycharmProjects\\interface\\images\\XB450.jpeg',
                'Fone De Ouvido com Fio JBL Xb-450 '
                'Extra Bass Headphone na promoção por apenas R$ 65,00')
LumiLed = Product('LumiLed', 'C:\\Users\\fellip\\PycharmProjects\\interface\\images\\LumiLed.jpeg',
                  'Luminária LED, Luz Noturna, 3 LED, Sensível ao Toque, Adesiva de Parede, '
                  'Teto, armários embutidos, Piso, Sem Fio, na promoção por apenas R$ 25,00')
MagnetCharger = Product('MagnetCharger', 'C:\\Users\\fellip\\PycharmProjects\\interface\\images\\MagnetCharger.jpeg',
                        'Carregador Magnético Sem Fio indução Para '
                        'Iphone 8 Plus X Xs 11 Pro Max 12 / 12 Pro'
                        ' com preço promocional de lançamento por apenas R$ 115,00')

KTS1049A = Product('KTS1049A', 'C:\\Users\\fellip\\PycharmProjects\\interface\\images\\KTS1049A.jpeg',
                   'Caixa de Som Portátil com '
                   'Bluetooth KTS-1049A na cor preta com preço promocional de R$ 60,00')

ControleRemoto = Product('ControleRemoto', 'C:\\Users\\fellip\\PycharmProjects\\interface\\images\\ControleRemoto.jpeg',
                         'Controle remoto para tv Samsung, Philco, LG, AOC '
                         'e Panasonic com preço promocional de lançamento '
                         'por apenas R$ 35,00')

set_of_products = {RiomartecR8, XB450, ControleRemoto, KTS1049A,
                   MagnetCharger, LumiLed, Y30,
                   BombaEletronica, Sw120, Tesoura, ADots3, AirD2}
