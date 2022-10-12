#----------------------------------
#     Klase par Nomu
#----------------------------------

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

'''
  prod_kategorija - produkta kategorija (zāģis, vīle utt_)
  prod_nos - produkta nosaukums - modeļa nosaukums (piem. BOSCH 350 utt) līdz 30 zīmēm
'''
class Produkts:
    def __init__(self,prod_kategorija=None,prod_nos=None,teh_rakst=None,n_cena_d=15):
        self.Produkta_kategorija = prod_kategorija
        self.Produkta_nosaukums = prod_nos
        self.Tehniskie_raksturojumi = teh_rakst
        self.Nomas_cena_diena = n_cena_d
    # metodes:
    def Produkts_info(self):
        print("Produkta kategorija: " +  str(self.Produkta_kategorija))
        print("Produkta nosaukums: " +  str(self.Produkta_nosaukums))
        print("Tehniskie raksturojumi: " +  str(self.Tehniskie_raksturojumi))
        print("Nomas cena dienā: " +  str(self.Nomas_cena_diena))

class Nomnieks:
    def __init__(self,vards=None,uzvards=None,pk=None,tel=None):
        self.Nomnieks_vards = vards
        self.Nomnieka_uzvards = uzvards
        self.Personas_kods = pk
        self.Telefona_numurs = tel
    # metodes:
    def Nomnieka_info(self):
        print("Nomnieka vārds, uzvārds: " +  str(self.Nomnieks_vards)+" "+  str(self.Nomnieka_uzvards))
        print("Personas kods: " +  str(self.Personas_kods))
        print("Telefona numurs: " +  str(self.Telefona_numurs))

class Noma:
    def __init__(self,sak_datums=None,beig_datums=None,xx1=None,xx2=None):
        self.sakDatums = sak_datums
        self.beigDatums = beig_datums

    # metodes:
  
# Šeit sākas galvenā daļā

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Autors", command=self.enterAuthor)
        fileMenu.add_command(label="Beigt", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Jauns", command=self.newNomnieks)
        editMenu.add_command(label="Dzēst")
        editMenu.add_command(label="Rediģēt")
        menu.add_cascade(label="Nomnieks", menu=editMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Jauns", command=self.newIerices)
        editMenu.add_command(label="Dzēst")
        editMenu.add_command(label="Rediģēt")
        menu.add_cascade(label="Ierīces", menu=editMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Jauns", command=self.newNoma)
        menu.add_cascade(label="Noma", menu=editMenu)

    def exitProgram(self):
        exit()

    def enterAuthor(self):
        messagebox.showinfo("Autors", "Juris Jurītis") 
       
    def newNomnieks(self):
        windowNomnieks = Toplevel(root)
        windowNomnieks.title("Dati par nomnieku")
        windowNomnieks.geometry("250x250")

        Label(windowNomnieks, text="Vārds:").grid(row=0,column=0)
        vards_entry=Entry(windowNomnieks)
        vards_entry.grid(row=0,column=1)

        Label(windowNomnieks, text="Uzvārds:").grid(row=1,column=0)
        uzvards_entry=Entry(windowNomnieks)
        uzvards_entry.grid(row=1,column=1)

        Label(windowNomnieks, text="Personas kods:").grid(row=3,column=0)
        pk_entry=Entry(windowNomnieks)
        pk_entry.grid(row=3,column=1)

        Label(windowNomnieks, text="Telefona numurs:").grid(row=2,column=0)
        numurs_entry=Entry(windowNomnieks)
        numurs_entry.grid(row=2,column=1)

        Button(windowNomnieks, text="Cancel").grid(row=4,column=0)
        Button(windowNomnieks, text="Ok").grid(row=4,column=1)

    def newIerices(self):
        windowIerices = Toplevel(root)
        windowIerices.title("Dati par ierīcēm")
        windowIerices.geometry("250x250")

        Label(windowIerices, text="Kategorija:").grid(row=0,column=0)
        name_entry=Entry(windowIerices)
        name_entry.grid(row=0,column=1)

        Label(windowIerices, text="Nosaukums:").grid(row=1,column=0)
        name_entry=Entry(windowIerices)
        name_entry.grid(row=1,column=1)

        Label(windowIerices, text="Tehniskie raksturojumi:").grid(row=3,column=0)
        name_entry=Entry(windowIerices)
        name_entry.grid(row=3,column=1)

        Label(windowIerices, text="Nomas cena dienā:").grid(row=2,column=0)
        name_entry=Entry(windowIerices)
        name_entry.grid(row=2,column=1)

        Button(windowIerices, text="Cancel").grid(row=4,column=0)
        Button(windowIerices, text="Ok").grid(row=4,column=1)

    def newNoma(self):
        windowNoma = Toplevel(root)
        windowNoma.title("Dati par nomu")
        windowNoma.geometry("250x250")

        Label(windowNoma, text="Saite uz nomnieku:").grid(row=0,column=0)
        name_entry=Entry(windowNoma)
        name_entry.grid(row=0,column=1)

        Label(windowNoma, text="Saite uz ierīci:").grid(row=1,column=0)
        name_entry=Entry(windowNoma)
        name_entry.grid(row=1,column=1)

        Label(windowNoma, text="Nomas sākuma datums:").grid(row=3,column=0)
        name_entry=Entry(windowNoma)
        name_entry.grid(row=3,column=1)

        Label(windowNoma, text="Nomas beigu datums:").grid(row=2,column=0)
        name_entry=Entry(windowNoma)
        name_entry.grid(row=2,column=1)

        Button(windowNoma, text="Cancel").grid(row=4,column=0)
        Button(windowNoma, text="Ok").grid(row=4,column=1)
        
root = Tk()
root.geometry('400x400')
app = Window(root)
root.wm_title("Dažādu ierīču noma")
root.mainloop()