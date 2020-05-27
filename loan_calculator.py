# making of project loan_calculator
''' formula for calculating loan installment is:
 i = p*r*(1+r)**n/(1+r)**n
 '''
# Installment yaani 'n' yaani time duration months me hoga, suppose n=2 hai means 2 years to 24 month yaani 24 installments me loan chukaayega. Rate of interest per anum hota hai, isiliye hum 100 se divide kar ke phir 12 se bhi divide karenge, watch img 1.1
from tkinter import *
fields = ('Loan Amount','Number of Installments','Rate of Interest','Installment')   # yaha pe jo last wali string hai Installment wo hai byaaj kitna dena hoga debt chukaane ke baad.
def calculate_installment(entries):
    r = (float(entries[fields[2]].get())/100)/12
    p = float(entries[fields[0]].get())
    n = float(entries[fields[1]].get())
    i = p*r*(1+r)**n/((1+r)**n-1)
    i = ('%8.2f'%i).strip()
    entries[fields[3]].delete(0,END)
    entries[fields[3]].config(state=NORMAL)
    entries[fields[3]].insert(0,i)
    entries[fields[3]].config(state=DISABLED)
def makeform(root,fields):
    entries = {}
    for field in fields:
        row=Frame(root)
        lab = Label(row,width=22,text=field+': ',anchor='w',bg='aliceblue',fg='darkblue')
        ent = Entry(row)
        ent.insert(0,'0')
        row.pack(side=TOP,fill=X,padx=5,pady=5)  # fill=X means ye apne parent element ke barabar width le lega.
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT)
        entries[field]=ent
    entries[field].config(state=DISABLED)
    return entries
if __name__=='__main__':   # is called main module. __name__ is a global var aur iski value hai __main__. Means agar __name__ ki value __main__ hai to ye code chal jaaye. my: generally jab python me badi file banate hai to isko use karte hai.
    root = Tk()
    root.title('Loan Calculator')
    ents = makeform(root,fields)
    b1 =  Button(root,text='Calculate Installment',command=(lambda e=ents:calculate_installment(e)))
    b1.pack(side=LEFT,padx=5,pady=5)
    b2 = Button(root,text='Exit',command=root.quit)
    b2.pack(side=LEFT,padx=5,pady=5)

    root.mainloop()

# result me one month ka installment kitna hoga ye bataayega jab calculate installment pe click karoge