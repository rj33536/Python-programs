import tkinter 
root=tkinter.Tk()
L1 = tkinter.Label(root,text='your name')
E1= tkinter.Entry(root)
L1.grid(row=0,column=0)
E1.grid(row=0,column=1)
L2 = tkinter.Label(root,text='His / Her Name')
E2= tkinter.Entry(root)
L2.grid(row=1,column=0)
E2.grid(row=1,column=1)
def flames ():
    s1=E1.get()
    s2=E2.get()
    flames=0
    relation=['Friends','Love','Affection','Marriage','Enemy','Sister']
    for i in s1:
        t=1
        for j in s2:
           if j==i:
               t=0
        if t:
            flames=flames+1       
    for i in s2:
        t=1
        for j in s1:
           if j==i:
               t=0
        if t:
            flames=flames+1
    L4=tkinter.Label(root,text="Relation :")
    L4.grid(row=3,column=0)
    L3=tkinter.Label(root,text=relation[(flames-1)%6])
    L3.grid(row=3,column=1,columnspan=2)       
B1=tkinter.Button(root,text='ok',command=flames)
B1.grid(row=2,column=0,columnspan=2)
root.mainloop()

    
    
        
