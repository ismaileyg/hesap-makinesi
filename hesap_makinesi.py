import tkinter as tk
import math
from datetime import datetime


gecmis = []


app = tk.Tk()
app.title("Calculator Pro")
app.geometry("350x600")
app.configure(bg="black")


container = tk.Frame(app, bg="black")
container.pack(fill="both", expand=True)

frames = {}

def show_frame(name):
    frames[name].tkraise()


def create_btn(parent, text, color, cmd):
    btn = tk.Button(parent, text=text, bg=color, fg="white",
                    font=("Helvetica", 18), bd=0)

    def click():
        btn.config(bg="#555555")
        parent.after(100, lambda: btn.config(bg=color))
        cmd()

    btn.config(command=click)
    return btn


class Basit(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="black")

        self.ekran = tk.Entry(self, font=("Helvetica", 30),
                              bg="black", fg="white",
                              bd=0, justify="right")
        self.ekran.pack(fill="both", pady=20, padx=10, ipady=20)

        def tikla(x):
            self.ekran.insert(tk.END, str(x))

        def temizle():
            self.ekran.delete(0, tk.END)

        def hesapla():
            try:
                ifade = self.ekran.get()
                sonuc = str(eval(ifade))

                zaman = datetime.now().strftime("%H:%M")
                gecmis.append(f"{zaman}  {ifade} = {sonuc}")

                self.ekran.delete(0, tk.END)
                self.ekran.insert(0, sonuc)
            except:
                self.ekran.insert(0, "Hata")

        butonlar = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['0','C','=','+']
        ]

        for row in butonlar:
            f = tk.Frame(self, bg="black")
            f.pack(expand=True, fill="both")

            for b in row:
                if b == "=":
                    cmd = hesapla
                    color = "#FF9F0A"
                elif b == "C":
                    cmd = temizle
                    color = "#A5A5A5"
                else:
                    cmd = lambda x=b: tikla(x)
                    color = "#333333"

                create_btn(f, b, color, cmd)\
                    .pack(side="left", expand=True, fill="both", padx=5, pady=5)


class Gelismis(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="black")

        self.ekran = tk.Entry(self, font=("Helvetica", 26),
                              bg="black", fg="white",
                              bd=0, justify="right")
        self.ekran.pack(fill="both", pady=20, padx=10, ipady=20)

        def tikla(x):
            self.ekran.insert(tk.END, str(x))

        def temizle():
            self.ekran.delete(0, tk.END)

        def hesapla():
            try:
                ifade = self.ekran.get()
                sonuc = str(eval(ifade))

                zaman = datetime.now().strftime("%H:%M")
                gecmis.append(f"{zaman}  {ifade} = {sonuc}")

                self.ekran.delete(0, tk.END)
                self.ekran.insert(0, sonuc)
            except:
                self.ekran.insert(0, "Hata")

        def sin():
            try:
                val = float(self.ekran.get())
                self.ekran.delete(0, tk.END)
                self.ekran.insert(0, str(math.sin(val)))
            except:
                self.ekran.insert(0, "Hata")

        butonlar = [
            ['sin','C','/','*'],
            ['7','8','9','-'],
            ['4','5','6','+'],
            ['1','2','3','='],
            ['0','.']
        ]

        for row in butonlar:
            f = tk.Frame(self, bg="black")
            f.pack(expand=True, fill="both")

            for b in row:
                if b == "=":
                    cmd = hesapla
                    color = "#FF9F0A"
                elif b == "C":
                    cmd = temizle
                    color = "#A5A5A5"
                elif b == "sin":
                    cmd = sin
                    color = "#FF9F0A"
                else:
                    cmd = lambda x=b: tikla(x)
                    color = "#333333"

                create_btn(f, b, color, cmd)\
                    .pack(side="left", expand=True, fill="both", padx=5, pady=5)


class Gecmis(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="black")

        self.listbox = tk.Listbox(self,
                                   bg="black",
                                   fg="white",
                                   font=("Helvetica", 14),
                                   selectbackground="#FF9F0A")
        self.listbox.pack(expand=True, fill="both", padx=10, pady=10)

        btn = tk.Frame(self, bg="black")
        btn.pack(fill="x")

        tk.Button(btn, text="Seçili Sil",
                  bg="#FF3B30", fg="white",
                  command=self.sil_secili)\
            .pack(side="left", expand=True, fill="x")

        tk.Button(btn, text="Tümünü Sil",
                  bg="#FF9500", fg="white",
                  command=self.sil_hepsi)\
            .pack(side="left", expand=True, fill="x")

        tk.Button(btn, text="Kaydet",
                  bg="#34C759", fg="white",
                  command=self.kaydet)\
            .pack(side="left", expand=True, fill="x")

    def guncelle(self):
        self.listbox.delete(0, tk.END)
        for i in gecmis:
            self.listbox.insert(tk.END, i)

    def sil_secili(self):
        secili = self.listbox.curselection()
        if secili:
            val = self.listbox.get(secili[0])
            if val in gecmis:
                gecmis.remove(val)
            self.guncelle()

    def sil_hepsi(self):
        gecmis.clear()
        self.guncelle()

    def kaydet(self):
        with open("history.txt", "w", encoding="utf-8") as f:
            for i in gecmis:
                f.write(i + "\n")


for F, name in [(Basit,"basit"), (Gelismis,"gelismis"), (Gecmis,"gecmis")]:
    frame = F(container)
    frames[name] = frame
    frame.place(relwidth=1, relheight=1)


nav = tk.Frame(app, bg="#111111", height=60)
nav.pack(fill="x", side="bottom")

def open_gecmis():
    show_frame("gecmis")
    frames["gecmis"].guncelle()

tk.Button(nav, text="Basit", bg="#111111", fg="white",
          bd=0, command=lambda: show_frame("basit"))\
    .pack(side="left", expand=True, fill="both")

tk.Button(nav, text="Pro", bg="#111111", fg="white",
          bd=0, command=lambda: show_frame("gelismis"))\
    .pack(side="left", expand=True, fill="both")

tk.Button(nav, text="Geçmiş", bg="#111111", fg="white",
          bd=0, command=open_gecmis)\
    .pack(side="left", expand=True, fill="both")


show_frame("basit")

app.mainloop()