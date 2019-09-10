# -*- coding: utf8 -*-
from tkinter import *
import tkinter.filedialog as fd
from PIL import Image, ImageDraw, ImageTk

from tkinter import messagebox

class MainWindow(Frame, object):

    def __init__(self, master):
        super(MainWindow, self).__init__(master)
        # Frame, на котором размещаем Canvas для возможности его удаления
        self.canvasFrame = None
        self.pack()
        self.placeMenu()

    def placeMenu(self):
        m = Menu(self.master)
        self.master.config(menu=m)
        fm = Menu(m, tearoff=0)
        m.add_cascade(label=u"Меню", menu=fm)
        fm.add_command(label=u"Открыть", command=self.openPicture)
        #fm.add_command(label=u"Построить график", command=self.printChart)
        fm.add_command(label=u"Выход", command=self.close)
        fm.add_command(label=u"Сохранить", command=self.save)
        hm = Menu(m, tearoff=0)
        m.add_cascade(label=u"Помощь", menu=hm)
        hm.add_command(label=u"Справка", command=self.information)

    def information(self):
        messagebox.showinfo("Справка", "Данная программа позволяет работать с изображениями. ")
                            #+ "Необходимо выбрать нужное действие в 'Меню':\n"
                            #+ "можно открыть изображение или построить график, выбрав соответствующие пункты.")

    def openPicture(self):
     # Открываем файловый диалог
        filename = fd.askopenfilename()
        # если файл открыли
        if filename != "":
            # проверяем, что рамка размещена на экране
            if not self.canvasFrame is None:
                # если она размещена, то удаляем рамку с канвасом на ней
                self.canvasFrame.destroy()
                # обнуляем ссылку на рамку
                self.canvasFrame = None
            # Заново создаем пустую рамку
            self.canvasWidth = 800
            self.canvasHeight = 800

            self.canvasFrame = Frame(self, width=self.canvasWidth, height=self.canvasHeight, background='blue')
            self.canvasFrame.pack(side=LEFT)

            self.btnFrame = Frame(self, width=100, height=self.canvasHeight, background='black')
            self.btnFrame.pack(side=LEFT)

            # помещаем на неё канвас
            self.canvas = Canvas(self.canvasFrame, width=self.canvasWidth, height=self.canvasHeight)
            self.canvas.pack()
             # создаем изображение
            self.imgObject = self.canvas.create_image(0, 0)

            try:
                # считываем картинку из файла в массив байтов
                self.src = Image.open(filename)


                self.pix = self.src.load()
                 # подгоняем её под нужный размер
                self.src.thumbnail((1000, 1000))
                 # переводим картинку из массива байтов в изображение
                self.img = ImageTk.PhotoImage(self.src)
                # # рисуем изображение на канвасе
                self.canvas.itemconfigure(self.imgObject, image=self.img, anchor="nw")

                # #########################
                self.wdth = self.src.size[0]  # Определяем ширину.
                self.hght = self.src.size[1]  # Определяем высоту.

                self.btn1 = Button(self.btnFrame, text="ЧБ", font="35", background='green',command=lambda: self.bwFilter())

                self.btn2 = Button(self.btnFrame, text="del", font="35", background='yellow', command=lambda: self.delF())
                self.btn3 = Button(self.btnFrame, text="del", font="35", background='red',
                                   command=lambda: self.sepia())
                #self.btn1["command"] = self.bwFilter()
            except IOError:
                print("Incorrect file")

            self.btn1.pack(side=TOP)
            self.btn2.pack(side=TOP)
            self.btn3.pack(side=TOP)

    def delF(self):
        #draw = ImageDraw.Draw(self.src)
        self.img = self.copy
        self.canvas.itemconfigure(self.imgObject, image=self.img, anchor="nw")
    #-----------------------
    def bwFilter(self):
        self.copy=self.src
        draw = ImageDraw.Draw(self.src)
        pix = self.src.load()


        self.wdth = self.src.size[0]  # Определяем ширину.
        self.hght = self.src.size[1]  # Определяем высоту.
        for i in range(self.wdth):
            for j in range(self.hght):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                draw.point((i, j), (S, S, S))
        self.img = ImageTk.PhotoImage(self.src)
        self.canvas.itemconfigure(self.imgObject, image=self.img, anchor="nw")

    def save(self):
        self.src.save("answer.jpg", "JPEG")

    def sepia(self):
        depth = 40
        self.copy = self.src
        draw = ImageDraw.Draw(self.src)
        pix = self.src.load()

        self.wdth = self.src.size[0]  # Определяем ширину.
        self.hght = self.src.size[1]  # Определяем высоту.
        for i in range(self.wdth):
            for j in range(self.hght):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                a = S + depth * 2
                b = S + depth
                c = S
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))
        self.img = ImageTk.PhotoImage(self.src)
        self.canvas.itemconfigure(self.imgObject, image=self.img, anchor="nw")
        #self.canvas.itemconfigure(self.imgObject, image=ImageTk.PhotoImage(self.src), anchor="nw")
    #-----------------











    # закрыть окно
    def close(self):
       self.master.destroy()





if __name__ == "__main__":
    window = Tk()
    window.title("PhotoFiltersbyNovikovaAnastasia")
    window.geometry("1000x1000")
    app = MainWindow(window)
    window.mainloop()
