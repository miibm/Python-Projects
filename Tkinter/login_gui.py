import sqlite3 as s
from tkinter import *
from tkinter import messagebox

class Database:

    def __init__(self):
        self.file = s.Connection("accounts.db")
        self.obj = self.file.cursor()
        try:
            self.obj.execute("CREATE TABLE log (name text,password text,pin int)")
        except:
            pass

    def add(self,name,password,pin):
        try:
            self.data = (name,password,pin)
            self.obj.execute("INSERT INTO log (name,password,pin) VALUES(?,?,?)",self.data)
        except:
            print("Wrong Data Type Given ...")

    def modify(self,key,old_value,new_value):
        try:
            self.obj.execute(f'UPDATE log SET {key}=? WHERE {key}=?',(new_value,old_value))
        except:
            print("Invailed Value ...")

    def show(self):
        self.l = []
        for self.x in self.obj.execute("SELECT * FROM log "):
            self.l.append(self.x)
        return tuple(self.l)

    def save(self):
        self.file.commit()


class Login(Database):

    def login(self,username,password):
        self.st = 0
        for x in self.show():
            if ((x[0] == username)):
                self.st = 1
                if ((x[1] == password)):
                    return (0,"Login successful")
                    break
                else:
                    return (1,"Invalid Password")
                    break
        if(self.st == 0):
            return (1,"Invalid Username")

    def newaccount(self,username,password,pin):
            if (type(username) == str and type(password) == str and type(pin) == int):
                self.add(name=username, password=password,pin=pin)
                self.save()
                return (0,"Account successfully Added ")
            else:
                return (1,"Enter values correctly ")

    def recover(self,username,pin):
        self.st = 0
        for x in self.show():
            if ((x[0] == username)):
                if ((x[2] == pin)):
                    return (0,f'Password : {x[1]}')
                    self.st = 1
                else:
                    return (1,"Invalid Recovery Pin")
                    self.st = 1
        if(self.st == 0):
            return (1,"Invalid Username")

    def change(self,username,password,choice,new_value):
        self.st = 0
        for x in self.show():
            if ((x[0] == username)):
                if ((x[1] == password)):
                    if (choice == 1):
                        self.modify(key="name",new_value=new_value,old_value=username)
                        self.st = 1
                        self.save()
                        return (0,"Username changed")
                    elif (choice == 2):
                        self.modify(key="password",new_value=new_value,old_value=password)
                        self.st = 1
                        self.save()
                        return (0,"Password changed")
                    elif (choice == 3):
                        self.modify(key="pin",new_value=new_value,old_value=x[2])
                        self.st = 1
                        self.save()
                        return (0,"Recovery Pin changed")
                    else:
                        return (1,"Invalid choice")
                        self.st = 1
                else:
                    return (1,"Invalid Password")
                    self.st = 1
        if(self.st == 0):
            return (1,"Invalid Username")
        self.save()


        # self.start()

    def start(self):
        self.msg = """\nWelcome To Login Database
        \t1.Login
        \t2.Create New Account
        \t3.Recovery Password
        \t4.Change Account Details
        \t5.Exit
        """
        print(self.msg)
        while True:
            self.ch = int(input("Enter Your Choice : "))
            if(self.ch == 1):
                self.login()
            elif(self.ch == 2):
                self.newaccount()
            elif(self.ch == 3):
                self.recover()
            elif(self.ch == 4):
                self.change()
            elif(self.ch == 5):
                break
            else:
                print("Wrong Choice..")


class tk_login(Login):
    def start(self):
        self.root_login = Tk()
        self.root_login.title("Login")
        self.root_login.geometry("250x230")
    def function(self):
        self.user_v = self.user_e.get()
        self.pasd_v = self.pasd_e.get()
        self.val,self.response = self.login(username=self.user_v, password=self.pasd_v)
        if self.val == 0:
            messagebox.showinfo("Login",self.response)
        elif self.val == 1:
            messagebox.showerror("Error",self.response)
        else:
            pass
    def home(self):
        self.root_login.destroy()
        o = tk_index().run()
    def structure(self):
        self.title    = Label(self.root_login,text="Login",fg="blue")

        self.user_l   = Label(self.root_login,text="Username  ")
        self.pasd_l   = Label(self.root_login,text="Password  ")

        self.user_e   = Entry(self.root_login)
        self.pasd_e   = Entry(self.root_login)

        self.login_b  = Button(self.root_login,text="Login",command=self.function,bg="green",fg="white")
        self.home_b   = Button(self.root_login,text="Home",command=self.home,bg="green",fg="white")
        self.exit_b   = Button(self.root_login,text="Exit",command=self.root_login.destroy,bg="green",fg="white")
    def build(self):
        self.title.grid(row=3,column=5,rowspan=1,columnspan=10,pady=25)

        self.user_l.grid(row=5,column=5,rowspan=1,columnspan=1,padx=10)
        self.pasd_l.grid(row=7,column=5,rowspan=1,columnspan=1,padx=10)

        self.user_e.grid(row=5,column=10,rowspan=1,columnspan=1)
        self.pasd_e.grid(row=7,column=10,rowspan=1,columnspan=1)

        self.login_b.grid(row=10,column=10,rowspan=1,columnspan=5,ipadx=20,ipady=1,pady=15,padx=20)
        self.home_b.grid(row=12,column=5,rowspan=1,columnspan=10,ipadx=80,ipady=1,pady=2)
        self.exit_b.grid(row=10,column=5,rowspan=1,columnspan=5,ipadx=25,ipady=1,pady=15,padx=20)
    def run(self):
        self.start()
        self.structure()
        self.build()
        self.root_login.mainloop()


class tk_newac(Login):
    def start(self):
        self.root_newac = Tk()
        self.root_newac.title("New Acount")
        self.root_newac.geometry("250x250")
    def function(self):
        self.user_v = self.user_e.get()
        self.pasd_v = self.pasd_e.get()
        self.repi_v = int(self.repi_e.get())
        self.val,self.response = self.newaccount(username=self.user_v, password=self.pasd_v,pin=self.repi_v)
        if self.val == 0:
            messagebox.showinfo("New Account",self.response)
        elif self.val == 1:
            messagebox.showerror("Error",self.response)
        else:
            pass
    def home(self):
        self.root_newac.destroy()
        o = tk_index().run()
    def structure(self):
        self.title    = Label(self.root_newac,text="Create New Account",fg="blue")

        self.user_l   = Label(self.root_newac,text="Username       ")
        self.pasd_l   = Label(self.root_newac,text="Password       ")
        self.repi_l   = Label(self.root_newac,text="Recovery Pin   ")

        self.user_e   = Entry(self.root_newac)
        self.pasd_e   = Entry(self.root_newac)
        self.repi_e   = Entry(self.root_newac)

        self.creat_b  = Button(self.root_newac,text="Create",command=self.function,bg="green",fg="white")
        self.home_b   = Button(self.root_newac,text="Home",command=self.home,bg="green",fg="white")
        self.exit_b   = Button(self.root_newac,text="Exit",command=self.root_newac.destroy,bg="green",fg="white")
    def build(self):
        self.title.grid(row=3,column=5,rowspan=1,columnspan=10,pady=25)

        self.user_l.grid(row=5,column=5,rowspan=1,columnspan=1,padx=10,pady=2)
        self.pasd_l.grid(row=10,column=5,rowspan=1,columnspan=1,padx=10,pady=2)
        self.repi_l.grid(row=15,column=5,rowspan=1,columnspan=1,padx=10,pady=2)

        self.user_e.grid(row=5,column=10,rowspan=1,columnspan=1,pady=2)
        self.pasd_e.grid(row=10,column=10,rowspan=1,columnspan=1,pady=2)
        self.repi_e.grid(row=15,column=10,rowspan=1,columnspan=1,pady=2)

        self.creat_b.grid(row=20,column=10,rowspan=1,columnspan=5,ipadx=20,ipady=1,pady=15,padx=20)
        self.home_b.grid(row=25,column=5,rowspan=1,columnspan=10,ipadx=80,ipady=1,pady=2)
        self.exit_b.grid(row=20,column=5,rowspan=1,columnspan=5,ipadx=25,ipady=1,pady=15,padx=20)
    def run(self):
        self.start()
        self.structure()
        self.build()
        self.root_newac.mainloop()


class tk_recps(Login):
    def start(self):
        self.root_recps = Tk()
        self.root_recps.title("Change Password")
        self.root_recps.geometry("250x250")
    def home(self):
        self.root_recps.destroy()
        o = tk_chrec().run()
    def function(self):
        self.user_e_v  = self.user_e.get()
        self.opasd_e_v = self.opasd_e.get()
        self.npasd_e_v = self.npasd_e.get()
        self.val,self.response = self.change(username=self.user_e_v, password=self.opasd_e_v,new_value=self.npasd_e_v,choice=2)
        if self.val == 0:
            messagebox.showinfo("Password",self.response)
        elif self.val == 1:
            messagebox.showerror("Error",self.response)
        else:
            pass
    def structure(self):
        self.title       = Label(self.root_recps,text="Change Password",fg="blue")

        self.user_l      = Label(self.root_recps,text="Username    ")
        self.opasd_l     = Label(self.root_recps,text="Old Password")
        self.npasd_l     = Label(self.root_recps,text="New Password")

        self.user_e      = Entry(self.root_recps)
        self.opasd_e     = Entry(self.root_recps)
        self.npasd_e     = Entry(self.root_recps)

        self.recps_b     = Button(self.root_recps,text="Change",command=self.function,bg="green",fg="white")
        self.home_b      = Button(self.root_recps,text="Home",command=self.home,bg="green",fg="white")
        self.exit_b      = Button(self.root_recps,text="Exit",command=self.root_recps.destroy,bg="green",fg="white")
    def build(self):
        self.title.grid(row=3,column=5,rowspan=1,columnspan=10,pady=25)

        self.user_l.grid(row=5,column=5,rowspan=1,columnspan=1,padx=10,pady=2)
        self.opasd_l.grid(row=10,column=5,rowspan=1,columnspan=1,padx=10,pady=2)
        self.npasd_l.grid(row=15,column=5,rowspan=1,columnspan=1,padx=10,pady=2)

        self.user_e.grid(row=5,column=10,rowspan=1,columnspan=1,pady=2)
        self.opasd_e.grid(row=10,column=10,rowspan=1,columnspan=1,pady=2)
        self.npasd_e.grid(row=15,column=10,rowspan=1,columnspan=1,pady=2)

        self.recps_b.grid(row=20,column=10,rowspan=1,columnspan=5,ipadx=20,ipady=1,pady=15,padx=20)
        self.home_b.grid(row=25,column=5,rowspan=1,columnspan=10,ipadx=80,ipady=1,pady=2)
        self.exit_b.grid(row=20,column=5,rowspan=1,columnspan=5,ipadx=25,ipady=1,pady=15,padx=20)
    def run(self):
        self.start()
        self.structure()
        self.build()
        self.root_recps.mainloop()


class tk_recus(Login):
    def start(self):
        self.root_recus = Tk()
        self.root_recus.title("Change Username")
        self.root_recus.geometry("250x250")
    def home(self):
        self.root_recus.destroy()
        o = tk_chrec().run()
    def function(self):
        self.user_e_v  = self.user_e.get()
        self.pasd_e_v = self.pasd_e.get()
        self.nuser_e_v = self.nuser_e.get()
        self.val,self.response = self.change(username=self.user_e_v, password=self.pasd_e_v,new_value=self.nuser_e_v,choice=1)
        if self.val == 0:
            messagebox.showinfo("Username",self.response)
        elif self.val == 1:
            messagebox.showerror("Error",self.response)
        else:
            pass
    def structure(self):
        self.title      = Label(self.root_recus,text="Change Username",fg="blue")

        self.user_l     = Label(self.root_recus,text="Username")
        self.pasd_l     = Label(self.root_recus,text="Password")
        self.nuser_l    = Label(self.root_recus,text="New Username")

        self.user_e     = Entry(self.root_recus)
        self.pasd_e     = Entry(self.root_recus)
        self.nuser_e    = Entry(self.root_recus)

        self.recu_b     = Button(self.root_recus,text="Change",command=self.function,bg="green",fg="white")
        self.home_b     = Button(self.root_recus,text="Home",command=self.home,bg="green",fg="white")
        self.exit_b     = Button(self.root_recus,text="Exit",command=self.root_recus.destroy,bg="green",fg="white")
    def build(self):
        self.title.grid(row=3,column=5,rowspan=1,columnspan=10,pady=25)

        self.user_l.grid(row=5,column=5,rowspan=1,columnspan=1,padx=10,pady=2)
        self.pasd_l.grid(row=10,column=5,rowspan=1,columnspan=1,padx=10,pady=2)
        self.nuser_l.grid(row=15,column=5,rowspan=1,columnspan=1,padx=10,pady=2)

        self.user_e.grid(row=5,column=10,rowspan=1,columnspan=1,pady=2)
        self.pasd_e.grid(row=10,column=10,rowspan=1,columnspan=1,pady=2)
        self.nuser_e.grid(row=15,column=10,rowspan=1,columnspan=1,pady=2)

        self.recu_b.grid(row=20,column=10,rowspan=1,columnspan=5,ipadx=20,ipady=1,pady=15,padx=20)
        self.home_b.grid(row=25,column=5,rowspan=1,columnspan=10,ipadx=80,ipady=1,pady=2)
        self.exit_b.grid(row=20,column=5,rowspan=1,columnspan=5,ipadx=25,ipady=1,pady=15,padx=20)
    def run(self):
        self.start()
        self.structure()
        self.build()
        self.root_recus.mainloop()


class tk_recpn(Login):
    def start(self):
        self.root_recpn = Tk()
        self.root_recpn.title("Change Recovery Pin")
        self.root_recpn.geometry("250x250")
    def home(self):
        self.root_recpn.destroy()
        o = tk_chrec().run()
    def function(self):
        self.user_e_v = self.user_e.get()
        self.pasd_e_v = self.pasd_e.get()
        self.npin_e_v = int(self.npin_e.get())
        self.val,self.response = self.change(username=self.user_e_v, password=self.pasd_e_v,new_value=self.npin_e_v,choice=3)
        if self.val == 0:
            messagebox.showinfo("Recovery Pin",self.response)
        elif self.val == 1:
            messagebox.showerror("Error",self.response)
        else:
            pass
    def structure(self):
        self.title       = Label(self.root_recpn,text="Change Recovery Pin",fg="blue")

        self.user_l      = Label(self.root_recpn,text="Username")
        self.pasd_l      = Label(self.root_recpn,text="Password")
        self.npin_l      = Label(self.root_recpn,text="New Recovery Pin")

        self.user_e      = Entry(self.root_recpn)
        self.pasd_e      = Entry(self.root_recpn)
        self.npin_e      = Entry(self.root_recpn)

        self.recpn_b     = Button(self.root_recpn,text="Change",command=self.function,bg="green",fg="white")
        self.home_b      = Button(self.root_recpn,text="Home",command=self.home,bg="green",fg="white")
        self.exit_b      = Button(self.root_recpn,text="Exit",command=self.root_recpn.destroy,bg="green",fg="white")
    def build(self):
        self.title.grid(row=3,column=5,rowspan=1,columnspan=10,pady=25)

        self.user_l.grid(row=5,column=5,rowspan=1,columnspan=1,padx=10,pady=2)
        self.pasd_l.grid(row=10,column=5,rowspan=1,columnspan=1,padx=10,pady=2)
        self.npin_l.grid(row=15,column=5,rowspan=1,columnspan=1,padx=10,pady=2)

        self.user_e.grid(row=5,column=10,rowspan=1,columnspan=1,pady=2)
        self.pasd_e.grid(row=10,column=10,rowspan=1,columnspan=1,pady=2)
        self.npin_e.grid(row=15,column=10,rowspan=1,columnspan=1,pady=2)

        self.recpn_b.grid(row=20,column=10,rowspan=1,columnspan=5,ipadx=20,ipady=1,pady=15,padx=20)
        self.home_b.grid(row=25,column=5,rowspan=1,columnspan=10,ipadx=80,ipady=1,pady=2)
        self.exit_b.grid(row=20,column=5,rowspan=1,columnspan=5,ipadx=25,ipady=1,pady=15,padx=20)
    def run(self):
        self.start()
        self.structure()
        self.build()
        self.root_recpn.mainloop()


class tk_chrec(tk_recpn,tk_recps,tk_recus):
    def start(self):
        self.chrec = Tk()
        self.chrec.title("Change Account Details")
        self.chrec.geometry("250x250")

    def run_recus(self):
        self.chrec.destroy()
        self.o_tk_recus = tk_recus().run()
    def run_recps(self):
        self.chrec.destroy()
        self.o_tk_recps = tk_recps().run()
    def run_recpn(self):
        self.chrec.destroy()
        self.o_tk_recpn = tk_recpn().run()
    def home(self):
        self.chrec.destroy()
        o = tk_index().run()

    def structure(self):
        self.title = Label(self.chrec,text="Change Account Details",font=("vijaya",20))

        self.usr_btn   = Button(self.chrec,command=self.run_recus,text="Change Username",bg="black",fg="white")
        self.psd_btn   = Button(self.chrec,command=self.run_recps,text="Change Password",bg="black",fg="white")
        self.pin_btn   = Button(self.chrec,command=self.run_recpn,text="Change Recovery Pin",bg="black",fg="white")
        self.home_btn  = Button(self.chrec,text="Home",command=self.home,bg="black",fg="white")
        self.ext_btn   = Button(self.chrec,text="Exit",command=self.chrec.destroy,bg="black",fg="white")

    def build(self):
        self.title.grid(  row=3,column=10,columnspan=1,pady=13,padx=10,ipady=1)
        self.usr_btn.grid(row=4,column=10,columnspan=1,pady=3,padx=45,ipadx=10)
        self.psd_btn.grid(row=5,column=10,columnspan=1,pady=3,padx=45,ipadx=12)
        self.pin_btn.grid(row=6,column=10,columnspan=1,pady=3,padx=45,ipadx=3)
        self.home_btn.grid(row=7,column=10,columnspan=1,pady=3,padx=45,ipadx=44)
        self.ext_btn.grid(row=8,column=10,columnspan=1,pady=3,padx=45,ipadx=52)
    def run(self):
        self.start()
        self.structure()
        self.build()
        self.chrec.mainloop()


class tk_rec(Login):
    def start(self):
        self.root_rec = Tk()
        self.root_rec.title("Recovery Password")
        self.root_rec.geometry("250x230")
    def home(self):
        self.root_rec.destroy()
        o = tk_index().run()
    def function(self):
        self.user_v = self.user_e.get()
        self.pin_v = int(self.pin_e.get())
        self.val,self.response = self.recover(username=self.user_v,pin=self.pin_v)
        if self.val == 0:
            messagebox.showinfo("Password",self.response)
        elif self.val == 1:
            messagebox.showerror("Error",self.response)
        else:
            pass
    def structure(self):
        self.title    = Label(self.root_rec,text="Recovery Password",fg="blue")

        self.user_l   = Label(self.root_rec,text="Username      ")
        self.pin_l    = Label(self.root_rec,text="Recovery Pin  ")

        self.user_e   = Entry(self.root_rec)
        self.pin_e    = Entry(self.root_rec)

        self.rec_b    = Button(self.root_rec,text="Recovery",command=self.function,bg="green",fg="white")
        self.home_b   = Button(self.root_rec,text="Home",command=self.home,bg="green",fg="white")
        self.exit_b   = Button(self.root_rec,text="Exit",command=self.root_rec.destroy,bg="green",fg="white")
    def build(self):
        self.title.grid(row=3,column=5,rowspan=1,columnspan=10,pady=25)

        self.user_l.grid(row=5,column=5,rowspan=1,columnspan=1,padx=10,pady=2)
        self.pin_l.grid(row=10,column=5,rowspan=1,columnspan=1,padx=10,pady=2)

        self.user_e.grid(row=5,column=10,rowspan=1,columnspan=1,pady=2)
        self.pin_e.grid(row=10,column=10,rowspan=1,columnspan=1,pady=2)

        self.rec_b.grid(row=15,column=10,rowspan=1,columnspan=5,ipadx=20,ipady=1,pady=15,padx=20)
        self.home_b.grid(row=20,column=5,rowspan=1,columnspan=10,ipadx=85,ipady=1,pady=2)
        self.exit_b.grid(row=15,column=5,rowspan=1,columnspan=5,ipadx=25,ipady=1,pady=15,padx=20)
    def run(self):
        self.start()
        self.structure()
        self.build()
        self.root_rec.mainloop()


class tk_index(tk_login,tk_newac,tk_chrec,tk_rec):
    def start(self):
        self.index = Tk()
        self.index.title("Login Database")
        self.index.geometry("300x250")

    def login_btn(self):
        self.index.destroy()
        self.o_login =tk_login()
        self.o_login.run()
    def newac_btn(self):
        self.index.destroy()
        self.o_newac =tk_newac()
        self.o_newac.run()
    def chrec_btn(self):
        self.index.destroy()
        self.o_chrec =tk_chrec()
        self.o_chrec.run()
    def rec_btn(self):
        self.index.destroy()
        self.o_rec =tk_rec()
        self.o_rec.run()

    def structure(self):
        self.welcome_label = Label( self.index, text=" Welcome to the Login Database",fg="green",font=("vijaya",20))
        self.login_btn     = Button(self.index,command=self.login_btn,text="Login",bg="black",fg="white",font=("consols",10))
        self.newac_btn     = Button(self.index,command=self.newac_btn,text="Create New Account",bg="black",fg="white",font=("consols",10))
        self.recover_btn   = Button(self.index,command=self.rec_btn,text="Recover Password",bg="black",fg="white",font=("consols",10))
        self.change_btn    = Button(self.index,command=self.chrec_btn,text="Change Account Details",bg="black",fg="white",font=("consols",10))
        self.exit_btn      = Button(self.index,command=self.index.destroy,text="Exit",bg="black",fg="white",font=("consols",10))

    def build(self):
        self.welcome_label.grid(row=3,column=5,columnspan=7)
        self.login_btn.grid(row=6,column=5,columnspan=7,ipadx=57,pady=5)
        self.newac_btn.grid(row=8,column=5,columnspan=7,ipadx=13,pady=5)
        self.recover_btn.grid(row=10,column=5,columnspan=7,ipadx=20,pady=5)
        self.change_btn.grid(row=11,column=5,columnspan=7,ipadx=5,pady=5)
        self.exit_btn.grid(row=13,column=5,columnspan=7,ipadx=65,pady=5)

    def run(self):
        self.start()
        self.structure()
        self.build()
        self.index.mainloop()



o = tk_index()
o.run()
