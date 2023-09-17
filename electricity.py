from tkinter import*
from PIL import ImageTk, Image

class electricity:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+250+100")
        self.root.title("Electricity Charge Calculation")
        self.root.resizable(False,False)

        self.photo_image=ImageTk.PhotoImage(file="electricity.png")
        self.lbl_photo_image=Label(self.root,image=self.photo_image,bd=0).place(x=0,y=0)

        title=Label(self.root,text="Electricity Bill Calculation", font=('times',20,'bold') ,bg='lightblue', anchor='w', padx=20)
        title.place(x=320,y=20,relwidth=1,height=30)

        # Variable

        self.var_reading = IntVar()
        self.var_fixed_amount=IntVar()
        self.var_cal_amount=IntVar()
        self.var_total_amount=IntVar()

        lbl_reading_=Label(self.root,text="Enter your reading", font=('times',25,'bold'), fg='red').place(x=20,y=350)
        entry_reading=Entry(self.root,textvariable=self.var_reading,font=('times',25,'bold'), fg='black', bd=0)
        entry_reading.place(x=320,y=350,width=100)
        entry_reading.focus()


        btn_cal=Button(self.root,text="Calculate",command=self.cal, font=('times',25,'bold'),fg='blue', cursor='hand2').place(x=440, y= 350, width=140, height=40)
        btn_clear=Button(self.root,text="Clear",command=self.clear, font=('times',25,'bold'),fg='blue', cursor='hand2').place(x=600, y= 350, width=140, height=40)

    def cal(self):
        if self.var_reading.get() > 0:
            if self.var_reading.get() >0 and self.var_reading.get() <=30:
                self.var_fixed_amount.set('400')
                self.var_cal_amount.set(30*self.var_reading.get())
                self.var_total_amount.set(self.var_cal_amount.get() +self.var_fixed_amount.get())

            elif self.var_reading.get() >=31 and self.var_reading.get() <=60:
                 self.var_fixed_amount.set('550')
                 self.var_cal_amount.set(37*self.var_reading.get())
                 self.var_total_amount.set(self.var_cal_amount.get() +self.var_fixed_amount.get())

            elif self.var_reading.get() >=61 and self.var_reading.get() <=90:
                 self.var_fixed_amount.set('650')
                 self.var_cal_amount.set(42*self.var_reading.get())
                 self.var_total_amount.set(self.var_cal_amount.get() +self.var_fixed_amount.get())

            elif self.var_reading.get() >=91 and self.var_reading.get() <=120:
                 self.var_fixed_amount.set('1500')
                 self.var_cal_amount.set(50*self.var_reading.get())
                 self.var_total_amount.set(self.var_cal_amount.get() +self.var_fixed_amount.get())

            elif self.var_reading.get() >=121 and self.var_reading.get() <=180:
                 self.var_fixed_amount.set('1500')
                 self.var_cal_amount.set(50*self.var_reading.get())
                 self.var_total_amount.set(self.var_cal_amount.get() +self.var_fixed_amount.get())

            elif self.var_reading.get() >=181:
                 self.var_fixed_amount.set('2000')
                 self.var_cal_amount.set(75*self.var_reading.get())
                 self.var_total_amount.set(self.var_cal_amount.get() +self.var_fixed_amount.get())

        lbl_result=Label(self.root,text="Your bill amount is : " +str(self.var_total_amount.get()),font=('times',20,'bold'),fg='blue').place(x=20,y=400)


    
    def clear(self):
        self.var_reading.set("")
        self.var_fixed_amount.set("")
        self.var_cal_amount.set("")
        self.var_total_amount.set("")
        lbl_result=Label(self.root,text='                                                          ',font=('times',20,'bold'),fg='blue').place(x=20,y=400)

    


if __name__ == "__main__":
    root=Tk()
    obj = electricity(root)
    root.mainloop()

        
