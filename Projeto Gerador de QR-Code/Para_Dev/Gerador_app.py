import PySimpleGUIQt as sg
from os import getcwd
import qrcode

info_code = ''
name_doc = ''
cdw = getcwd()  # Retorna a URL do arquivo da imagem.
local_img = str(f'{cdw}/Seu_QR-code/{name_doc}.png')
sg.theme('DarkGreen4')
icone = './img/favicon.ico'

def janela1():
	tela1 = [
		[sg.Text('Digite uma informação a ser codificada: ')],
        [sg.InputText()],
        [sg.Text('Digite um nome para o arquivo: ')],
        [sg.InputText()],
        [sg.Image('./img/img_banner.png')],
        [sg.Button('Gerar'),sg.Button('Sair')]]
	return sg.Window('Gerador de QR-Code', icon=(icone), size=(280, 380), layout=tela1)

def janela2():
	tela2 = [
		[sg.Text(f'Seu arquivo: {values[1]}.png .')],
    	[sg.Image(f'./Seu_QR-Code/{values[1]}.png')],
    	[sg.Text('O arquivo foi salvo na pasta Seu_QR-Code !')],
    	[sg.Button('Voltar'), sg.Button('Sair')]]
	return sg.Window('Gerador de QR-Code', icon=(icone), size=(280, 380), layout=tela2)

janela = janela1()

def gerar():
    info_code = values[0]
    name_doc = values[1]
    img = qrcode.make(info_code)
    type(img)
    img.save(f'./Seu_QR-Code/{name_doc}.png')


while True:
	event, values = janela.read()
	if event == 'Gerar' and (len(values[0]) == 0 or len(values[1]) == 0):
		sg.popup('PRECISA INSERIR UM TEXTO A SER CODIFICADO E UM NOME PARA O ARQUIVO!', title="ATENÇÃO", icon=(icone))
	
	elif event == 'Gerar' and (len(values[0]) > 0 and len(values[1]) > 0):
		janela = janela2()
		gerar()

	elif event == 'Voltar':
		janela.close()
		janela = janela1()

	elif event == sg.WIN_CLOSED or event == 'Sair':
		break

janela.close()
