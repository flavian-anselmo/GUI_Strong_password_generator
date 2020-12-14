#password generator with python_Tkinter
from tkinter import*
from random import*
from tkinter.font import Font
from string import punctuation,ascii_letters
from tkinter import messagebox

win=Tk()
win.geometry('500x520')
win.title("password_generator@anselmo.Jr")
win.resizable(False,False)

#shuffle(list)
#sample(var,sample)

#create a list of characters,alphabets and numbers
#iam going to use ascii lettersto generate a list
#iam using punctuations to generate characters 

alpha=[]#list to store our alphabets
pun=list(punctuation)#list to store our punctiations
nums=[j for j in range(1,11)]#use list comprehension to create a list of nums
stren_list= ['very_strong',
            'strong'
            ]#the strength of password

for letters in ascii_letters:
    alpha.append(letters)
#alphabets created
#punctuations created 
cont_list_one=(alpha+pun+nums)#very strong passwords
cont_list_two=(alpha+nums)#strong passwords 

def generate_pwd():
    #once the button is clicked this function will be excecuted
    try:
        if strength_click.get()==stren_list[0]:
            #verystrong password
            """concantenate all lists to generate a password with
                punctuations,alphabets and numeric values
            """ 
            #cont_list=(alpha+pun+nums)
            #shuffle the list
            #the program will generate some number of passwords
            if int(len_entry.get())>=8:
              #password should be greater than 8  
                counter_one=0
                while counter_one!=int(number_pwd_entry.get()):
                    pwd_one=shuffle(cont_list_one)
                    pwd_one_very_strong=sample(cont_list_one,int(len_entry.get()))
                    print(str(pwd_one_very_strong))
                    pwd_list_box.insert(END,pwd_one_very_strong)
                    counter_one+=1
                if counter_one==int(number_pwd_entry.get()):
                        messagebox.showinfo("passord_creation_info",
                        "{}  passwords have been generated".format(int(number_pwd_entry.get())))      
                len_entry.delete(0,END)
                number_pwd_entry.delete(0,END)
            elif(int(len_entry.get()))<8:
                messagebox.showerror("password_length_error",
                "password_cannot have a length less than 8 characters")    
        if int(len_entry.get())>8:
            #the password should be greater than 8
            if strength_click.get()==stren_list[1]:
                #strong_password
                """
                only get passwords with 
                alpahbets and numeric passwords
                """  
                #shuffle again
                #some number of passwords will be generated 
                counter_two=0
                while counter_two!=int(number_pwd_entry.get()):
                    pwd_two=shuffle(cont_list_two)
                    pwd_two_strong=sample(cont_list_two,int(len_entry.get()))
                    print(str(pwd_two_strong))
                    pwd_list_box.insert(END,pwd_two_strong) 
                    counter_two+=1
                if counter_two==int(number_pwd_entry.get()):
                            messagebox.showinfo("passord_creation_info",
                            "{}  passwords have been generated".format(int(number_pwd_entry.get())))    
                len_entry.delete(0,END)
                number_pwd_entry.delete(0,END)
        elif(int(len_entry.get()))<8:
            messagebox.showerror("password_creation_error","password_cannot have less than 8 characters")        
                
    except:
        if  len(len_entry.get())==0:
        #showerror
            messagebox.showerror("length_EntryBox_error",
                                        "Enter the  length of password ")
        elif len(number_pwd_entry.get())==0:
            messagebox.showerror("number_of_password_Error",
                                    "Enter the number of password to generate")    
#end of function
#-------------------------------------------------------------------------
#THE USER_INTERFACE
head=Label(win,text="STRONG PASSWORD GENERATOR",
                        font=("Times new roman",20),fg="green")                 
head.pack()
tail=Label(win,text="crafted by anselmo.JR ",
                        font=("Times new roman",15),fg="red")                 
tail.pack()
strength_click=StringVar()
#set the default as very_strong
strength_click.set(stren_list[0])
#password_strength label
my_font = Font(size=12)
pwd_strength=Label(win,text="password_strength",
                        font=("Times new roman",12),fg="blue")                 
pwd_strength.pack() 
#drop down list
drop_down=OptionMenu(win,strength_click,*stren_list)
drop_down.pack()
#label for length entry
pwd_length=Label(win,text="password_length",
                        font=("Times new roman",12),fg="blue")                 
pwd_length.pack() 
#entry_box
len_entry=Entry(win,width=25)
len_entry.pack()
#lable for number of passwords
pwd_number=Label(win,text="number of passwords to generate",
                        font=("Times new roman",12),fg="blue")                 
pwd_number.pack() 
#number of passwords to generate 
number_pwd_entry=Entry(win,width=25)
number_pwd_entry.pack()

#button to click to generate  the password
generate_bt_click=Button(win,text="get_password",
                        command=generate_pwd,padx=15,bg="green")
generate_bt_click.pack()

#list to display the passwaords
pwd_list_box=Listbox(win,width=80,height=15)
scroll=Scrollbar(win,command=pwd_list_box.yview)
pwd_list_box.configure(yscrollcommand=scroll.set)
pwd_list_box.pack(side=LEFT)
scroll.pack(side=RIGHT,fill=Y)


win.mainloop()
#end of program
#-------------------------------------------------------------------------
