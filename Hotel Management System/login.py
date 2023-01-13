from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


# ===============================Login class============================================================

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"D:\images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"D:\images\LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimage1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimage1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # label
        username = lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=152)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15))
        self.txtuser.place(x=40, y=180, width=270)

        username = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=222)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15))
        self.txtpass.place(x=40, y=250, width=270)

        # =================icon================
        img2 = Image.open(r"D:\images\LoginIconAppl.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimage1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimage1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"D:\images\lock-512.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimage1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimage1.place(x=650, y=393, width=25, height=25)

        # ====================login btn======================
        loginbtn = Button(frame, text="Login", command=self.home_page, font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="red", cursor="hand2", activeforeground="white",
                          activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # ====================registerbtn=========================
        registerbtn = Button(frame, command=self.rigister_window, text="New User Registration",
                             font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black",
                             cursor="hand2", activeforeground="white", activebackground="black")
        registerbtn.place(x=16, y=355, width=160, height=35)

        # ================forgetpass==============================
        forgetpass = Button(frame, command=self.forgot_password_window, text="Forget Password", font=("times new roman", 10, "bold"), fg="white", bg="black",
                            borderwidth=0, cursor="hand2", activeforeground="white", activebackground="black")
        forgetpass.place(x=0, y=385, width=160)

    def rigister_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def home_page(self):

        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        elif self.txtuser.get() == "mohammed" and self.txtpass.get() == "M0hammed":
            messagebox.showinfo("Success", "Welcome Back")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="M0hammed", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))

            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username or Password")
            else:
                open_main = messagebox.askyesno("Yes/No", "Are you Admin ??")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    #===========================reset password============================

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question", parent=self.root2)
        elif self.txt_securityA.get()=="":
            messagebox.showerror("Error","Please Enter Correct Answer", parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter New Password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="M0hammed", database="management")
            my_cursor = conn.cursor()
            qury = ("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_securityA.get(),)
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Please Enter Correct Answer", parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Successful","Your Password has been reset Successfully", parent=self.root2)
                self.root2.destroy()



#==========================forget password===============================================

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter Username First\n type username > Forget Password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="M0hammed", database="management")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error", "Please Enter Valid Username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=("times new ronam", 20 , "bold"), fg="red",  bg= "white")
                l.place(x=0, y=1, relwidth=1)

                # ====================row3
                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 14), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend Name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)

                self.txt_securityA = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_securityA.place(x=50, y=180, width=250)


                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass,font=("times new roman", 15, "bold"),fg="white", bg="green")
                btn.place(x=125, y=290, width=100)











# ===================Register Class============================================================================

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ===================variable==========================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ====================================bg image====================================
        self.bg = ImageTk.PhotoImage(file=r"D:\images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relheight=1, relwidth=1)

        # ====================================bg image====================================
        self.bg1 = ImageTk.PhotoImage(file=r"D:\images\bgimg.png")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # =============== main frame==================================
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen",
                             bg="white")
        register_lbl.place(x=20, y=20)

        # ==============================label and entry===================================
        # ================row1
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # =====================row2
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # ====================row3
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white",
                           fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 14),
                                             state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend Name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # =================row4
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                             fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ==============check button===========================
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions",
                               font=("times new roman", 12, "bold"), bg="white", fg="black", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # ====================button=======================
        img = Image.open(r"D:\images\register-now-button1.jpg")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, fg="black", bg="white", borderwidth=0, cursor="hand2")
        b1.place(x=245, y=420, width=200)

        '''img1 = Image.open(r"D:\images\loginpng.png")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, fg="black", bg="white", borderwidth=0, cursor="hand2")
        b1.place(x=380, y=420, width=200)'''

        # ====================function dec==============================

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select" or self.var_lname.get() == "" or self.var_contact.get() == "" or self.var_securityA.get()=="" or self.var_pass.get()=="" or self.var_confpass.get()=="":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Confirm Password must be Same as Password",parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Check the Terms & Conditions Button",parent=self.root)
        else:

            conn = mysql.connector.connect(host="localhost", username="root", password="M0hammed",
                                           database="management")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User Already exist",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Register Successfully",parent=self.root)
                self.root.destroy()





if __name__ == "__main__":
    main()
