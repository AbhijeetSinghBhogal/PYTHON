import tkinter as tk
from tkinter import font
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

# Conda environment "env_pypdf2"

root = tk.Tk()
root.title('PDF Extract')
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open('/Users/abhijeetsingh/PYTHON/PDF Extract/logo.png')
logo = ImageTk.PhotoImage(logo)
logoLabel = tk.Label(image=logo)
logoLabel.image = logo
logoLabel.grid(column=1, row=0)

# instructions
instructions = tk.Label(root, text='Select a PDF file on your computer to extract all its text')
instructions.grid(columnspan=3, column=0, row=1)

def openFile():
     browseText.set('Loading....')
     file = askopenfile(parent=root, mode='rb', title='Choose a file', filetypes=[('Pdf file', '*.pdf')])
     if file:
         readPdf = PyPDF2.PdfFileReader(file)
         page = readPdf.getPage(0)
         pageContent = page.extractText()
         
         #textbox
         textBox = tk.Text(root, height=10, width=50, padx=15, pady=15)
         textBox.insert(1.0, pageContent)
         textBox.tag_configure('center', justify='center')
         textBox.tag_add('center', 1.0, "end")
         textBox.grid(column=1, row=3)

         browseText.set("Browse")

# browse button
browseText = tk.StringVar()
browseBtn = tk.Button(root, textvariable=browseText, bg='#20bebe', fg='white', height=2, width=15, command=lambda: openFile())
browseText.set('Browse')
browseBtn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()