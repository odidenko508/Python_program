from tkinter import *
from tkinter.messagebox import *

#створення графічного вікна
Window = Tk()
Window.title("Зоопарк")
Window.geometry("400x440+150+150")

#створення графічного полотна
canvas = Canvas(Window)
canvas.place(x=160, y=20, width=220, height=220)


#обробники подій наведення курсору миші на написи
def L1_mot(event):
    global img
    img = PhotoImage(file='giraffe.png')
    canvas.create_image(0, 0, anchor=NW, image=img)


def L2_mot(event):
    global img
    img = PhotoImage(file='zebra.png')
    canvas.create_image(0, 0, anchor=NW, image=img)


def L3_mot(event):
    global img
    img = PhotoImage(file='lev.png')
    canvas.create_image(0, 0, anchor=NW, image=img)


def L4_mot(event):
    global img
    img = PhotoImage(file='begemot.png')
    canvas.create_image(0, 0, anchor=NW, image=img)


#обробники подій  клацанням лівої кнопки миші на написах
def L1_click(event):
    info = showinfo(
        "Інформація про жирафу",
        'Жира́фа — рід ссавців із родини жирафових. Це найвища наземна тварина на планеті. Щоб відрізнити від родича — окапі («лісової жирафи») — жирафу часом називають «степовою жирафою»'
    )


def L2_click(event):
    info = showinfo(
        "Інформація про зебру",
        'Зе́бра — позатаксаномічна група коней, що складається з двох підродів. До підроду Hippotigris входять такі види, як гірська зебра і зебра Бурчелла, а до підроду Dolichohippus відноситься пустельна зебра.'
    )


def L3_click(event):
    info = showinfo(
        "Інформація про лева",
        'Лев або пантера лев (Panthera leo) — вид хижих ссавців з роду пантер родини котових. Це другий за величиною вид родини після тигра.'
    )


def L4_click(event):
    info = showinfo(
        "Інформація про бегемота",
        'Бегемо́т, гіпопотам  — рід наземноводяних ссавців з родини бегемотових  ряду оленеподібних.Бегемотів відносять до групи «нежуйних» «парнокопитних» ссавців.'
    )


#написи
L1 = Label(text="Жирафа",
           width=9,
           justify=CENTER,
           font="Arial 16",
           bg="#287a1a")
L1.place(x=20, y=20)
L1.bind('<Motion>', L1_mot)
L1.bind('<Button-1>', L1_click)

L2 = Label(text="Зебра",
           width=9,
           justify=CENTER,
           font="Arial 16",
           bg="#287a1a")
L2.place(x=20, y=60)
L2.bind('<Motion>', L2_mot)
L2.bind('<Button-1>', L2_click)

L3 = Label(text="Лев", width=9, justify=CENTER, font="Arial 16", bg="#287a1a")
L3.place(x=20, y=100)
L3.bind('<Motion>', L3_mot)
L3.bind('<Button-1>', L3_click)

L4 = Label(text="Бегемот",
           width=9,
           justify=CENTER,
           font="Arial 16",
           bg="#287a1a")
L4.place(x=20, y=140)
L4.bind('<Motion>', L4_mot)
L4.bind('<Button-1>', L4_click)



mainloop()


