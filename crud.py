from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Students:
    def __init__(self,window):
        self.ventana = window
        self.ventana.title('System')
        self.ventana.config(bg='#282C34')
        self.ventana.geometry("1370x750+0+0")
        self.ventana.resizable(False,False)
        #relief es relieve,flat, raised, suken, groove, ridge
        #font=(family='', size= ,weight='')
        title = Label(self.ventana, text='CRUD', bd=10, relief='flat',font=("Helvetica",36,"bold"),bg='#282C34', fg='white')
        title.pack(side='top')
        #Variables
        self.matricula_var = StringVar()
        self.nombre_var = StringVar()
        self.email_var = StringVar()
        self.genero_var = StringVar()
        self.telefono_var = StringVar()
        self.Fechanac_var = StringVar()
        self.buscar_por = StringVar()
        self.buscar_txt = StringVar()

        #Contenedor de izquierda
        Left_frame = Frame(self.ventana, bd=4 , relief='flat', bg='#21252B')
        Left_frame.place(x=20, y=100, width=520, height=620)

        M_Title = Label(Left_frame, text='Control data' ,bg='#21252B',fg='white',font=('Segoe UI',30,'bold'))
        M_Title.grid(row=0 , columnspan=2, pady=20)
        #complementos
        #matricula
        lbmatricula = Label(Left_frame, text='Matricula: ', bg='#21252B', fg='white', font=('Segoe UI',20,'bold'))
        lbmatricula.grid(row=1, column=0, pady=10 , padx=20 , sticky='w')
        txtmatricula = Entry(Left_frame, textvariable=self.matricula_var,font=('Segoe UI',15,'normal'), bd=5, relief='flat')
        txtmatricula.grid(row=1,column=1,pady=10 , padx=20 , sticky='w')
        #nombre
        lbnombre = Label(Left_frame, text='Nombre: ', bg='#21252B', fg='white', font=('Segoe UI',20,'bold'))
        lbnombre.grid(row=2, column=0, pady=10 , padx=20 , sticky='w')
        txtnombre = Entry(Left_frame,textvariable=self.nombre_var, font=('Segoe UI',15,'normal'), bd=5, relief='flat')
        txtnombre.grid(row=2,column=1,pady=10 , padx=20 , sticky='w')
        #correo
        lbcorreo = Label(Left_frame, text='Correo: ', bg='#21252B', fg='white', font=('Segoe UI',20,'bold'))
        lbcorreo.grid(row=3, column=0, pady=10 , padx=20 , sticky='w')
        txtcorreo = Entry(Left_frame,textvariable=self.email_var,font=('Segoe UI',15,'normal'), bd=5, relief='flat')
        txtcorreo.grid(row=3,column=1,pady=10 , padx=20 , sticky='w')
        #genero
        lbgenero = Label(Left_frame, text='Genero: ', bg='#21252B', fg='white', font=('Segoe UI',20,'bold'))
        lbgenero.grid(row=4, column=0, pady=10 , padx=20 , sticky='w')
        cbmgenero = ttk.Combobox(Left_frame,textvariable=self.genero_var,width=9,font=('Segoe UI',15,'normal'), state='readonly')
        cbmgenero['values'] = ("Masculino" ,"Femenino")
        cbmgenero.grid(row=4,column=1,pady=10 , padx=20 , sticky='w')
        #telefono
        lbtelefono = Label(Left_frame, text='Telefono: ', bg='#21252B', fg='white', font=('Segoe UI',20,'bold'))
        lbtelefono.grid(row=5, column=0, pady=10 , padx=20 , sticky='w')
        txttelefono = Entry(Left_frame,textvariable=self.telefono_var,font=('Segoe UI',15,'normal'), bd=5, relief='flat')
        txttelefono.grid(row=5,column=1,pady=10 , padx=20 , sticky='w')
        #fecha nac
        lbfechnac = Label(Left_frame, text='Fecha Nac.: ', bg='#21252B', fg='white', font=('Segoe UI',20,'bold'))
        lbfechnac.grid(row=6, column=0, pady=10 , padx=20 , sticky='w')
        txtfechnac = Entry(Left_frame,textvariable=self.Fechanac_var,font=('Segoe UI',15,'normal'), bd=5, relief='flat')
        txtfechnac.grid(row=6,column=1,pady=10 , padx=20 , sticky='w')
        #domicilio
        lbdirrec = Label(Left_frame, text='Dirreccion: ', bg='#21252B', fg='white', font=('Segoe UI',20,'bold'))
        lbdirrec.grid(row=7, column=0, pady=10 , padx=20 , sticky='w')
        self.txtdirrec = Text(Left_frame,width=32,height=4,font=('Segoe UI',10,'normal'), bd=5, relief='flat')
        self.txtdirrec.grid(row=7,column=1,pady=10 , padx=20 , sticky='w')

        #Frame de botones
        btn_frame = Frame(Left_frame, bd=4, relief='flat', bg='#21252B')
        btn_frame.place(x=40,y=580,width=420)

        btnagregar= Button(btn_frame,text="Agregar",command=self.agregar, width=7,font=('Segoe UI',10,'normal'))
        btnagregar.grid(row=0,column=0 ,padx=10)
        btnupdate= Button(btn_frame, text="Actualizar",command=self.editar ,width=7 ,font=('Segoe UI',10,'normal'))
        btnupdate.grid(row=0,column=1 ,padx=10)
        btndelete= Button(btn_frame, text="Borrar",command=self.eliminar ,width=7 ,font=('Segoe UI',10,'normal'))
        btndelete.grid(row=0,column=2 ,padx=10)
        btnclear= Button(btn_frame,command=self.clear,text="Limpiar Campos", width=14 ,font=('Segoe UI',10,'normal'))
        btnclear.grid(row=0,column=3 ,padx=10)
        #Contenedor de la Derecha
        #el <nav> 
        Right_Frame= Frame(self.ventana, bd=4, relief='flat', bg='#21252B')
        Right_Frame.place(x=550, y=100, width=810 , height=620)
        lbbuscar= Label(Right_Frame, text='Buscar por: ', bg='#21252B', fg='white', font=('Segoe UI',20,'bold'))
        lbbuscar.grid(row=0,column=0,padx=20,pady=10, sticky='w')
        self.cmbbuscar=ttk.Combobox(Right_Frame, width=9,font=('Segoe UI',15,'normal'), state='readonly')
        self.cmbbuscar['values'] = ('Matricula','Nombre','Telefono')
        self.cmbbuscar.grid(row=0,column=1,pady=10,padx=20,sticky='w')

        self.txtfiltro=Entry(Right_Frame, width=20,font=('Segoe UI',11,'normal'), bd=5, relief='flat')
        self.txtfiltro.grid(row=0,column=3,pady=10,padx=20, sticky='w')

        btnaplicarbuscar = Button(Right_Frame,command=self.buscar,text="Buscar", width=7 ,font=('Segoe UI',10,'normal'))
        btnaplicarbuscar.grid(row=0,column=4 ,padx=10)
        btnmostrartodo = Button(Right_Frame, text="Mostrar Todo",command=self.get_registers,width=12 ,font=('Segoe UI',10,'normal'))
        btnmostrartodo.grid(row=0,column=5 ,padx=10)
        #el DataGridView
        GridFrame = Frame(Right_Frame, bd=4, relief='flat' ,bg='#282C34')
        GridFrame.place(x=10,y=70, width=780, height=530)
       #agregando los scrollbars
        scrollx = Scrollbar(GridFrame,orient='horizontal')
        scrolly = Scrollbar(GridFrame,orient='vertical')
        self.Grid=ttk.Treeview(GridFrame, columns=('Matricula','Nombre','Email','Genero','Telefono','Fecha Nac','Direccion'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        #empaquetando los scrolbars y configurandolos con funciones ya definidas de python
        scrollx.pack(side='bottom', fill='x')
        scrolly.pack(side='right', fill='y')
        scrollx.config(command=self.Grid.xview)
        scrolly.config(command=self.Grid.yview)
        #un amanera de madificar el texto de un heading
        self.Grid.heading('Matricula' , text='Matricula')
        self.Grid.heading('Nombre' , text='Nombre')
        self.Grid.heading('Email' , text='Email')
        self.Grid.heading('Genero' , text='Genero')
        self.Grid.heading('Telefono' , text='Telefono')
        self.Grid.heading('Fecha Nac' , text='Fecha Nac')
        self.Grid.heading('Direccion' , text='Direccion')
        #adentrandonos en la configuracion de los anchos de las columns
        self.Grid['show'] = 'headings'
        self.Grid.column('Matricula', width=100)
        self.Grid.column('Nombre', width=200)
        self.Grid.column('Email', width=200)
        self.Grid.column('Genero', width=90)
        self.Grid.column('Telefono', width=200)
        self.Grid.column('Fecha Nac', width=200)
        self.Grid.column('Direccion', width=200)
        #empaquetando y confirmanco dlos cambios realizados en el grid
        #expand le dice que tome cualquier espacio que no esté 
        # asignado a ningún widget y lo distribuya a todos values 1 o 0
        # y both sirve para que abarque ambas posiciones en el grid 
        self.Grid.pack(fill=BOTH, expand=1)

        #vinculando el tree view con el evento con un click
        self.Grid.bind('<ButtonRelease-1>',self.get_seleccion)

        self.get_registers()

    def clear(self):
        #un string vacio 
        self.matricula_var.set("")
        self.nombre_var.set("")
        self.email_var.set("")
        self.genero_var.set("")
        self.telefono_var.set("")
        self.Fechanac_var.set("")
        self.txtdirrec.delete("1.0",END)
    
    def run_query(self, query, parameters = ()):
        conn = pymysql.connect(host="localhost", user="root",password="",database="python_example")
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        #obtiene todos los registros en una lista de tuplas
        result=cursor.fetchall()
        conn.commit()
        conn.close()
        return result
    def get_registers(self):
        query = 'SELECT * FROM estudiantes'
        rows = self.run_query(query)
        if len(rows)!=0:
            self.Grid.delete(*self.Grid.get_children())
            for row in rows:
                self.Grid.insert('',END,values=row)
            
    def agregar(self):
        if self.matricula_var.get()=="" or self.nombre_var.get()=="" or self.email_var.get()=="" or self.genero_var.get()=="" or self.telefono_var.get()=="" or self.Fechanac_var.get()=="":
            messagebox.showerror("Error", "Todos los campos son requeridos!!!")
        else:
            if messagebox.askyesno("Esta Seguro","Se Guardara el registro"):
                query = "INSERT INTO estudiantes VALUES(%s,%s,%s,%s,%s,%s,%s)"
                parametros = (self.matricula_var.get(),self.nombre_var.get(),self.email_var.get(),self.genero_var.get(),self.telefono_var.get(),self.Fechanac_var.get(),self.txtdirrec.get('1.0',END))
                self.run_query(query,parametros)
                messagebox.showinfo("Adelante...", "Se agregó correctamente el registro")
                self.clear()
                self.get_registers()
    #es el manejo de un evento cuando se hace click en un row del treeview
    def get_seleccion(self,event):
        seleccion_row = self.Grid.focus()
        contenido = self.Grid.item(seleccion_row)
        row = contenido['values']
        #print(row)          
        self.matricula_var.set(row[0])
        self.nombre_var.set(row[1])
        self.email_var.set(row[2])
        self.genero_var.set(row[3])
        self.telefono_var.set(row[4])
        self.Fechanac_var.set(row[5])
        self.txtdirrec.delete('1.0',END)
        self.txtdirrec.insert(END,row[6])
    
    def editar(self):
        if self.matricula_var.get()=="" or self.nombre_var.get()=="" or self.email_var.get()=="" or self.genero_var.get()=="" or self.telefono_var.get()=="" or self.Fechanac_var.get()=="":
            messagebox.showerror("Error","Seleccione el registro a actualizar")
        else:
            if messagebox.askyesno("Esta Seguro","Se Editara el registro"):
                query="update estudiantes set nombre=%s,email=%s,genero=%s,telefono=%s,fecha_nac=%s,domicilio=%s where matricula=%s"
                parametros = (
                    self.nombre_var.get(),
                    self.email_var.get(),
                    self.genero_var.get(),
                    self.telefono_var.get(),
                    self.Fechanac_var.get(),
                    self.txtdirrec.get('1.0', END),
                    self.matricula_var.get()
                )
                self.run_query(query,parametros)
                messagebox.showinfo("Adelante...", "Se Edito correctamente el registro")
                self.clear()
                self.get_registers()
    
    def eliminar(self):
        if self.matricula_var.get()=="" or self.nombre_var.get()=="" or self.email_var.get()=="" or self.genero_var.get()=="" or self.telefono_var.get()=="" or self.Fechanac_var.get()=="":
            messagebox.showerror("Error", "Seleccione el registro a eliminar")
        else :
            if messagebox.askyesno("Esta Seguro","Se eliminar el registro"):
                query = "DELETE FROM estudiantes WHERE matricula=%s"
                parametros=(self.matricula_var.get())
                self.run_query(query,parametros)
                messagebox.showinfo("Adelante...", "Se Elimino correctamente el registro")
                self.clear()
                self.get_registers()

    def buscar(self):
        con=pymysql.connect(host="localhost", user="root",password="",database="python_example")
        cur=con.cursor()
        query = "SELECT * FROM estudiantes WHERE "+str(self.cmbbuscar.get())+" LIKE '%"+str(self.txtfiltro.get())+"%'"
        cur.execute(query)
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Grid.delete(*self.Grid.get_children())
            for row in rows:
                self.Grid.insert('',END,values=row)
            con.commit()
        con.close()	

if __name__ =='__main__':
    ventana = Tk()
    obj = Students(ventana)
    ventana.mainloop()





