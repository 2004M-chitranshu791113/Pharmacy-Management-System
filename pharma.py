from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk 
import mysql.connector
from tkinter import messagebox

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1200x700")
        self.root.minsize(1000,600)


        # ==========================================addMed Variable ===============================
        self.addmed_var = StringVar()
        self.refMed_var = StringVar()

        # ==========================================main variable ==================================
        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()

        lbltitle = Label(self.root, text = "    PHARMACY MANAGEMENT SYSTEM", bd = 15, relief = RIDGE, bg = "white", fg = "darkgreen", font = ("times new roman", 50, "bold"), padx = 2, pady = 4)
        lbltitle.pack(side = TOP, fill = X)

        img1 = Image.open("logo.jpg")
        img1 = img1.resize((80, 80), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button (self.root, image = self.photoimg1, borderwidth = 0)
        b1.place(x=15, y=15)

        # ========================DataFrame=======================================
        DataFrame = Frame(self.root, bd = 15, relief=RIDGE, padx = 20)
        DataFrame.pack(fill=BOTH, expand=True, padx=10, pady=5)

        DataFrameLeft = LabelFrame(DataFrame, bd = 10, relief=RIDGE, padx = 20, text = "Medicine Infromation", fg = "darkgreen", font = ("arial", 12, "bold"))
        DataFrameLeft.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        DataFrameRight = LabelFrame(DataFrame, bd = 10, relief=RIDGE, padx = 20, text = "Medicine Add Department", fg = "darkgreen", font = ("arial", 12, "bold"))
        DataFrameRight.pack(side=LEFT, fill=Y, expand=False, padx=5, pady=5)

        # ================================ButtonsFrame======================================
        ButtonFrame = Frame(self.root, bd = 15, relief=RIDGE, padx = 20)
        ButtonFrame.pack(fill=X, padx=10, pady=5)

        # =================================Main Button =====================================
        btnAddData = Button(ButtonFrame, command = self.add_data, text = "ADD MEDICINE", font = ("arial", 12, "bold"), bg = "darkgreen", fg = "white")
        btnAddData.grid(row = 0, column = 0)
        btnUpdateData = Button(ButtonFrame, command = self.update_data, text = "UPDATE", font = ("arial", 12, "bold"), bg = "darkgreen", fg = "white")
        btnUpdateData.grid(row = 0, column = 1)
        btnDeleteData = Button(ButtonFrame, command = self.delete, text = "DELETE", font = ("arial", 12, "bold"), bg = "red", fg = "white")
        btnDeleteData.grid(row = 0, column = 2) 
        btnReset = Button(ButtonFrame, command = self.reset, text = "RESET", font = ("arial", 12, "bold"), bg = "darkgreen", fg = "white")
        btnReset.grid(row = 0, column = 3)
        btnExit = Button(ButtonFrame, text = "EXIT", font = ("arial", 12, "bold"), bg = "red", fg = "white")
        btnExit.grid(row = 0, column = 4)

        # ========================================Search By ==============================================
        lblSearch = Label(ButtonFrame, font=("arial", 16, "bold"), text = "Search By", padx = 2, bg = "orange", fg = "white")
        lblSearch.grid(row = 0, column = 5, sticky = W)

        # ================= variable =================
        self.search_var = StringVar()
        search_combo = ttk.Combobox(ButtonFrame, textvariable = self.search_var, width = 12, font = ("arial", 16, "bold"), state = "readonly")
        search_combo["values"] = ("Ref_no", "MedName", "LotNo")
        search_combo.grid(row = 0, column = 6)
        search_combo.current(0)

        self.searchTxt_var = StringVar()
        txtSearch = Entry(ButtonFrame, textvariable = self.searchTxt_var, bd = 3, relief=RIDGE, width = 24, font = ("arial", 16, "bold"))
        txtSearch.grid(row = 0, column = 7)

        searchButton = Button(ButtonFrame, command = self.search_data, text = "SEARCH", font = ("arial", 13, "bold"), width = 14, bg = "darkgreen", fg = "white")
        searchButton.grid(row = 0, column = 8)
        showAll = Button(ButtonFrame, command = self.fetch_data, text = "SHOW ALL", font = ("arial", 13, "bold"), width = 14, bg = "darkgreen", fg = "white")
        showAll.grid(row = 0, column = 9)
        

        # =====================================Label and Entry ============================
        conn = mysql.connector.connect(host="localhost", username="root", password="7777", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("Select Ref from pharma")
        row = my_cursor.fetchall()

        lblrefno = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Reference No: ", padx = 1)
        lblrefno.grid(row = 0, column = 0, sticky = W)

        ref_combo = ttk.Combobox(DataFrameLeft, textvariable=self.ref_var, width = 27, font = ("arial", 12, "bold"), state = "readonly")
        ref_combo["values"] = row
        ref_combo.grid(row = 0, column = 1)
        if ref_combo["values"]:
            ref_combo.current(0)


        lblCompanyName = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Company Name: ", padx = 1)
        lblCompanyName.grid(row = 1, column = 0, sticky = W)
        txtCompanyName = Entry(DataFrameLeft, textvariable=self.cmpName_var, font = ("arial", 13, "bold"), bg = "white", bd = 2, relief=RIDGE, width = 29)
        txtCompanyName.grid(row = 1, column = 1)

        lblTypeMedicine = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Type of Medicine: ", padx = 1)
        lblTypeMedicine.grid(row = 2, column = 0, sticky = W)
        comTypeMedicine = ttk.Combobox(DataFrameLeft, textvariable=self.typeMed_var, state = "readonly", font = ("arial", 12, "bold"), width = 27)
        comTypeMedicine["values"] = ("Tablet", "Syrup", "Capsules", "Drops", "Injection", "Inhales", "Cream")
        comTypeMedicine.current(0)
        comTypeMedicine.grid(row = 2, column = 1)

        # ============================= Add Medicine ==========================================
        conn = mysql.connector.connect(host="localhost", username="root", password="7777", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select MedName from pharma") 
        med = my_cursor.fetchall()

        lblMedicineName = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Medicine Name: ", padx = 1)
        lblMedicineName.grid(row = 3, column = 0, sticky = W)

        comMedicineName = ttk.Combobox(DataFrameLeft, textvariable=self.medName_var, state = "readonly", font = ("arial", 12, "bold"), width = 27)
        comMedicineName["values"] = med
        if comMedicineName["values"]:
            comMedicineName.current(0)
        comMedicineName.grid(row = 3, column = 1)


        lblLotNo = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Lot No: ", padx = 1)
        lblLotNo.grid(row = 4, column = 0, sticky = W)
        txtLotNo = Entry(DataFrameLeft, textvariable=self.lot_var, font = ("arial", 13, "bold"), bg = "white", bd = 2, relief=RIDGE, width = 29)
        txtLotNo.grid(row = 4, column = 1)

        lblIssueDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Issue Date: ", padx = 1)
        lblIssueDate.grid(row = 5, column = 0, sticky = W)
        txtIssueDate = Entry(DataFrameLeft, textvariable=self.issuedate_var, font = ("arial", 13, "bold"), bg = "white", bd = 2, relief=RIDGE, width = 29)
        txtIssueDate.grid(row = 5, column = 1)

        lblExDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Expiry Date: ", padx = 1)
        lblExDate.grid(row = 6, column = 0, sticky = W)
        txtExDate = Entry(DataFrameLeft, textvariable=self.expdate_var, font = ("arial", 13, "bold"), bg = "white", bd = 2, relief=RIDGE, width = 29)
        txtExDate.grid(row = 6, column = 1)

        lblUses = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Uses: ", padx = 1)
        lblUses.grid(row = 7, column = 0, sticky = W)
        txtUses = Entry(DataFrameLeft, textvariable=self.uses_var, font = ("arial", 13, "bold"), bg = "white", bd = 2, relief=RIDGE, width = 29)
        txtUses.grid(row = 7, column = 1)

        lblSideEffects = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Side Effects: ", padx = 1)
        lblSideEffects.grid(row = 8, column = 0, sticky = W)
        txtSideEffects = Entry(DataFrameLeft, textvariable=self.sideEffect_var, font = ("arial", 13, "bold"), bg = "white", bd = 2, relief=RIDGE, width = 29)
        txtSideEffects.grid(row = 8, column = 1)

        lblPrecWarning = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Warning: ", padx = 1)
        lblPrecWarning.grid(row = 0, column = 2, sticky = W)
        txtPrecWarning = Entry(DataFrameLeft, textvariable=self.warning_var, font = ("arial", 10, "bold"), bg = "white", bd = 2, relief=RIDGE, width = 29)
        txtPrecWarning.grid(row = 0, column = 3)

        lblDasoage = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Dosage: ", padx = 2)
        lblDasoage.grid(row = 1, column = 2, sticky = W)
        txtDosage = Entry(DataFrameLeft, textvariable=self.dosage_var, font = ("arial", 10, "bold"), bg = "white", bd = 2, relief=RIDGE, width = 29)
        txtDosage.grid(row = 1, column = 3)

        lblPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Tablets Price: ", padx = 2)
        lblPrice.grid(row = 2, column = 2, sticky = W)
        txtPrice = Entry(DataFrameLeft, textvariable=self.price_var, font = ("arial", 10, "bold"), bg = "white", bd = 2, relief=RIDGE, width = 29)
        txtPrice.grid(row = 2, column = 3)

        lblProductQt = Label(DataFrameLeft, font=("arial", 12, "bold"), text = "Product QT: ", padx = 2)
        lblProductQt.grid(row = 3, column = 2, sticky = W)
        txtProductQt = Entry(DataFrameLeft, textvariable=self.product_var, font = ("arial", 10, "bold"), bg = "white", bd = 2, relief=RIDGE, width = 29)
        txtProductQt.grid(row = 3, column = 3)

        # ==============================================Images =========================================
        lblhome = Label(DataFrameLeft, font = ("arial", 10, "bold"), text = "STAY HOME STAY SAFE", padx = 35, pady = 2, fg  = "red", bg = "white", width = 30)
        lblhome.place(x = 425, y = 100)

        img2 = Image.open("med.jpg")
        img2 = img2.resize((150, 105), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button (self.root, image = self.photoimg2, borderwidth = 0)
        b1.place(x=490, y=280)

        img3 = Image.open("lab.jpg")
        img3 = img3.resize((160, 105), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button (self.root, image = self.photoimg3, borderwidth = 0)
        b1.place(x=640, y=280)



        # =================================DataFrame Right ============================================
        DataFrameRight = LabelFrame(DataFrame, bd = 10, relief=RIDGE, padx = 20, text = "Medicine Add Department", fg = "darkgreen", font = ("arial", 12, "bold"))
        DataFrameRight.place(x = 810, y = 5, width = 480, height=255)

        img4 = Image.open("img1.jpg")
        img4 = img4.resize((160, 55), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button (self.root, image = self.photoimg4, borderwidth = 0)
        b1.place(x=860, y=160)

        img5 = Image.open("img2.jpg")
        img5 = img5.resize((160, 55), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button (self.root, image = self.photoimg5, borderwidth = 0)
        b1.place(x=1020, y=160)

        img6 = Image.open("img3.jpg")
        img6 = img6.resize((130, 105), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button (self.root, image = self.photoimg6, borderwidth = 0)
        b1.place(x=1180, y=160)

        lblrefno = Label(DataFrameRight, font=("arial", 12, "bold"), text = "Reference No: ", padx = 0)
        lblrefno.place(x = 0, y = 57)
        txtrefno = Entry(DataFrameRight, textvariable = self.refMed_var, font = ("arial", 10, "bold"), bg = "white", bd = 2, relief=RIDGE, width = 22)
        txtrefno.place(x = 135, y = 57)

        lblMedicineName = Label(DataFrameRight, font=("arial", 12, "bold"), text = "Medicine Name: ", padx = 0)
        lblMedicineName.place(x = 0, y = 80)
        txtMedicineName = Entry(DataFrameRight, textvariable = self.addmed_var, font = ("arial", 10, "bold"), bg = "white", bd = 2, relief=RIDGE, width = 22)
        txtMedicineName.place(x = 135, y = 80)

        # ==================================side Frame =============================================
        side_frame=Frame (DataFrameRight, bd=4, relief=RIDGE, bg="white")
        side_frame.place (x=0,y=100, width=295, height=120)
        sc_x=ttk.Scrollbar (side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y=ttk.Scrollbar (side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table=ttk. Treeview(side_frame,column=("ref", "medname"), xscrollcommand=sc_x.set, yscrollcommand = sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack (fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease-1>", self.Medget_cursor)


        # ============================Medicine and buttons ====================================
        down_frame=Frame (DataFrameRight, bd=4, relief=RIDGE, bg="darkgreen")
        down_frame.place (x=300,y=110, width=137, height=115)
        btnAddmed=Button(down_frame, text="ADD", font=("arial", 8, "bold"), width=17, bg="blue", fg="white", pady=2, command=self.AddMed)  
        btnAddmed.grid(row=0, column=0)
        btnUpdatemed=Button (down_frame, text="UPDATE", font=("arial", 8, "bold"), width=17, bg="purple", fg="white", pady=2, command = self.UpdateMed)
        btnUpdatemed.grid(row=1, column=0)
        btnDeletemed=Button (down_frame, text="DELETE", font=("arial",8,"bold"), width=17, bg="red", fg="white", pady=2, command = self.DeleteMed)
        btnDeletemed.grid(row=2, column=0)
        btnClearmed=Button (down_frame, text="CLEAR", font=("arial", 8, "bold"), width=17, bg="orange", fg="white", pady=2, command = self.clearMed)
        btnClearmed.grid(row=3, column=0)

        # ==============================================FrameDetails===========================================
        Framedeatils = Frame(self.root, bd=2, relief=RIDGE)
        Framedeatils.pack(fill=BOTH, expand=True, padx=10, pady=5)



        #==============================================Main Table & scrollbar=======================r====
        Table_frame=Frame (Framedeatils, bd=15, relief=RIDGE, padx=0)
        Table_frame.pack(fill=BOTH, expand=True)

        scroll_x=ttk.Scrollbar (Table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y=ttk.Scrollbar (Table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y) 

        self.pharmacy_table=ttk. Treeview (Table_frame, column=("reg", "companyname", "type", "tabletname", "lotno", "issuedate","expdate", "uses","sideeffect", "warning", "dosage", "price", "productqt"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"
         
        self.pharmacy_table.heading("reg", text="Reference No")
        self.pharmacy_table.heading("companyname", text="Company Name")
        self.pharmacy_table.heading("type", text="Type Of Medicine")
        self.pharmacy_table.heading("tabletname", text="Tablet Name")
        self.pharmacy_table.heading("lotno", text="Lot No")
        self.pharmacy_table.heading("issuedate", text="Issue Date") 
        self.pharmacy_table.heading("expdate", text="Exp Date")
        self.pharmacy_table.heading("uses", text="Uses")
        self.pharmacy_table.heading("sideeffect", text="Side Effect")
        self.pharmacy_table.heading("warning", text="Prec&Warning")
        self.pharmacy_table.heading("dosage", text="Dosage")
        self.pharmacy_table.heading("price", text="Price")
        self.pharmacy_table.heading("productqt", text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1) 

        self.pharmacy_table.column("reg", width=100)
        self.pharmacy_table.column("companyname", width=100)
        self.pharmacy_table.column("type", width=100)   
        self.pharmacy_table.column("tabletname", width=100)
        self.pharmacy_table.column("lotno", width=100)
        self.pharmacy_table.column("issuedate", width=100)
        self.pharmacy_table.column("expdate", width=100)
        self.pharmacy_table.column("uses", width=100)
        self.pharmacy_table.column("sideeffect", width=100)
        self.pharmacy_table.column("warning", width=100)
        self.pharmacy_table.column("dosage", width=100)
        self.pharmacy_table.column("price", width=100)
        self.pharmacy_table.column("productqt", width=100)  
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>", self.get_cursor)


    # ======================Add Medicine Functionality Declaration==============================
    def AddMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="7777", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into pharma(Ref, MedName) values (%s, %s)", ( 
                                                                                    self.refMed_var.get(),
                                                                                    self.addmed_var.get(), 
                                                                            ))
        conn.commit()
        self.fetch_dataMed() 
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success", "Medicine Added")
    def AddMed(self):
        if self.refMed_var.get() == "" or self.addmed_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="7777", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO pharma (Ref, Medname) VALUES (%s, %s)", (
                self.refMed_var.get(),
                self.addmed_var.get()
            ))
            conn.commit()
            self.fetch_dataMed()
            self.Medget_cursor()
            conn.close()
            messagebox.showinfo("Success", "Medicine Added")
        except Exception as e:
            print("Error in AddMed():", e)
            messagebox.showerror("Database Error", f"Something went wrong:\n{str(e)}")

    def fetch_dataMed(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="7777", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM pharma")
            rows = my_cursor.fetchall()
            if rows:
                self.medicine_table.delete(*self.medicine_table.get_children())
            for row in rows:
                self.medicine_table.insert("", END, values=row)

            conn.close()
        except Exception as e:
            print("Error in fetch_dataMed():", e)
            messagebox.showerror("Database Error", f"Failed to fetch data:\n{str(e)}")


        # =====================================MedGet cursor=================================
    def Medget_cursor(self, event=""):           
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content ["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row [1])
        
    def UpdateMed(self):
        if self.refMed_var.get()=="" or self.addmed_var.get() =="":
            messagebox.showerror("Error", "All fields are Required")
        else:
            conn=mysql.connector.connect (host="localhost", username="root", password="Test@123", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharma set Med Name=%s where Ref=%s", (
            self.addmed_var.get(),
            self.refMed_var.get(),
            ))
        conn.commit()
        self.fetch_dataMed()
        conn.close()
        messagebox.showinfo("Success", "Medicine has been Updated")  

    def UpdateMed(self):
        if self.refMed_var.get() == "" or self.addmed_var.get() == "":
            messagebox.showerror("Error", "All fields are Required")
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="7777", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE pharma SET Medname=%s WHERE Ref=%s", (
                self.addmed_var.get(),
                self.refMed_var.get(),
            ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("Success", "Medicine has been Updated")
        except Exception as e:
            print("Error in UpdateMed():", e)
            messagebox.showerror("Database Error", f"Something went wrong:\n{str(e)}")


    def DeleteMed(self):
        if self.refMed_var.get() == "":
            messagebox.showerror("Error", "Reference number is required for deletion")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this medicine?")
        if confirm:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="7777", database="mydata")
                my_cursor = conn.cursor()
                sql = "DELETE FROM pharma WHERE Ref = %s"
                val = (self.refMed_var.get(),)
                my_cursor.execute(sql, val)
                conn.commit()
                self.fetch_dataMed()
                conn.close()
                messagebox.showinfo("Success", "Medicine has been deleted")
            except Exception as e:
                print("Error in DeleteMed():", e)
                messagebox.showerror("Database Error", f"Something went wrong:\n{str(e)}")
    
    def clearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")


    # ==============================================Main Table ===============================================
    def add_data(self):
        if self.ref_var.get() =="" or self.lot_var.get() =="":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn=mysql.connector.connect (host="localhost", username="root", password="7777", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO pharmacy VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
            self.ref_var.get(),
            self.cmpName_var.get(),
            self.typeMed_var.get(),
            self.medName_var.get(),
            self.lot_var.get(),
            self.issuedate_var.get(),
            self.expdate_var.get(),
            self.uses_var.get(),
            self.sideEffect_var.get(),
            self.warning_var.get(),
            self.dosage_var.get(),
            self.price_var.get(),
            self.product_var.get()
            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "data has been inserted")


    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="7777", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM pharmacy")
            rows = my_cursor.fetchall()
            
            if len(rows) != 0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for row in rows:
                    self.pharmacy_table.insert("", END, values=row)
            
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", f"Something went wrong:\n{str(e)}")


    def get_cursor(self, ev=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]

        self.ref_var.set(row[0]),
        self.cmpName_var.set(row [1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row [3]),
        self.lot_var.set(row [4]),
        self.issuedate_var.set(row [5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row [8]),
        self.warning_var.set(row [9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row [11]),
        self.product_var.set(row [12])


    def update_data(self):
        if self.ref_var.get() =="":
            messagebox.showerror("Error", "All Fields Are Required")
        else:
            conn=mysql.connector.connect(host='localhost', username='root', password='7777', database='mydata')
            my_cursor = conn.cursor()
            my_cursor.execute("update pharmacy set cmpName=%s, Type=%s, medname=%s, lot=%s, issuedate=%s, expdate=%s,uses=%s, sideeffect=%s, warning=%s, dosge=%s, price=%s, product=%s where refro=%s", (
                                                                                                                                                                                                            self.cmpName_var.get(),
                                                                                                                                                                                                            self.typeMed_var.get(),
                                                                                                                                                                                                            self.medName_var.get(),
                                                                                                                                                                                                            self.lot_var.get(),
                                                                                                                                                                                                            self.issuedate_var.get(),
                                                                                                                                                                                                            self.expdate_var.get(),
                                                                                                                                                                                                            self.uses_var.get(),
                                                                                                                                                                                                            self.sideEffect_var.get(),
                                                                                                                                                                                                            self.warning_var.get(),
                                                                                                                                                                                                            self.dosage_var.get(),
                                                                                                                                                                                                            self.price_var.get(),
                                                                                                                                                                                                            self.product_var.get(),
                                                                                                                                                                                                            self.ref_var.get()
                                                                                                                                                                                                            ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("UPDATE", "Record has been updated successfully")

    def update_data(self):
        if self.ref_var.get() == "":
            messagebox.showerror("Error", "All Fields Are Required")
            return
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='7777', database='mydata')
            my_cursor = conn.cursor()
            my_cursor.execute("""
                UPDATE pharmacy 
                SET CmpName=%s, TypeMed=%s, MedName=%s, LotNo=%s, Issuedate=%s, Expdate=%s, 
                    Uses=%s, Sideeffect=%s, warning=%s, dosage=%s, Price=%s, product=%s 
                WHERE ref_no=%s
            """, (
                self.cmpName_var.get(),
                self.typeMed_var.get(),
                self.medName_var.get(),
                self.lot_var.get(),
                self.issuedate_var.get(),
                self.expdate_var.get(),
                self.uses_var.get(),
                self.sideEffect_var.get(),
                self.warning_var.get(),
                self.dosage_var.get(),
                self.price_var.get(),
                self.product_var.get(),
                self.ref_var.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("UPDATE", "Record has been updated successfully")
        except Exception as e:
            messagebox.showerror("Database Error", f"Something went wrong:\n{str(e)}")

    
    def delete(self):
        conn=mysql.connector.connect (host="localhost", username="root", password="7777", database="mydata")
        my_cursor = conn.cursor()


        sql="delete from pharmacy where ref_no=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql, val)

        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Delete", "Info deleted successfully")

    def delete(self):
        if self.ref_var.get() == "":
            messagebox.showerror("Error", "Reference No. is required")
            return
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="7777", database="mydata")
            my_cursor = conn.cursor()

            sql = "DELETE FROM pharmacy WHERE ref_no = %s"
            val = (self.ref_var.get(),)
            my_cursor.execute(sql, val)

            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Delete", "Record deleted successfully")
        except Exception as e:
            messagebox.showerror("Database Error", f"Something went wrong:\n{str(e)}")


    def reset(self):
        # self.ref_var.set(""), 
        self.cmpName_var.set(""),
        # self.typeMed_var.set(""),
        # self.medName_var.set(""),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(r""),
        self.price_var.set(r""),
        self.product_var.set(r"")

    def search_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="7777", database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy where "+str(self.search_var.get())+"LIKE"+str(self.serchTxt_var.get())+"%")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def search_data(self):
        if self.search_var.get() == "" or self.searchTxt_var.get() == "":
            messagebox.showerror("Error", "Both search field and text are required")
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="7777", database="mydata")
            my_cursor = conn.cursor()

            query = f"SELECT * FROM pharmacy WHERE {self.search_var.get()} LIKE %s"
            value = ("%" + self.searchTxt_var.get() + "%",)
            my_cursor.execute(query, value)
            rows = my_cursor.fetchall()

            if len(rows) != 0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in rows:
                    self.pharmacy_table.insert("", END, values=i)
            else:
                messagebox.showinfo("Not Found", "No matching records found.")

            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", f"Something went wrong:\n{str(e)}")






if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()