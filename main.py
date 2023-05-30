from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Rectangle, Line, Ellipse, Color
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.properties  import NumericProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import json

from unidecode import unidecode
from string import ascii_lowercase


# Configura um tamanho minimo para a janela.
Window.minimum_width, Window.minimum_height = (400, 500)
del(Window)


global_dificudade = ''
pontos_ganhados = 0
resutado = 'derrota'
texto_final = list()

   


try:
    with open("pontos.json",'r')as file:
        pontos_totais = json.load(file)

except FileNotFoundError:
    with open("pontos.json",'w')as file:
        pontos_totais = 0
        json.dump(0,file)
        
class Gerenciador(ScreenManager):
    def celetor(self, dificudade):  # responsavel pela celecão da dificudade
        global global_dificudade
        global_dificudade = dificudade


class Tela_Finalizacao(Screen):  # cria a tela do final do jogo
    lista_desenho = list()
    pontos = NumericProperty(0)
    lista_letras = list()
    spaco_padrao = 20
    
    def on_size(self, *args):
        self.desenhor()
        self.removedor_widget()
        
    def on_enter(self, *args):
        global pontos_ganhados, pontos_totais
        self.desenhor()
        self.removedor_widget()
        if pontos_ganhados < 1 and resutado == 'vitoria':
            pontos_ganhados = 1
        elif resutado == 'derrota':
            pontos_ganhados = 0
        self.pontos = pontos_ganhados
        pontos_totais += pontos_ganhados
        
        with open("pontos.json",'w')as file:
            json.dump(pontos_totais,file)
        
    def removedor_widget(self,*args):
        if len(self.lista_letras) == 1:
            self.remove_widget(self.lista_letras[0])
            
        elif len(self.lista_letras) > 1:
            for letra in self.lista_letras:
                self.remove_widget(letra)
                
        self.lista_letras.clear()
                  
        if resutado == 'derrota':
            for pos, letra in enumerate(texto_final[1]):
                if texto_final[0][pos] not in  ' .-_':
                    self.lista_letras.append(Label(text=letra, pos=((self.spaco_padrao * .45 + pos * self.spaco_padrao) - (len(texto_final[1]) / 2 * self.spaco_padrao), 12 + self.spaco_padrao * .75 / 2),
                                            font_size = self.spaco_padrao *.75 ))
            
                    self.add_widget(self.lista_letras[-1])
                elif texto_final[0][pos] == ' ' and letra != ' ':
                    self.lista_letras.append(Label(text=letra, pos=((self.spaco_padrao * .45 + pos * self.spaco_padrao) - (len(texto_final[1]) / 2 * self.spaco_padrao), 12 + self.spaco_padrao * .75 / 2),
                                            font_size = self.spaco_padrao *.75 , color=(1,0,0,1)))
                    self.add_widget(self.lista_letras[-1])
                    
                else:
                    self.lista_letras.append(Label(text=letra, pos=((self.spaco_padrao * .45 + pos * self.spaco_padrao) - (len(texto_final[1]) / 2 * self.spaco_padrao), 12 + self.spaco_padrao * .75 / 2),
                                            font_size = self.spaco_padrao *.75 ))
                    self.add_widget(self.lista_letras[-1])
        else:
            for pos, letra in enumerate(texto_final[1]):
                if texto_final[0][pos] not in  ' .-_':
                    self.lista_letras.append(Label(text=letra, pos=((self.spaco_padrao * .45 + pos * self.spaco_padrao) - (len(texto_final[1]) / 2 * self.spaco_padrao), 12 + self.spaco_padrao * .75 / 2),
                                            font_size = self.spaco_padrao *.75 ))
            
                    self.add_widget(self.lista_letras[-1])
                    
                else:
                    self.lista_letras.append(Label(text=letra, pos=((self.spaco_padrao * .45 + pos * self.spaco_padrao) - (len(texto_final[1]) / 2 * self.spaco_padrao), 12 + self.spaco_padrao * .75 / 2),
                                            font_size = self.spaco_padrao *.75 ))
                    self.add_widget(self.lista_letras[-1])
    def desenhor(self, *args):
        
        width = self.width * .20   
        # Se a 20% da largura for maior que o 20% da altura então a largura sera igual a 20% da altura
        if width > self.height/5: 
            width = self.height/5
        
        with self.canvas:
            if len(self.lista_desenho) > 1:
                for obijato in self.lista_desenho:
                    self.canvas.remove(obijato)
                    
                self.lista_desenho.clear()
                
            
            
            
            if resutado == 'derrota':
                                
            # desenhar a forca 
                 # Vigar vertical
                self.lista_desenho.append(
                    Rectangle(pos=(20, self.height/2 + 60), size=(5, self.height/5))) 
                
                # Vigar horizontal 
                self.lista_desenho.append(Rectangle(pos=(10, self.height/2 + 60 + self.height/5), size=(width - 10, 5)))  
                
                # Vigar tras versal
                self.lista_desenho.append(Line(points=(
                    35, self.height/2 + 60 + self.height/5, 25,  self.height/2 + 50 + self.height/5), width=2)) 
                
                # Base 
                self.lista_desenho.append(Rectangle(pos=(10, self.height/2 + 55), size=(30,5)))
                
            # Cabeca do boneco 
                self.lista_desenho.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +60 - width * .30 + self.height /5,
                                                        width *.75 + width * .25 / 2, self.height/2 + 60 + self.height/5)))
                self.lista_desenho.append(Ellipse(pos=(width *.75, self.height /2 +60 - width * .30 + self.height /5) ,size=(width * .25, width * .25)))
                Color(rgba=(0,0,0,1))
                self.lista_desenho.append(Ellipse(pos = (width *.78, self.height /2 + 63 - width * .30 + self.height /5) ,size=(width * .19, width * .19)))
                Color(rgba=(1,1,1,1))
                
            # Coluna do boneco 
                self.lista_desenho.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +60 - width * .30 + self.height /5,
                                                                width *.75 + width * .25 / 2, self.height /2 +30 - width * .30 + self.height /5), width=2))
            
            # Desenhar o braso esquerdo do boneco                                         width *.75 + width * .25 / 2, self.height /2 +30 - width * .30 + self.height /5), width=2))
                self.lista_desenho.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +60 - width * .30 + self.height /5,
                                                            width *.75 + width * .25 / 2 - 10, self.height /2 +30 - width * .30 + self.height /5), width=2))
            # Desenhar o braso direito do boneco
                self.lista_desenho.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +60 - width * .30 + self.height /5,
                                                            width *.75 + width * .25 / 2 + 10, self.height /2 +30 - width * .30 + self.height /5), width=2))
            # Desenhar a perna esTrueuerda do boneco
                self.lista_desenho.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +30 - width * .30 + self.height /5,
                                                            width *.75 + width * .25 / 2 - 10, self.height /2  - width * .30 + self.height /5), width=2))
            # Desenhar a perna direita do boneco 
                self.lista_desenho.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +30 - width * .30 + self.height /5,
                                                           width *.75 + width * .25 / 2 + 10, self.height /2  - width * .30 + self.height /5), width=2))
                                                         
               
                # Desenha umas barras de dicas
                for pos, letra in enumerate(texto_final[1]):
                    with self.canvas:
                        if letra not in  ' .-_':
                            self.lista_desenho.append(Rectangle(pos=((self.width/2 + self.spaco_padrao * 0.35 / 2) -  len(texto_final[1]) / 2 * self.spaco_padrao + pos * self.spaco_padrao,
                            self.height/2 + 10), size=(self.spaco_padrao * .62, 2)))
                         
                
                
                        
            else:
            # Cabeca do boneco 
                self.lista_desenho.append(Ellipse(pos=(width *.79 , self.height /2 + 51  + self.height /5), size=(width * .14,width * .05)))
                self.lista_desenho.append(Ellipse(pos=(width *.72 , self.height /2 + 51  + self.height /5), size=(width * .28, 3)))
                
                self.lista_desenho.append(Ellipse(pos=(width *.75, self.height /2 +60 - width * .30 + self.height /5) ,size=(width * .25, width * .25)))
                Color(rgba=(0,0,0,1))
                self.lista_desenho.append(Ellipse(pos = (width *.78, self.height /2 + 63 - width * .30 + self.height /5) ,size=(width * .19, width * .19)))
                Color(rgba=(1,1,1,1))
                
            # Coluna do boneco 
                self.lista_desenho.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +60 - width * .30 + self.height /5,
                                                                width *.75 + width * .25 / 2, self.height /2 +30 - width * .30 + self.height /5), width=2))
            
            # Desenhar o braso esquerdo do boneco                                         width *.75 + width * .25 / 2, self.height /2 +30 - width * .30 + self.height /5), width=2))
                self.lista_desenho.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +60 - width * .30 + self.height /5,
                                                            width *.75 + width * .25 / 2 - 10, self.height /2 +30 - width * .30 + self.height /5), width=2))
            # Desenhar o braso direito do boneco
                self.lista_desenho.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +60 - width * .30 + self.height /5,
                                                            width *.75 + width * .25 / 2 + 10, self.height /2 +30 - width * .30 + self.height /5), width=2))
            # Desenhar a perna esquerda do boneco
                self.lista_desenho.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +30 - width * .30 + self.height /5,
                                                            width *.75 + width * .25 / 2 - 10, self.height /2  - width * .30 + self.height /5), width=2))
            # Desenhar a perna direita do boneco 
                self.lista_desenho.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +30 - width * .30 + self.height /5,
                                                       width *.75 + width * .25 / 2 + 10, self.height /2  - width * .30 + self.height /5), width=2))
                              
                # Desenha umas barras de dicas
                for pos, letra in enumerate(texto_final[1]):
                    with self.canvas:
                        if letra not in  ' .-_':
                            self.lista_desenho.append(Rectangle(pos=((self.width/2 + self.spaco_padrao * 0.35 / 2) -  len(texto_final[1]) / 2 * self.spaco_padrao + pos * self.spaco_padrao,
                            self.height/2 + 10), size=(self.spaco_padrao * .62, 2)))
                
class Game(Screen):
    
    lista_desafios = list()
    lista_canvas = list()
    desenho = list()
    lista_letras = list()
    boneco_canvas = list()
    letras_sertas = ' '
    spaco_padrao = 30
    
    def on_enter(self, *args):
        
        self.criador_de_lista()
        self.criador_de_desafio()
        self.forca('init')
        if self.desafio != 'erro':
            for letra in ascii_lowercase:
                self.ids[letra].disabled = False         
        

    def criador_de_lista(self, *args) -> None:  # responsavel pela leitura dos desafios
        '''ler um arquivo com o formato .txt e retona um lista
            com todas as palavras encontradas no arquivo'''
        
        try:
            with open('desafios/normal.txt', 'r') as file_n, open('desafios/dificio.txt', 'r') as file_d:
                if global_dificudade == 'n':
                    file = file_n      
                    
                else:
                    file = file_d
                  
                for palavras in file:
                    palavras = palavras.strip().upper()
                    if ':' in palavras:
                        self.lista_desafios.append(
                            [palavras.replace(':', '')])
                    else:
                        self.lista_desafios[-1].append(palavras)

        except FileNotFoundError:
            self.lista_desafios = 'erro'
            for letra in ascii_lowercase:
                self.ids[letra].disabled = True
    
    def criador_de_desafio(self, *args) -> None:
        '''sorteia o  tema e o desafio quando chamada, presisar que a lista_desafios tenha sido'''
        global texto_final, pontos_totais, pontos_ganhados
        try:
            self.desafio
            
        except AttributeError:
            pass
        from random import randint
        
        tema = self.lista_desafios[randint(0, len(self.lista_desafios)-1)]
        self.desafio = tema[randint(1, len(tema) - 1)]
        pontos_ganhados = 8
        del(randint)
            
        self.ids.tema.text = tema[0].title()
        self.letras_sertas *= len(self.desafio)
        for pos, letra in enumerate(self.desafio):
            if letra in '-_.':
                self.letras_sertas = self.letras_sertas[:pos] + letra +self.letras_sertas[pos+1:]
        texto_final.clear()
        
        self.desenhar()
    
        
        
    def desenhar(self,*args) -> None:
        
        
        if len(self.desenho) > 1:
            for i in self.desenho:
                self.canvas.remove(i)
                
        elif len(self.desenho) == 1:
            self.canvas.remove(self.desenho) 
            
        self.desenho.clear()
        
        # verifiva ser o desafio ja foi criador
        try:
            self.desafio
            
        # finalizar a execusão caso o desafio ainda não tenha cido criado
        except AttributeError: 
            return None 
        
        # configura o tamanho do spaco padrão de acordo com o tamanho do desafio
        if len(self.desafio) < 8:
            self.spaco_padrao = self.width *.4 / 8
            
        elif len(self.desafio) > 12:
            self.spaco_padrao = self.width *.7 / len(self.desafio)
            
        else:
            self.spaco_padrao = self.width *.4 / len(self.desafio)
   
        
        if len(self.lista_letras) == 1:
            self.remove_widget(self.lista_letras[0])
        
        elif len(self.lista_letras) > 1:
            for letra in self.lista_letras:
                self.remove_widget(letra)
                
        self.lista_letras.clear()
         
        # Desenha letras
        for pos, letra in enumerate(self.letras_sertas):
            if letra not in  ' .-_':
                self.lista_letras.append(Label(text=letra, pos=((self.spaco_padrao * .45 + pos * self.spaco_padrao) - (len(self.desafio) / 2 * self.spaco_padrao), 12 + self.spaco_padrao * .75 / 2),
                                                font_size = f'{self.spaco_padrao *.75}sp' ))
                self.add_widget(self.lista_letras[-1])

                
        # Desenha umas barras de dicas
        for pos, letra in enumerate(self.desafio):
            with self.canvas:
                if letra not in  ' .-_':
                    self.desenho.append(Rectangle(pos=((self.width/2 + self.spaco_padrao * 0.35 / 2) -  len(self.desafio) / 2 * self.spaco_padrao + pos * self.spaco_padrao,
                    self.height/2 + 10), size=(self.spaco_padrao * .62, 2)))
                
                
    def forca(self, errou) -> None:
        '''Responsavel por cria a forca e o boneco\n
        errou =  1-6 cria o boneco\n
        errou = init cria a forca '''
        
        global width
        if errou == 'init' and len(self.lista_canvas) >= 2:
            for canvas in self.lista_canvas:
                self.canvas.remove(canvas)
                
            self.lista_canvas.clear()

        with self.canvas:
            
            # Quadando o a fucao e inicida ou quando o tamanho da janela muda
            if errou == 'init':
                
                width = self.width * .20
                
                # Se a 20% da largura for maior que o 20% da altura então a largura sera igual a 20% da altura
                if width > self.height/5: 
                    width = self.height/5
                    
            # Cria o desenha da forca
                
                # Vigar vertical
                self.lista_canvas.append(
                    Rectangle(pos=(20, self.height/2 + 60), size=(5, self.height/5))) 
                
                # Vigar horizontal 
                self.lista_canvas.append(Rectangle(
                    pos=(10, self.height/2 + 60 + self.height/5), size=(width - 10, 5)))  
                
                # Vigar tras versal
                self.lista_canvas.append(Line(points=(
                    35, self.height/2 + 60 + self.height/5, 25,  self.height/2 + 50 + self.height/5), width=2)) 
                
                # Base 
                self.lista_canvas.append(Rectangle(pos=(10, self.height/2 + 55), size=(30,5)))
                
                errou = len(self.boneco_canvas) 
               
        # Desenha pedacos do boneco quando o jogador erra
        
            if errou > 0:
                if len(self.boneco_canvas) > 1:
                    
                    # Apagar todos o pedacos do boneco
                    for iten in self.boneco_canvas:
                        self.canvas.remove(iten)
                    self.boneco_canvas.clear()
                    
                for numero in range(0, errou):
                    
                    # Desenhar a corda e a cabeça do boneco 
                    if numero == 0:
                        self.boneco_canvas.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +60 - width * .30 + self.height /5,
                                                               width *.75 + width * .25 / 2, self.height/2 + 60 + self.height/5)))
                        self.boneco_canvas.append(Ellipse(pos=(width *.75, self.height /2 +60 - width * .30 + self.height /5) ,size=(width * .25, width * .25)))
                        Color(rgba=(0,0,0,1))
                        self.boneco_canvas.append(Ellipse(pos = (width *.78, self.height /2 + 63 - width * .30 + self.height /5) ,size=(width * .19, width * .19)))
                        Color(rgba=(1,1,1,1))
                    # Desenhar a coluna do boneco
                    elif numero == 3:
                        self.boneco_canvas.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +60 - width * .30 + self.height /5,
                                                            width *.75 + width * .25 / 2, self.height /2 +30 - width * .30 + self.height /5), width=2))
                    # Desenhar o braso esquerdo do boneco
                    elif numero == 4:
                        self.boneco_canvas.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +60 - width * .30 + self.height /5,
                                                            width *.75 + width * .25 / 2 - 10, self.height /2 +30 - width * .30 + self.height /5), width=2))
                    # Desenhar o braso direito do boneco
                    elif numero == 5:
                        self.boneco_canvas.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +60 - width * .30 + self.height /5,
                                                            width *.75 + width * .25 / 2 + 10, self.height /2 +30 - width * .30 + self.height /5), width=2))
                    # Desenhar a perna esquerda do boneco
                    elif numero == 6:
                        self.boneco_canvas.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +30 - width * .30 + self.height /5,
                                                            width *.75 + width * .25 / 2 - 10, self.height /2  - width * .30 + self.height /5), width=2))
                    # Desenhar a perna direita do boneco 
                    elif numero == 7:
                        self.boneco_canvas.append(Line(points=(width *.75 + width * .25 / 2, self.height /2 +30 - width * .30 + self.height /5,
                                                            width *.75 + width * .25 / 2 + 10, self.height /2  - width * .30 + self.height /5), width=2))
                        self.reboot()

    def techado(self, key) -> None:
        key_errada = True
        
        for pos, letra in enumerate(self.desafio):
            if key == unidecode(letra):
                self.lista_letras.append(Label(text=letra, pos=((self.spaco_padrao * .45 + pos * self.spaco_padrao) - (len(self.desafio) / 2 * self.spaco_padrao), 12 + self.spaco_padrao * .75 / 2),
                                                font_size = f'{self.spaco_padrao *.75}sp' ))
                self.add_widget(self.lista_letras[-1])
                self.letras_sertas = self.letras_sertas[:pos] + letra +self.letras_sertas[pos+1:]
                key_errada = False
                
        if self.letras_sertas == self.desafio:
            self.reboot()
            
        elif key_errada:
            self.forca(len(self.boneco_canvas) + 1) 
    def dica(self, *args): 
        global pop, layout, label
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text=f'você tem {pontos_totais} pontos' ))
        layout.add_widget(Button(text='uma letra (6 pontos)',font_size='12sp', on_press=self.revelar_letras))
        label = Label()
        
        layout.add_widget(label)

        pop = Popup(title='Dicas', content=layout, pos=(self.width , self.height), size_hint=(.35, .35), pos_hint={'right': 1,'top': 0.9})
        pop.open()
        return pop
    def revelar_letras(self, *args):
        global pontos_ganhados, pop, layout, label, pontos_totais
        if pontos_totais >= 6:
            pontos_totais -= 6
            pontos_ganhados -= 3
            letras_sortear = ''
            
            from random import choice
            for pos,letra in enumerate(self.desafio):
                if letra != ' ' and self.letras_sertas[pos] == ' ':
                    letras_sortear += letra
            letra_sorteada = choice(letras_sortear)
            self.techado(letra_sorteada)
            self.ids[unidecode(letra_sorteada.lower())].disabled = True
            pop.dismiss()
            del(choice)
            del(pop)
        else:
            label.text=f'falta {6 - pontos_totais } pontos'
            
    def reboot(self,*args):
        global resutado, texto_final, pontos_ganhados
        if len(self.boneco_canvas) >= 8:
            resutado = 'derrota'
        else:
            resutado = 'vitoria'   
            
        if len(self.boneco_canvas) > 1:
            for canvas in self.boneco_canvas:
                self.canvas.remove(canvas)
        pontos_ganhados -= len(self.boneco_canvas) 
        self.boneco_canvas.clear()
        texto_final.append(self.letras_sertas)
        texto_final.append(self.desafio)
        self.letras_sertas = ' '
        
        App.get_running_app().root.current = 'tela_final' 
        
    def on_size(self, *args):
        
        self.desenhar()
        self.forca('init')


class TelaApp(App):
    pass


TelaApp().run()
