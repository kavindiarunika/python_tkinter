import tkinter as tk
from tkinter import ttk
import pyshorteners
import pyshorteners.shorteners

root=tk.Tk()
root.title("url shorner")
root.geometry('500x500')

def shortern():
    shortner = pyshorteners.shortener()
    short_url=shortner.tinyurl.short("https://docs.python.org/3/library/index.html")
    print(short_url)


longurl_label=tk.Label(root,text="enter the long url")
longurl_entry = tk.Entry(root)
shorturl_label=tk.Label(root,text="output short url")
shorturl_entry=tk.Entry(root)
shortern_button=tk.Button(root,text="Shortern URL",command=shortern)

longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shortern_button.pack()


root.mainloop()