from tkinter import *
import pyshorteners
def convert():
    s = pyshorteners.Shortener().tinyurl.short(url.get())
    shorturl.set(s)
root = Tk()
Label(root, text="URL Shortner", bg="orange", fg="white", font="verdana 22 ").place(x=80, y=10)
root.title(" URL Shortner")
root.geometry("1000x1000")
root.config(background="orange")
url = StringVar()
shorturl = StringVar()
Label(root, text="Enter URL Here ").place(x=7, y=100)
Entry(root, textvariable=url).place(x=7, y=120)
Button(root, text="Convert to shortened", command=convert).place(x=7, y=180)
Label(root, text="Shortened URL" ).place(x=7, y=250)
Entry(root, textvariable=shorturl, width=35, font="verdana 12").place(x=7, y=270)
root.mainloop()