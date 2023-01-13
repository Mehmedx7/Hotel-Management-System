from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #=================variable====================
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()


        # ====================title================================

        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # =======================logo=============================================

        img2 = Image.open(r"D:\images\logohotel.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        #===========================label frame=============================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        #========================labels and entry======================================
        #custRef
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, state="readonly", font=("arial", 12))
        entry_ref.grid(row=0, column=1)

        #Cust Name
        cname = Label(labelframeleft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, width=29, font=("arial", 12))
        txtcname.grid(row=1, column=1)

        # mother name
        lblmname = Label(labelframeleft, text="Mother Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft, textvariable=self.var_mother , width=29, font=("arial", 12))
        txtmname.grid(row=2, column=1)

        # gender combobox
        label_gender = Label(labelframeleft, text="Gender:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender , font=("arial", 12), width=27, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # postcode
        lblPostCode = Label(labelframeleft, text="PostCode:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode = ttk.Entry(labelframeleft, textvariable=self.var_post, width=29, font=("arial", 12))
        txtPostCode.grid(row=4, column=1)

        # mobilenumer
        lblmobile = Label(labelframeleft, text="Mobile:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmobile.grid(row=5, column=0, sticky=W)
        txtmobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, width=29, font=("arial", 12))
        txtmobile.grid(row=5, column=1)

        # Email
        lblEmail = Label(labelframeleft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font=("arial", 12))
        txtEmail.grid(row=6, column=1)

        # nationality
        lblNationality = Label(labelframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_Nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("arial", 12), width=27, state="readonly")
        combo_Nationality["value"] = ("Indian", "American", "Britist")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        # idproof type combobox
        lblIdProof = Label(labelframeleft, text="Id Proof Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_id = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("arial", 12), width=27, state="readonly")
        combo_id["value"] = ("Aadhaar Card", "Driving Licence", "Passport")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        # id number
        lblIdNumber = Label(labelframeleft, text="Id Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number, width=29, font=("arial", 12))
        txtIdNumber.grid(row=9, column=1)

        # address
        lblAddress = Label(labelframeleft, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelframeleft, textvariable=self.var_address, width=29, font=("arial", 12))
        txtAddress.grid(row=10, column=1)

        #========================btns====================================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="ADD", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10, cursor="hand2")
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="UPDATE", command=self.update, font=("arial", 11, "bold"), bg="black", fg="gold", width=10, cursor="hand2")
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="DELETE", command=self.mDelete, font=("arial", 11, "bold"), bg="black", fg="gold", width=10, cursor="hand2")
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="RESET", command=self.reset, font=("arial", 11, "bold"), bg="black", fg="gold", width=10, cursor="hand2")
        btnReset.grid(row=0, column=3, padx=1)

        #========================tabel frame search system===========================
        Tabel_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search", font=("times new roman", 12, "bold"), padx=2)
        Tabel_Frame.place(x=435, y=50, width=860, height=490)

        lblsearchBy = Label(Tabel_Frame, text="Search By:", bg="red", fg="white", font=("arial", 12, "bold"))
        lblsearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.serch_var = StringVar()
        combo_Search= ttk.Combobox(Tabel_Frame, textvariable=self.serch_var, font=("arial", 12), width=24, state="readonly")
        combo_Search["value"] = ("Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtsearch = ttk.Entry(Tabel_Frame, textvariable=self.txt_search, width=24, font=("arial", 13))
        txtsearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Tabel_Frame, text="Search", command=self.search, font=("arial", 11, "bold"), bg="black", fg="gold", width=10, cursor="hand2")
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Tabel_Frame, text="Show All", command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10, cursor="hand2")
        btnShowAll.grid(row=0, column=4, padx=1)

        #======================show data tabel=======================
        Details_Tabel = Frame(Tabel_Frame, bd=2, relief=RIDGE)
        Details_Tabel.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(Details_Tabel, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Details_Tabel, orient=VERTICAL)

        self.Cust_Details_Tabel = ttk.Treeview(Details_Tabel, columns=("ref","name","mother","gender", "post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Tabel.xview)
        scroll_y.config(command=self.Cust_Details_Tabel.yview)

        self.Cust_Details_Tabel.heading("ref", text="Refer No")
        self.Cust_Details_Tabel.heading("name", text="Name")
        self.Cust_Details_Tabel.heading("mother", text="Mother Name")
        self.Cust_Details_Tabel.heading("gender", text="Gender")
        self.Cust_Details_Tabel.heading("post", text="PostCode")
        self.Cust_Details_Tabel.heading("mobile", text="Mobile")
        self.Cust_Details_Tabel.heading("email", text="Email")
        self.Cust_Details_Tabel.heading("nationality", text="Nationality")
        self.Cust_Details_Tabel.heading("idproof", text="Id Proof")
        self.Cust_Details_Tabel.heading("idnumber", text="Id Number")
        self.Cust_Details_Tabel.heading("address", text="Address")

        self.Cust_Details_Tabel["show"] = "headings"

        self.Cust_Details_Tabel.column("ref", width=100)
        self.Cust_Details_Tabel.column("name", width=100)
        self.Cust_Details_Tabel.column("mother", width=100)
        self.Cust_Details_Tabel.column("gender", width=100)
        self.Cust_Details_Tabel.column("post", width=100)
        self.Cust_Details_Tabel.column("mobile", width=100)
        self.Cust_Details_Tabel.column("email", width=100)
        self.Cust_Details_Tabel.column("nationality", width=100)
        self.Cust_Details_Tabel.column("idproof", width=100)
        self.Cust_Details_Tabel.column("idnumber", width=100)
        self.Cust_Details_Tabel.column("address", width=100)

        self.Cust_Details_Tabel.pack(fill=BOTH, expand=1)
        self.Cust_Details_Tabel.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error", "All fields are requaired", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="M0hammed", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                        self.var_ref.get(),
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_mother.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_post.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_nationality.get(),
                                                                                        self.var_id_proof.get(),
                                                                                        self.var_id_number.get(),
                                                                                        self.var_address.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent = self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Somthing went wrong:{str(es)}", parent = self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="M0hammed", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Tabel.delete(*self.Cust_Details_Tabel.get_children())
            for i in rows:
                self.Cust_Details_Tabel.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cuersor(self, event=""):
        cusrsor_row = self.Cust_Details_Tabel.focus()
        content = self.Cust_Details_Tabel.item(cusrsor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error", "Please fill all the fields", parent = self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="M0hammed", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Address=%s where Ref=%s", (
                                                                                                                                                                                    self.var_cust_name.get(),
                                                                                                                                                                                    self.var_mother.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_post.get(),
                                                                                                                                                                                    self.var_mobile.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_nationality.get(),
                                                                                                                                                                                    self.var_id_proof.get(),
                                                                                                                                                                                    self.var_id_number.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_ref.get()

                                                                                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details has been updated successfully", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent = self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="M0hammed", database="management")
            my_cursor = conn.cursor()
            #my_cursor.execute("type here delete uery")

            #second method for execution
            query = "delete from customer where Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="M0hammed", database="management")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.serch_var.get())+" LIKE '%" +str(self.txt_search.get()) +"%'")
        rows = my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Tabel.delete(*self.Cust_Details_Tabel.get_children())
            for i in rows:
                self.Cust_Details_Tabel.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == '__main__':
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()