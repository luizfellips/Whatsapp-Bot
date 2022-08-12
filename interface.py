from tkinter import *
from tkinter import ttk
import database


class MainApplication:
    def __init__(self,toplevel):
        self.frame = Frame(toplevel).grid()
        columns = ('desc','pri')
        style = ttk.Style(root)
        style.theme_use("clam")
        style.configure("Treeview", background="#45458B", 
                fieldbackground="#45458B", foreground="white")
        
        ###titulos
        title = Label(self.frame,text='Whatsapp Automatic Sending',font=('Verdana',18,'bold'),background='gray',fg='white',borderwidth=2).place(x=27,y=10)
        driverlabel = Label(self.frame,text='Load Driver',font=('Helvetica',13,'bold'),background='gray',fg='white',border=2).place(x=27,y=45)
        alertboxtext = Label(self.frame,text='Process Alert Box',font=('Helvetica',13,'bold'),background='gray',fg='white',border=2).place(x=27,y=95)
        treedatabasetitle = Label(self.frame,text='DATABASE',font=('Helvetica',20,'bold'),background='gray',fg='white').place(x=250,y=85)
        startsendtitle = Label(self.frame,text='START PROGRAM',font=('Helvetica',13,'bold'),background='gray',fg='white').place(x=27,y=300)
        grouplisttitle = Label(self.frame,text='CONTACT LIST',font=('Helvetica',20,'bold'),background='gray',fg='white').place(x=890,y=85)
        addcontacttitle = Label(self.frame,text='ADD CONTACT',font=('Helvetica',13,'bold'),background='gray',fg='white').place(x=890,y=350)
        addproducttitle = Label(self.frame,text='ADD PRODUCT',font=('Helvetica',13,'bold'),background='gray',fg='white').place(x=250,y=350)
        productnametitle = Label(self.frame,text='Description',font=('Helvetica',10,'bold'),background='gray',fg='white').place(x=250,y=370)
        productpricetitle = Label(self.frame,text='Price',font=('Helvetica',10,'bold'),background='gray',fg='white').place(x=450,y=370)
        ###widgets
        self.openwindowbutton = Button(self.frame,text='LOAD',
                                       fg='black',bg='white',
                                       width=15)
        self.openwindowbutton.place(x=30,y=70)
        self.textbox = Text(self.frame,width=18,height=7)
        self.textbox.place(x=30,y=120)
        self.cleartextbutton = Button(self.frame,text='CLEAR',fg='black',bg='white',width=13)
        self.cleartextbutton.place(x=50,y=240)
        self.startbutton = Button(self.frame,text='START',fg='black',bg='white',width=13)
        self.startbutton.place(x=50,y=322)
        self.description = Entry(self.frame)
        self.description.place(x=250,y=390)
        self.price = Entry(self.frame,width=10)
        self.price.place(x=450,y=390)
        self.addproductbutton = Button(self.frame,text='ADD',fg='black',bg='white',width=10)
        self.addproductbutton.place(x=520,y=387)
        self.contactname = Entry(self.frame)
        self.contactname.place(x=890,y=370)
        self.addcontactbutton = Button(self.frame,text='ADD',fg='black',bg='white',width=8)
        self.addcontactbutton.place(x=1020,y=368)
        self.updatetreebutton = Button(self.frame,text='UPDATE',fg='black',bg='WHITE')
        self.updatetreebutton.place(x=476,y=92)

        
        ##trees
        self.main_tree = ttk.Treeview(self.frame,columns=columns,show='headings')
        self.main_tree.heading('desc',text='Description',anchor=CENTER)
        self.main_tree.heading('pri',text='Price',anchor=CENTER)
        self.main_tree.column('desc',width=500,anchor=W)
        self.main_tree.column('pri',width=100,anchor=CENTER)
        for item in database.set_of_products:
            value = f'R${item.price},00' 
            self.main_tree.insert('',END,values=(item.description,value),tags=('oddrow'))
            self.main_tree.tag_configure('oddrow',background='#45458B',foreground='white')
        self.main_tree.place(x=250,y=120)
        
        self.contact_tree = ttk.Treeview(self.frame,columns=('contact','index'),show='headings')
        self.contact_tree.heading('contact',text='CONTACTS')
        self.contact_tree.heading('index',text='INDEX')
        self.contact_tree.column('index',width=40,anchor=CENTER)
        for count,item in enumerate(database.list_of_contacts,start=1):
            value = f'{item}'
            self.contact_tree.insert('',END,values=(value,count),tags=('oddrow'))
            self.contact_tree.tag_configure('oddrow',background='#45458B',foreground='white')
        self.contact_tree.place(x=890,y=120)
        
        
        
        

if __name__ == '__main__':
    root = Tk()
    MainApplication(root)
    root.geometry('1200x450')
    root.configure(background='gray')
    root.mainloop()