from cmath import isnan, nan
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pandas as pd



class MainApplication:
    
    def load_driver(self,event):
        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com')
        self.wait = WebDriverWait(self.driver,10)
        self.textbox.insert('1.0', 'Login to your account and start program')
        
    def find_contact(self,name):
        sfield = self.driver.find_elements(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
        sfield[0].click()
        sfield[0].send_keys(name)
        sfield[0].send_keys(Keys.ENTER)
        
    
    def send_message(self,filename,description):
        self.driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
        attach = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        sleep(4)
        attach.send_keys(filename)
        sleep(4)
        sfield = self.driver.find_elements(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
        sfield[0].click()
        sfield[0].send_keys(description)
        sleep(4)
        send = self.driver.find_element(By.CSS_SELECTOR, "span[data-icon='send']")
        send.click()
        
    
    def start_program(self,event):
        
        self.products_df = pd.read_excel('products.xlsx')
        self.contacts_df = pd.read_excel('contacts.xlsx')
        locationslist = self.products_df['LOCATION'].tolist()
        descriptionslist = self.products_df['DESCRIPTION'].tolist()
        
        for i in range(0,len(self.contacts_df)):
            self.find_contact(self.contacts_df.loc[i,'CONTACTS'])
            sleep(3)
            for a in range(0,len(locationslist)):
                self.send_message(locationslist[a],descriptionslist[a])
                sleep(7)
            
                    
            
            
    
    
    
    def update_contact_database(self,event):
        try:
            self.textbox.delete('1.0', END)
            contact_name = self.contactname.get()
            if contact_name == '':
                self.textbox.insert('1.0','ERROR')
            else:
                self.contacts_df = pd.read_excel('contacts.xlsx')
                self.contacts_df.loc[len(self.products_df)] = contact_name
                self.contacts_df.to_excel('contacts.xlsx',index=False)
                self.textbox.insert('1.0','SUCCESS')
        except:
            self.textbox.insert('1.0','ERROR')
        
        
    def update_product_database(self,event):
        try:
            self.textbox.delete('1.0', END)
            description = self.description.get()
            price = self.price.get()
            file = self.filenameentry.get()
            if description == '' or price == '' or file == '':
                self.textbox.insert('1.0','ERROR')
            else:
                self.products_df = pd.read_excel('products.xlsx')     
                row = (file,description,price)
                self.products_df.loc[len(self.products_df)] = row
                self.products_df.to_excel('products.xlsx',index=False)
                self.textbox.insert('1.0','SUCCESS')
        except:
            self.textbox.insert('1.0','ERROR')
        
        
    def insert_infos(self,event):
        self.products_df = pd.read_excel('products.xlsx')
        self.contacts_df = pd.read_excel('contacts.xlsx')
        try:
            self.main_tree.delete(*self.main_tree.get_children())
            self.contact_tree.delete(*self.contact_tree.get_children())
        finally:
            descriptions = self.products_df['DESCRIPTION'].tolist()
            sorted_descriptions = sorted(descriptions)
            prices = self.products_df['PRICE'].tolist()
            for i in range(0,len(self.products_df)):
                entire_list = (sorted_descriptions[i],f'R${prices[i]}.00')
                self.main_tree.insert('',END,values=entire_list,tags=('oddrow',))
                self.main_tree.tag_configure('oddrow',background='#99FF66',foreground='black')
                
            contactlist = self.contacts_df['CONTACTS'].tolist()
            for i in range(0,len(self.contacts_df)):
                self.contact_tree.insert('',END,values=(contactlist[i],'-'),tags=('oddrow',))
                self.contact_tree.tag_configure('oddrow',background='#99FF66',foreground='black')
            
        
    
    def clear_textbox(self,event):
        self.textbox.delete('1.0', END)
        
    
    def browsefunc(self,event):
        filename = askopenfilename(filetypes=(("jpeg files","*.jpeg"),("png files","*.png"),("All files","*.*")))
        self.filenameentry.insert(END, filename) # add this
    
    
    
    
    def __init__(self,toplevel):
        
        
        self.frame = Frame(toplevel).grid()
        columns = ('desc','pri')
        style = ttk.Style(root)
        style.theme_use("clam")
        style.configure("Treeview", background="##99FF66", 
                fieldbackground="##99FF66", foreground="black")
        
        style.configure("Treeview.Heading", background="black", 
                fieldbackground="black", foreground="#99FF66")
        
        ###titulos
        title = Label(self.frame,text='Whatsapp Automatic Sending',font=('Verdana',18,'bold'),background='black',fg='#99FF66',borderwidth=2).place(x=27,y=10)
        driverlabel = Label(self.frame,text='Load Driver',font=('Helvetica',13,'bold'),background='black',fg='#99FF66',border=2).place(x=27,y=45)
        alertboxtext = Label(self.frame,text='Alert Box',font=('Helvetica',13,'bold'),background='black',fg='#99FF66',border=2).place(x=27,y=98)
        treedatabasetitle = Label(self.frame,text='DATABASE',font=('Helvetica',20,'bold'),background='black',fg='#99FF66').place(x=250,y=85)
        startsendtitle = Label(self.frame,text='START PROGRAM',font=('Helvetica',13,'bold'),background='black',fg='#99FF66').place(x=27,y=300)
        grouplisttitle = Label(self.frame,text='CONTACT LIST',font=('Helvetica',20,'bold'),background='black',fg='#99FF66').place(x=890,y=85)
        addcontacttitle = Label(self.frame,text='ADD CONTACT',font=('Helvetica',13,'bold'),background='black',fg='#99FF66').place(x=890,y=350)
        addproducttitle = Label(self.frame,text='ADD PRODUCT',font=('Helvetica',13,'bold'),background='black',fg='#99FF66').place(x=250,y=350)
        productnametitle = Label(self.frame,text='Description',font=('Helvetica',10,'bold'),background='black',fg='#99FF66').place(x=250,y=370)
        productpricetitle = Label(self.frame,text='Price',font=('Helvetica',10,'bold'),background='black',fg='#99FF66').place(x=450,y=370)
        productpicturetitle = Label(self.frame,text='File(.jpeg or .png)',font=('Helvetica',10,'bold'),background='black',fg='#99FF66').place(x=250,y=415)
        
        
        ###widgets
        self.loaddriverbutton = Button(self.frame,text='LOAD',
                                       fg='#99FF66',bg='black',relief='groove',
                                       width=15)
        self.loaddriverbutton.place(x=30,y=70)
        self.loaddriverbutton.bind('<Button-1>',self.load_driver)
        self.textbox = Text(self.frame,width=18,font=('Helvetica'),height=7,fg='#99FF66',bg='black',highlightcolor='pink',highlightthickness=2)
        self.textbox.place(x=30,y=120)
        self.cleartextbutton = Button(self.frame,text='CLEAR',fg='#99FF66',bg='black',relief='groove',width=13)
        self.cleartextbutton.place(x=50,y=260)
        self.cleartextbutton.bind('<Button-1>',self.clear_textbox)
        self.startbutton = Button(self.frame,text='START',fg='#99FF66',bg='black',relief='groove',width=13)
        self.startbutton.place(x=50,y=322)
        self.startbutton.bind('<Button-1>',self.start_program)
        self.description = Entry(self.frame)
        self.description.place(x=250,y=390)
        self.price = Entry(self.frame,width=10)
        self.price.place(x=450,y=390)
        self.addproductbutton = Button(self.frame,text='ADD',fg='#99FF66',bg='black',relief='groove',width=10)
        self.addproductbutton.place(x=520,y=387)
        self.addproductbutton.bind('<Button-1>',self.update_product_database)
        self.contactname = Entry(self.frame)
        self.contactname.place(x=890,y=370)
        self.addcontactbutton = Button(self.frame,text='ADD',fg='#99FF66',bg='black',relief='groove',width=8)
        self.addcontactbutton.place(x=1020,y=368)
        self.addcontactbutton.bind('<Button-1>',self.update_contact_database)
        self.updatetreebutton = Button(self.frame,text='UPDATE',fg='#99FF66',bg='black',relief='groove')
        self.updatetreebutton.place(x=476,y=92)
        self.updatetreebutton.bind('<Button-1>',self.insert_infos)
        self.filenameentry = Entry(self.frame,width=30)
        self.filenameentry.place(x=250,y=440)
        self.addfilelocation = Button(self.frame,text='BROWSE',fg='#99FF66',bg='black',relief='groove')
        self.addfilelocation.place(x=440,y=438)
        self.addfilelocation.bind('<Button-1>',self.browsefunc)

        
        ##trees
        self.main_tree = ttk.Treeview(self.frame,columns=columns,show='headings')
        self.main_tree.heading('desc',text='Description',anchor=CENTER)
        self.main_tree.heading('pri',text='Price',anchor=CENTER)
        self.main_tree.column('desc',width=500,anchor=W)
        self.main_tree.column('pri',width=100,anchor=CENTER)
        self.main_tree.place(x=250,y=120)
        
        self.contact_tree = ttk.Treeview(self.frame,columns=('contact'),show='headings')
        self.contact_tree.heading('contact',text='CONTACTS')
        self.contact_tree.place(x=890,y=120)
        
        
        
        

if __name__ == '__main__':
    root = Tk()
    MainApplication(root)
    root.geometry('1200x480')
    root.configure(background='black')
    root.mainloop()