from tkinter import *
from tkinter import messagebox



win = Tk()
win.title("Part B")
win.geometry("500x500")

win.configure(background='powder blue')

Label(win, text="Please Select a method from below",bg='powder blue',font=("Arial",20,'bold')).pack()


# creating Check_Prime_No Function

def Check_Prime_No():
    #win.destroy()
    Cp = Tk()
    Cp.title("Check prime Number")
    Cp.geometry("500x500")
    Cp.configure(background='yellow')

    #creating functionality
    P_No = IntVar()
    EntryBox=Entry(Cp, textvariable=P_No,font=('Arial', 20, 'bold'))
    EntryBox.pack()
    # creating Prime No Btn Functionality
    def Prime_No():
      if P_No.get()/2==0 or P_No.get()/3==0 or P_No.get()/5==0 or P_No.get()/7==0: 
        Label(Cp, text='It is a  Not a prime number',font=('Arial',20,'bold')).pack()
      else:
        Label(Cp, text='It is a prime number',font=('Arial',20,'bold')).pack()  
    Btn = Button(Cp, text='Calculate',font=('Arial',20,'bold'),command=Prime_No,)
    Btn.pack()
    
# creating Radian_to_degree function
def Radian_to_degree():
    #win.destroy()
    Rd = Tk()
    Rd.title('Radian to Degree')
    
    Rd.geometry("500x500")
    Rd.configure(background='yellow')
    Label(Rd, text="Enter Radian value to convert into degrees",font=('Arial',15,'bold')).pack()
    # Creating Radian To Degree Converter Function

    r = IntVar()
    take_input = Entry(Rd, textvariable=r)
    take_input.pack()
    def radian_to_degree():
      messagebox.showinfo("hello", message=r*180/3.14)
    btn= Button(Rd, text='Calculate',font=('Arial',20,'bold'),command=radian_to_degree)
    btn.pack()
    #Label(Rd, text=radian_to_degree(r.get()).pack())
    
    #def Rd_Find():
      
      
      
# creating Degree_to_radian function
def Degree_to_radian():
    #win.destroy()
    Dr = Tk()
    Dr.title('Degree to Radian')
    Dr.geometry("300x300")
# creating Compute_Arc_Length function
def Compute_Arc_Length():
    #win.destroy()
    Cal = Tk()
    Cal.title('Compute Arc Length of an Angle')
    Cal.geometry("300x300")
# creating Compute_Arc_Length function
def Area_of_sector():
    #win.destroy()
    Aos = Tk()
    Aos.title('Compute Area Of Sector')
    Aos.geometry("300x300")
# creating Compute_Arc_Length function
def UnKnown():
    #win.destroy()
    UK = Tk()
    UK.title('Unknown')
    UK.geometry("300x300")
#creating buttons
checkprimeno = Button(win, text="Check Prime",font=('Arial',20,'bold'),command=Check_Prime_No)
checkprimeno.pack()
radiantodegree = Button(win, text="Radians to Degrees",font=('Arial',20,'bold'),command=Radian_to_degree)
radiantodegree.pack()
degreestoradian = Button(win, text="degrees to radian",font=('Arial',20,'bold'),command=Degree_to_radian)
degreestoradian.pack()
arc_length = Button(win, text="Compute Arc Length of an angle",font=('Arial',20,'bold'),command=Compute_Arc_Length)
arc_length.pack()
area_of_sector = Button(win, text="Area of Sector",font=('Arial',20,'bold'),command=Area_of_sector)
area_of_sector.pack()
unknown = Button(win, text="Unknown",font=('Arial',20,'bold'),command=UnKnown)
unknown.pack()
win.mainloop()

