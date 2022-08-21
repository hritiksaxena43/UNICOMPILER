from tkinter import *
from pytube import YouTube 

# Designing the page

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('YouTube downloader')



# Link

Label(root, text="Download Youtube videos for free", font='san-serif 14 bold').pack()
link = StringVar() # Specifying the variable type
# resolution = StringVar()
Label(root, text="Paste your link here", font='san-serif 15 bold').place(x=150, y=55)
link_enter = Entry(root, width=70, textvariable=link).place(x=30, y=85)
# Label(root,text="Please Enter Resolution", font="san-serif 15 bold").place(x=150,y=130)
# Resolution_enter = Entry(root, width=70, textvariable=resolution).place(x=30, y=160)


def download():
    url = YouTube(str(link.get())) 
    video = url.streams.get_highest_resolution().download()
    # video.download() 
    Label(root, text="Downloaded", font="arial 15").place(x=100, y=250) 




Button(root, text='Download', font='san-serif 16 bold', bg='red', padx=2, command=download).place(x=100, y=190)

root.mainloop()
