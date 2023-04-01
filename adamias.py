import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
import tkinter.filedialog
import os
from PIL import Image, ImageTk
from adamAsmaca import *
from gameSettings import gameSet, ImStates, openPic, my_about

class Menu(ttk.Frame):

    def __init__(self, container, options={'padx' : 5, 'pady': 5}, texts="Helvetica 20"):
        super().__init__(container)
        self.container=container
        self.options = options
        self.allWords = []
        self.texts = texts
        self.xSize, self.ySize = gameSet['geometry'].split('x')
        self.startMenu()
        self.pack(fill='both')

    def startMenu(self):
        self.image, (w,h) = openPic("adamas.png")
        mainPic = tk.Canvas(self, width=w, height=h)
        mainPic.pack(fill='both', anchor='center')
        mainPic.create_image(int(self.xSize)/2 ,int(self.ySize)/2+200, image=self.image)

        startButton = ttk.Button(self, width = 20, text="oyun gir", command=lambda: self.change_frame('gameScreen'))
        startButton.pack(anchor='center', **self.options)

        self.settingsButton = ttk.Button(self, width = 20, text="ayarlar", command=self.SetDialog)
        self.settingsButton.pack(anchor='center', **self.options)

        wordListButton = ttk.Button(self, width=20, text='kelime listesi ekle', command=self.addWordList)
        wordListButton.pack(anchor='center', **self.options)

        aboutTextButton = ttk.Button(self, width=20, text='Hakkımda', command=self.About)
        aboutTextButton.pack(anchor='center', **self.options)

        extButton = ttk.Button(self, width=20, text='çıkış', command=self.destroy)
        extButton.pack(anchor='center', **self.options)

    
    def SetDialog(self):
        self.win = tk.Toplevel(self)
        self.win.grab_set()
        self.win.geometry('450x300')
        Label = ttk.Label(self.win, text="ayarları bozmak tehlikelidir setting dosyasının yedeğini alın")
        Label.pack()

        labels = [i for i in gameSet.keys()]
        for i in labels:
            Label = ttk.Label(self.win, text=i+': '+gameSet[i])
            Label.pack()
    
    def About(self):
        self.win = tk.Toplevel(self)
        self.win.grab_set()
        self.win.geometry('500x800')

        lbl = ttk.Label(self.win, text=my_about)
        lbl.pack(fill='both', expand=True)
    
    def setCh(self):
        print(self.entry.get())

    def change_frame(self, name):

        self.frames = {'gameScreen' : GameScreen(self.container, self.options, self.texts)}

        frame = self.frames[name]
        frame.setWordList(self.allWords)
        frame.pack(fill='both')
        self.destroy()
        frame.tkraise()

    def addWordList(self):
        try:
            wordFiles = tk.filedialog.askopenfile(mode='r')
            self.allWords = load_words(wordFiles)

        except:
            showerror("hata", "hatalı dosya formatı")


class GameScreen(ttk.Frame):
    def __init__(self, container, options, texts):
        super().__init__(container)
        self.container = container
        self.options = options
        self.texts = texts
        self.txt = ""
        self.WordList=None
        self.screet_word=""
        self.rights = gameSet['rights'] #6
        self.warning_rights = gameSet['warning_rights'] #3
        self.rest_chars = ""
        self.used_chars = ""
        self.startGame()

    def setWordList(self,wrdlist):
        self.WordList = wrdlist

    def startGame(self):
        self.restChars = ttk.Label(self, text="kalan harfler", background='red')
        self.restChars.grid(row=0,column=0,**self.options)

        self.usedChars = ttk.Label(self, text='kullanılan harfler', background='blue')
        self.usedChars.grid(row=1, column=0, **self.options)

        self.wordCount = ttk.Label(self, text="harf sayısı")
        self.wordCount.grid(row=0,column=1, **self.options)

        self.temp, (w,h) = openPic('adamas.png')
        self.StateIm = tk.Canvas(self, width=w, height=h)
        self.StateIm.grid(row=1, column=1, **self.options)
        self.StateIm.create_image(int(gameSet['sizeX'])/2,int(gameSet['sizeY'])/2, image=self.temp)

        self.temp_txt = tk.StringVar()
        self.charPred = ttk.Entry(self, textvariable=self.temp_txt)
        self.charPred.grid(row=2, column=1, **self.options)


        self.styleB = ttk.Style(self)
        self.confirmButton = ttk.Button(self, text="onayla", command=self.takePredict)
        #self.confirmButton.bind('<Return>',self.takePredict)
        self.confirmButton.grid(row=3, column=1, **self.options)
        

        self.restRight = ttk.Label(self, text='kalan haklar', background='green')
        self.restRight.grid(row=0, column=4, **self.options)

        self.PreWords = ttk.LabelFrame(self, text='olası eşleşmeler')
        self.PreWords.grid(row=2, column=4, **self.options)

        self.words = ttk.Label(self.PreWords, text='kelimeler')
        self.words.pack(fill='both')

        self.showWord = ttk.Label(self, text='kelime', background='blue')
        self.showWord.grid(row=3, column=4, **self.options)

        self.point = ttk.Label(self, text='puan', background='blue')
        self.point.grid(row=4, column=4, **self.options)

        self.backMenu = ttk.Button(self, text='menüye dön', command=self.change_frame)
        self.backMenu.grid(row=5, column=4, **self.options)

        self.gameStarted()


    def takePredict(self):

        if int(self.warning_rights) == 0:
            self.rights = str(int(self.rights)-1)
            self.warning_rights = gameSet['warning_rights']
            self.update()

        expr = self.temp_txt.get()
        for i in expr:
            if i not in list(string.ascii_lowercase):
                showinfo("dikkat", f"yanlış bir ifade girildi kalan uyarı hakkı {self.warning_rights}")
                self.warning_rights = str(int(self.warning_rights)-1)
                break
        
        if len(expr) > 1:
            self.rights = str(int(self.rights)-int(gameSet['wrong_vowels']))
            showinfo("tahmin","tahmin yanlış")
            self.rights = str(0)       
        
        if expr in list(self.used_chars):
            showinfo("tahmin","bunu zaten tahmin ettin")
            return

               
        if expr not in list(self.screet_word):
            if expr in ['a','e','i','o','u']:
                self.rights = str(int(self.rights)-int(gameSet['wrong_vowels']))
            else:
                self.rights = str(int(self.rights)-int(gameSet['wrong_chars']))

        self.used_chars += expr
        self.rest_chars = get_available_letters(self.used_chars)


        self.isWin()
        self.charPred.delete(0,tk.END)
        self.update()

#------------------------------------------------------------------------------------------------
    def gameStarted(self):

        if self.WordList is None:
            #self.WordList = load_words()
            self.WordList = ["bedir"]
        
        self.screet_word = choose_word(self.WordList)
        self.rest_chars = get_available_letters(self.used_chars)

        self.update()


    def set_Values(self, stringexp):
        res = ""
        for i in set(stringexp):
            res += i
        return res

    def change_frame(self):
        frame = Menu(self.container, self.options, self.texts)
        self.destroy()
        frame.tkraise()


    def update(self):
        self.wordCount['text'] = f"harf sayısı : {str(len(self.screet_word))}"
        self.restChars['text'] = "kalan harfler: "+self.set_Values(self.rest_chars)
        self.restRight['text'] = "kalan haklar: "+self.rights
        self.usedChars['text'] = "kullanılan harfler: "+self.set_Values(self.used_chars)
        self.showWord['text'] = get_guessed_word(self.screet_word, self.used_chars)
        self.point['text'] = "puanın: "+str(point_calculate(self.screet_word, self.rights))


    def isWin(self):
        
        length = 0
        for i in str(get_guessed_word(self.screet_word, self.used_chars)):
            if i != ' _ ':
                length += 1
 
        if length == len(self.screet_word) :
            showinfo("sistem", "Tebrikler! kazandın puanın: "+
                    str(point_calculate(self.screet_word, self.rights))
                    +"\ngizli kelime "+self.screet_word)
        
        if int(self.rights) <= 0:
            showinfo("sistem", "oyunu kaybettiniz puanınız :"+
                        str(point_calculate(self.screet_word, self.rights))
                        +"\ngizli kelime: "+self.screet_word)


            self.change_frame()


#|----------------------------------------------------------------------------------------------

class SetScreen(ttk.Frame):
    def __init__(self, container, options, texts):
        super().__init__(container)

class GameWindows(tk.Tk):
    def __init__ (self):
        super().__init__()
        self.settings()

    def settings(self):
        self.title(gameSet['title'])
        self.geometry(gameSet['geometry'])
        self.resizable(gameSet['resizableX'],gameSet['resizableY'])



if __name__ == "__main__":
    game = GameWindows()
    Menu(game)
    game.mainloop()
    