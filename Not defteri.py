import tkinter as tk 
from tkinter import filedialog, Text

def yeni_dosya():
    text.delete(1.0, tk.END)

def dosya_ac():
    dosya_yolu = filedialog.askopenfilename(filetypes=[("Text files",".txt")])

    if dosya_yolu:
        with open(dosya_yolu, 'r') as dosya:
            text.delete(1.0, tk.END)
            text.insert(tk.END, dosya.read())

def dosya_kaydet():
    dosya_yolu = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files",".txt")])

    if dosya_yolu:
        with open(dosya_yolu,"w") as dosya:
            dosya.write(text.get(1.0,tk.END))
def bosluk_birak():
    icerik = text.get(1.0, tk.END).strip()
    if icerik:
        kelimeler = icerik.split()
        yeni_icerik = " ".join(kelimeler[:-1])
    text.delete(1.0, tk.END)
    text.insert(1.0, yeni_icerik)


root = tk.Tk()
root.title("Not Defteri")

menu = tk.Menu(root)
root.config(menu=menu)

dosya_menu = tk.Menu(menu)
menu.add_cascade(label="Dosya", menu=dosya_menu)

dosya_menu.add_command(label="Yeni",command=yeni_dosya)
dosya_menu.add_command(label="Aç",command=dosya_ac)
dosya_menu.add_command(label="Kaydet",command=dosya_kaydet)

ayarlar = tk.Menu(menu)
menu.add_cascade(label="Ayarlar",menu=ayarlar)

ayarlar.add_command(label="kelime sil",command=bosluk_birak)


text = tk.Text(root, wrap="word")
text.pack(expand=1, fill="both")

root.mainloop()