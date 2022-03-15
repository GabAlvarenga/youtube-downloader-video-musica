import PySimpleGUI as sg
from pytube import YouTube 
class TelaPython:
    def __init__(self):
        sg.theme('DarkTeal6')
        #layout
        layout = [
            [sg.Text('Link da vídeo',size=(10,0)),sg.Input(size=(35,0),key="link")],
            [sg.Text('Diretório',size=(10,0)),sg.Input(size=(35,0),key='diretorio')],
            [sg.Button("Baixar")],
            [sg.Checkbox('Apenas áudio',key='only_audio')],
            [sg.Output(size=(45,10))]

        ]
        #janela
        self.janela = sg.Window("Baixar Video Yoytube").layout(layout)
        #extrair dados tela
        self.button, self.values = self.janela.Read()


    def Iniciar(self):
            while True:
                self.button, self.values = self.janela.Read()
                if self.button in (sg.WIN_CLOSED, 'Exit'):
                    break
                link = self.values["link"]
                diretorio = self.values["diretorio"]
                print(f"Link: {link}")
                print(f"Salvando Video em:{diretorio}")
                try:
                    SAVE_PATH = diretorio
                    yt = YouTube(link)
                    if self.values["only_audio"] == True:
                        mp4files = yt.streams.filter(only_audio=True).order_by('abr')
                        Q=mp4files[-2].itag
                    else:
                        mp4files = yt.streams.filter(progressive=True).order_by('resolution')
                        Q = mp4files[-1].itag
                    stream = yt.streams.get_by_itag(Q)
                    stream.download(SAVE_PATH)
                except:
                    print("ERRO :c")                 
                    
tela = TelaPython()
tela.Iniciar() 