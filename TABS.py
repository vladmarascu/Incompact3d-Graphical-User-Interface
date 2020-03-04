from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from decimal import *

#root=Tk()

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Incompact3d User Interface")
        self.minsize(640, 400)

        tabControl = ttk.Notebook(self)

        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text='Basic Parameters')

        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="Num. Options")

        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="Accuracy")

        self.tab4 = ttk.Frame(tabControl)
        tabControl.add(self.tab4, text="Case")

        tabControl.pack(expan=1, fill="both")
        self.addingWidgets()

    def addingWidgets(self):

        def write_file():

            val_precision = precision.get()
            val_itype = itype.get()
            val_praw = praw.get()
            val_pcol = pcol.get()
            val_NCLX1 = NCLX1.get()
            val_NCLXN = NCLXN.get()
            val_NCLY1 = NCLY1.get()
            val_NCLYN = NCLYN.get()
            val_NCLZ1 = NCLZ1.get()
            val_NCLZN = NCLZN.get()
            val_NX = NX.get()
            val_NY = NY.get()
            val_NZ = NZ.get()
            val_istret = istret.get()
            val_beta = beta.get()
            val_XLX = XLX.get()
            val_YLY = YLY.get()
            val_ZLZ = ZLZ.get()
            val_re = re.get()
            val_initnoise = init_noise.get()
            val_inflownoise = inflow_noise.get()
            val_dt = dt.get()
            val_ifirst = ifirst.get()
            val_ilast = ilast.get()
            val_ilesmod = ilesmod.get()
            val_iscalar = iscalar.get()
            val_iibm=iibm.get()
            val_ifirstder = ifirstder.get()
            val_iseconder = iseconder.get()
            val_itimescheme = itimescheme.get()
            val_irestart = irestart.get()
            val_icheckpoint = icheckpoint.get()
            val_ioutput = ioutput.get()
            val_nvisu = nvisu.get()
            val_nstat = nstat.get()
            val_nu0nu = nu0nu.get()
            val_cnu = cnu.get()
            val_smagcst = smagcst.get()
            val_walecst = walecst.get()
            val_iwall = iwall.get()

            str_val_itype = str(val_itype)
            str_val_praw = str(val_praw)
            str_val_pcol = str(val_pcol)
            str_val_NCLX1 = str(val_NCLX1)
            str_val_NCLXN = str(val_NCLXN)
            str_val_NCLY1 = str(val_NCLY1)
            str_val_NCLYN = str(val_NCLYN)
            str_val_NCLZ1 = str(val_NCLZ1)
            str_val_NCLZN = str(val_NCLZN)
            str_val_NX = str(val_NX)
            str_val_NY = str(val_NY)
            str_val_NZ = str(val_NZ)
            str_val_istret = str(val_istret)
            #str_val_beta = str(format(float(val_beta), '.8f'))
            #str_val_XLX = str(format(float(val_XLX), '.8f'))
            #str_val_YLY = str(format(float(val_YLY), '.8f'))
            #str_val_ZLZ = str(format(float(val_ZLZ), '.8f'))
            str_val_re = str(val_re)
            str_val_initnoise = str(val_initnoise)
            str_val_inflownoise = str(val_inflownoise)
            str_val_dt = str(val_dt)
            str_val_ifirst = str(val_ifirst)
            str_val_ilast = str(val_ilast)
            str_val_ilesmod = str(val_ilesmod)
            str_val_iscalar = str(val_iscalar)
            str_val_iibm = str(val_iibm)
            str_val_ifirstder = str(val_ifirstder)
            str_val_iseconder = str(val_iseconder)
            str_val_itimescheme = str(val_itimescheme)
            str_val_irestart = str(val_irestart)
            str_val_icheckpoint = str(val_icheckpoint)
            str_val_ioutput = str(val_ioutput)
            str_val_nvisu = str(val_nvisu)
            str_val_nstat = str(val_nstat)
            str_val_nu0nu = str(val_nu0nu)
            str_val_cnu = str(val_cnu)
            str_val_smagcst = str(val_smagcst)
            str_val_walecst = str(val_walecst)
            str_val_iwall = str(val_iwall)

            if val_precision == 'single':
                str_val_beta = str(format(Decimal(repr(float(val_beta))), '.8f'))
                str_val_XLX = str(format(Decimal(repr(float(val_XLX))), '.8f'))
                str_val_YLY = str(format(Decimal(repr(float(val_YLY))), '.8f'))
                str_val_ZLZ = str(format(Decimal(repr(float(val_ZLZ))), '.8f'))
            elif val_precision == 'double':
                str_val_beta = str(format(Decimal(repr(float(val_beta))), '.16f'))
                str_val_XLX = str(format(Decimal(repr(float(val_XLX))), '.16f'))
                str_val_YLY = str(format(Decimal(repr(float(val_YLY))), '.16f'))
                str_val_ZLZ = str(format(Decimal(repr(float(val_ZLZ))), '.16f'))

            file = open("users.txt", "w") # w or wb

            file.write('&BasicParam')
            file.write('\nitype = ' + str_val_itype)
            file.write('\np_row = ' + str_val_praw)
            file.write('\np_col = ' + str_val_pcol)
            file.write('\nnx = ' + str_val_NX)
            file.write('\nny = ' + str_val_NY)
            file.write('\nnz = ' + str_val_NZ)
            file.write('\nistret = ' + str_val_istret)
            file.write('\nbeta = ' + str_val_beta)
            file.write('\nxlx = ' + str_val_XLX)
            file.write('\nyly = ' + str_val_YLY)
            file.write('\nzlz = ' + str_val_ZLZ)
            file.write('\nnclx1 = ' + str_val_NCLX1)
            file.write('\nnclxn = ' + str_val_NCLXN)
            file.write('\nncly1 = ' + str_val_NCLY1)
            file.write('\nnclyn = ' + str_val_NCLYN)
            file.write('\nnclz1 = ' + str_val_NCLZ1)
            file.write('\nnclzn = ' + str_val_NCLZN)
            file.write('\niin = 1')
            file.write('\nre = ' + str_val_re)
            file.write('\nu1 = 8')
            file.write('\nu2 = 8')
            file.write('\ninit_noise = ' + str_val_initnoise)
            file.write('\ninflow_noise = ' + str_val_inflownoise)
            file.write('\ndt = ' + str_val_dt)
            file.write('\nifirst = ' + str_val_ifirst)
            file.write('\nilast = ' + str_val_ilast)
            file.write('\nilesmod = ' + str_val_ilesmod)
            file.write('\nnumscalar = ' + str_val_iscalar)
            file.write('\niibm = ' + str_val_iibm)
            file.write('\nivisu = 1')
            file.write('\nipost = 1')
            file.write('\n/End')
            file.write('\n&NumOptions')
            file.write('\nifirstder = ' + str_val_ifirstder)
            file.write('\nisecondder = ' + str_val_iseconder)
            file.write('\nitimescheme = ' + str_val_itimescheme)
            file.write('\nnu0nu = ' + str_val_nu0nu)
            file.write('\ncnu = ' + str_val_cnu)
            file.write('\n/End')
            file.write('\n&InOutParam')
            file.write('\nirestart = ' + str_val_irestart)
            file.write('\nicheckpoint = ' + str_val_icheckpoint)
            file.write('\nioutput = ' + str_val_ioutput)
            file.write('\nnvisu = ' + str_val_nvisu)
            file.write('\n/End')
            file.write('\n&Statistics')
            file.write('\nspinup_time = 0')
            file.write('\nnstat = ' + str_val_nstat)
            file.write('\n/End')
            file.write('\n&LESModel')
            file.write('\njles=1')
            file.write('\nsmagcst=' + str_val_smagcst)
            file.write('\nwalecst=' + str_val_walecst)
            file.write('\niwall=' + str_val_iwall)
            file.write('\n/End')
            file.write('\n&CASE')
            file.write('\ntgv_twod = .FALSE.')
            file.write('\n/End')

            file.close()

        def retrieve_input4():

            val_pfront = pfront.get()

            float_val_pfront = float(val_pfront)

            if float_val_pfront < 0:
                messagebox.showerror('Error', 'pfront has to be greater of equal to 0 !')


        def retrieve_input2():

            val_ifirst = ifirst.get()
            val_ilast = ilast.get()
            val_icheckpoint = icheckpoint.get()
            val_ioutput = ioutput.get()
            val_initnoise = init_noise.get()

            int_val_ifirst = int(val_ifirst)
            int_val_ilast = int(val_ilast)
            int_val_icheckpoint = int(val_icheckpoint)
            int_val_ioutput = int(val_ioutput)
            float_val_initnoise = float(val_initnoise)

            if int_val_ifirst < 1:
                messagebox.showerror('Error', 'ifirst has to be at least equal to 1 !')
            if int_val_ilast < int_val_ifirst:
                messagebox.showerror('Error', 'ilast has to be greater than ifirst !')
            if int_val_ilast % int_val_icheckpoint != 0 or int_val_ilast % int_val_ioutput != 0:
                messagebox.showerror('Error', ' ilast divided by icheckpoint or ioutput has to be an integer !')
            if float_val_initnoise < 0 or float_val_initnoise > 1:
                messagebox.showerror('Error', ' initnoise has to be between 0 and 1 !')


        def retrieve_input1():

            val_NCLX1 = NCLX1.get()
            val_NCLXN = NCLXN.get()
            val_NCLY1 = NCLY1.get()
            val_NCLYN = NCLYN.get()
            val_NCLZ1 = NCLZ1.get()
            val_NCLZN = NCLZN.get()
            val_NX = NX.get()
            val_NY = NY.get()
            val_NZ = NZ.get()
            val_praw = praw.get()
            val_pcol = pcol.get()


            int_val_NCLX1 = int(val_NCLX1)
            int_val_NCLXN = int(val_NCLXN)
            int_val_NCLY1 = int(val_NCLY1)
            int_val_NCLYN = int(val_NCLYN)
            int_val_NCLZ1 = int(val_NCLZ1)
            int_val_NCLZN = int(val_NCLZN)
            int_val_NX = int(val_NX)
            int_val_NY = int(val_NY)
            int_val_NZ = int(val_NZ)
            int_val_praw = int(val_praw)
            int_val_pcol = int(val_pcol)
            if int(val_NX) % 2 != 0:
                int_val_NXcopy = int(val_NX) - 1
            else:
                int_val_NXcopy = int(val_NX)
            if int(val_NY) % 2 != 0:
                int_val_NYcopy = int(val_NY) - 1
            else:
                int_val_NYcopy = int(val_NY)
            if int(val_NZ) % 2 != 0:
                int_val_NZcopy = int(val_NZ) - 1
            else:
                int_val_NZcopy = int(val_NZ)

            #int_val_NXcopy = int(val_NX)
            #int_val_NYcopy = int(val_NY)
            #int_val_NZcopy = int(val_NZ)

            if int_val_NCLX1 == 0 and int_val_NCLXN !=0:
                messagebox.showerror('Error', 'Incorrect (X) Boundary Conditions! Please insert NCLXN again as 0!')
            elif int_val_NCLX1==1 and int_val_NCLXN == 0:
                messagebox.showerror('Error', 'Incorrect (X) Boundary Conditions! Please insert NCLXN again as 1 or 2!')
            elif int_val_NCLX1==2 and int_val_NCLXN == 0:
                messagebox.showerror('Error', 'Incorrect (X) Boundary Conditions! Please insert NCLXN again as 1 or 2!')

            if int_val_NCLY1 == 0 and int_val_NCLYN !=0:
                messagebox.showerror('Error', 'Incorrect (Y) Boundary Conditions! Please insert NCLYN again as 0!')
            elif int_val_NCLY1==1 and int_val_NCLYN == 0:
                messagebox.showerror('Error', 'Incorrect (Y) Boundary Conditions! Please insert NCLYN again as 1 or 2!')
            elif int_val_NCLY1==2 and int_val_NCLYN == 0:
                messagebox.showerror('Error', 'Incorrect (Y) Boundary Conditions! Please insert NCLYN again as 1 or 2!')

            if int_val_NCLZ1 == 0 and int_val_NCLZN !=0:
                messagebox.showerror('Error', 'Incorrect (Z) Boundary Conditions! Please insert NCLZN again as 0!')
            elif int_val_NCLZ1==1 and int_val_NCLZN == 0:
                messagebox.showerror('Error', 'Incorrect (Z) Boundary Conditions! Please insert NCLZN again as 1 or 2!')
            elif int_val_NCLZ1==2 and int_val_NCLZN == 0:
                messagebox.showerror('Error', 'Incorrect (Z) Boundary Conditions! Please insert NCLZN again as 1 or 2!')

            if int_val_NX < 8:
                messagebox.showerror('Error', 'NX has to be greater or equal to 8')
            if int_val_NY < 8:
                messagebox.showerror('Error', 'NY has to be greater or equal to 8')
            if int_val_NZ < 8:
                messagebox.showerror('Error', 'NZ has to be greater or equal to 8')


            if int_val_NCLX1==0 and int_val_NCLXN==0:
                while int_val_NX % 2==0:
                      int_val_NX=int_val_NX/2
                if int_val_NX != 1:
                      messagebox.showerror('Error', 'Incorrect NX')
                else:
                    print('NX COrrect')
            else:
                int_val_NXf=int_val_NX-1
                while int_val_NXf % 2==0:
                      int_val_NXf=int_val_NXf/2
                if int_val_NXf != 1:
                      messagebox.showerror('Error', 'Incorrect NX')
                else:
                    print('NX COrrect')


            if int_val_NCLY1==0 and int_val_NCLYN==0:
                while int_val_NY % 2==0:
                      int_val_NY=int_val_NY/2
                if int_val_NY != 1:
                      messagebox.showerror('Error', 'Incorrect NY')
                else:
                    print('NY COrrect')
            else:
                int_val_NYf=int_val_NY-1
                while int_val_NYf % 2==0:
                      int_val_NYf=int_val_NYf/2
                if int_val_NYf != 1:
                      messagebox.showerror('Error', 'Incorrect NY')
                else:
                    print('NY COrrect')

            if int_val_NCLZ1==0 and int_val_NCLZN==0:
                while int_val_NZ % 2==0:
                      int_val_NZ=int_val_NZ/2
                if int_val_NZ != 1:
                      messagebox.showerror('Error', 'Incorrect NZ')
                else:
                    print('NZ COrrect')
            else:
                int_val_NZf=int_val_NZ-1
                while int_val_NZf % 2==0:
                      int_val_NZf=int_val_NZf/2
                if int_val_NZf != 1:
                      messagebox.showerror('Error', 'Incorrect NZ')
                else:
                    print('NZ COrrect')

            if int_val_praw > int_val_pcol:
                messagebox.showerror('Error', 'PRAW has to be smaller or equal to PCOL')

            if int_val_NXcopy % int_val_praw != 0 or int_val_NXcopy % int_val_pcol != 0 or int_val_NYcopy % int_val_praw != 0 or int_val_NYcopy % int_val_pcol != 0 or int_val_NZcopy % int_val_praw != 0 or int_val_NZcopy % int_val_pcol != 0:
                messagebox.showerror('Error', 'NX,NY,NZ divided by PRAW and PCOL has to be an integer!')

            if int_val_pcol > int_val_NXcopy/2 or int_val_pcol > int_val_NYcopy/2 or int_val_pcol > int_val_NZcopy/2:
                messagebox.showerror('Error', 'Pcol has to be smaller than NX,NY,NZ/2')
            if int_val_praw > int_val_NXcopy/2 or int_val_praw > int_val_NYcopy/2 or int_val_praw > int_val_NZcopy/2:
                messagebox.showerror('Error', 'Praw has to be smaller than NX,NY,NZ/2')

            str1 = 'The no of cores is: '
            str_raw = str(int_val_praw)
            str_col = str(int_val_pcol)
            str_x = ' x '
            str2 = 'The maximum no of cores is: '
            val_min=min(int_val_NXcopy , int_val_NYcopy , int_val_NZcopy)/2
            int_val_min=int(val_min)
            str_max = str(int_val_min)
            str_final = str1 + str_raw + str_x + str_col + ' . ' + str2 + str_max + str_x + str_max + ' . '
            messagebox.showinfo('INFO', str_final)



        # ...................................BASIC PARAMETERS..........................................................................................

        labelFrame1 = ttk.LabelFrame(self.tab1, text="Flow Type (0-6)")
        labelFrame1.grid(column=0, row=0)

        label=ttk.Label(labelFrame1, text="Insert Flow Type:")
        label.grid(column=0,row=0,sticky='W')
        itype = ttk.Combobox(labelFrame1, values=["0","1","2","3","4","5","6"])
        itype.grid(column=1,row=0)
        itype.current(0)

        labelFrame2 = ttk.LabelFrame(self.tab1, text="Boundary Conditions")
        labelFrame2.grid(column=0)

        label = ttk.Label(labelFrame2, text="NCLX1 :")
        label.grid(column=0, row=0, sticky='W')
        NCLX1 = ttk.Combobox(labelFrame2, values=["0","1","2"])
        NCLX1.grid(column=1, row=0)
        NCLX1.current(0)

        label = ttk.Label(labelFrame2, text="NCLXN :")
        label.grid(column=0, row=1, sticky='W')
        NCLXN = ttk.Combobox(labelFrame2, values=["0", "1", "2"])
        NCLXN.grid(column=1, row=1)
        NCLXN.current(0)

        label = ttk.Label(labelFrame2, text="NCLY1 :")
        label.grid(column=2, row=0, sticky='W')
        NCLY1 = ttk.Combobox(labelFrame2, values=["0", "1", "2"])
        NCLY1.grid(column=3, row=0)
        NCLY1.current(0)

        label = ttk.Label(labelFrame2, text="NCLYN :")
        label.grid(column=2, row=1, sticky='W')
        NCLYN = ttk.Combobox(labelFrame2, values=["0", "1", "2"])
        NCLYN.grid(column=3, row=1)
        NCLYN.current(0)

        label = ttk.Label(labelFrame2, text="NCLZ1 :")
        label.grid(column=4, row=0, sticky='W')
        NCLZ1 = ttk.Combobox(labelFrame2, values=["0", "1", "2"])
        NCLZ1.grid(column=5, row=0)
        NCLZ1.current(0)

        label = ttk.Label(labelFrame2, text="NCLZN :")
        label.grid(column=4, row=1, sticky='W')
        NCLZN = ttk.Combobox(labelFrame2, values=["0", "1", "2"])
        NCLZN.grid(column=5, row=1)
        NCLZN.current(0)

        labelFrame3 = ttk.LabelFrame(self.tab1, text="Domain")
        labelFrame3.grid(column=0, row=3)

        label = ttk.Label(labelFrame3, text="XLX :")
        label.grid(column=0, row=4, sticky='W')
        XLX = Entry(labelFrame3)
        XLX.grid(column=1, row=4)

        label = ttk.Label(labelFrame3, text="YLY :")
        label.grid(column=2, row=4, sticky='W')
        YLY = Entry(labelFrame3)
        YLY.grid(column=3, row=4)

        label = ttk.Label(labelFrame3, text="ZLZ :")
        label.grid(column=4, row=4, sticky='W')
        ZLZ = Entry(labelFrame3)
        ZLZ.grid(column=5, row=4)

        labelFrame4 = ttk.LabelFrame(self.tab1, text="Mesh")
        labelFrame4.grid(column=0, row=5)

        label = ttk.Label(labelFrame4, text="NX :")
        label.grid(column=0, row=5, sticky='W')
        NX = Entry(labelFrame4)
        NX.grid(column=1, row=5)

        label = ttk.Label(labelFrame4, text="NY :")
        label.grid(column=2, row=5, sticky='W')
        NY = Entry(labelFrame4)
        NY.grid(column=3, row=5)

        label = ttk.Label(labelFrame4, text="NZ :")
        label.grid(column=4, row=5, sticky='W')
        NZ = Entry(labelFrame4)
        NZ.grid(column=5, row=5)

        labelFrame5 = ttk.LabelFrame(self.tab1, text="Flow Characteristics: ")
        labelFrame5.grid(column=0, row=7)

        label = ttk.Label(labelFrame5, text="Insert Reynolds Number :")
        label.grid(column=0, row=7, sticky='W')
        re= Entry(labelFrame5)
        re.grid(column=1, row=7)

        labelFrame6 = ttk.LabelFrame(self.tab1, text="Domain decomposition")
        labelFrame6.grid(column=0, row=6)

        label = ttk.Label(labelFrame6, text="P RAW :")
        label.grid(column=0, row=6, sticky='W')
        praw = Entry(labelFrame6)
        praw.grid(column=1, row=6)

        label = ttk.Label(labelFrame6, text="P COL :")
        label.grid(column=2, row=6, sticky='W')
        pcol = Entry(labelFrame6)
        pcol.grid(column=3, row=6)

        labelFrame7 = ttk.LabelFrame(self.tab1, text="Precision")
        labelFrame7.grid(column=0, row=8)

        label = ttk.Label(labelFrame7, text="Precision is :")
        label.grid(column=0, row=8, sticky='W')
        precision = ttk.Combobox(labelFrame7, values=["single", "double"])
        precision.grid(column=1, row=8)
        precision.current(0)

        buttonCommit1 = Button(self.tab1, text="Check for errors", command=lambda: retrieve_input1())
        buttonCommit1.grid(column=0, row=9)

        buttonFile = Button(self.tab1, text="Create Input File", command=lambda: write_file())
        buttonFile.grid(column=0, row=10)

        #......................................NUM. OPTIONS......................................................................................


        label = ttk.Label(self.tab2, text="Insert Stretch Type :")
        label.grid(column=0, row=0, sticky='E')
        istret = ttk.Combobox(self.tab2, values=["0", "1", "2", "3"])
        istret.grid(column=1, row=0)
        istret.current(0)

        label = ttk.Label(self.tab2, text="beta :")
        label.grid(column=2, row=0, sticky='E')
        beta = Entry(self.tab2)
        beta.grid(column=3, row=0)

        label = ttk.Label(self.tab2, text="dt :")
        label.grid(column=0, row=1, sticky='E')
        dt = Entry(self.tab2)
        dt.grid(column=1, row=1)

        label = ttk.Label(self.tab2, text="Time scheme :")
        label.grid(column=0, row=2, sticky='E')
        itimescheme = ttk.Combobox(self.tab2, values=["1", "2"])
        itimescheme.grid(column=1, row=2)
        itimescheme.current(0)

        label = ttk.Label(self.tab2, text="First iteration :")
        label.grid(column=0, row=3, sticky='E')
        ifirst = Entry(self.tab2)
        ifirst.grid(column=1, row=3)

        label = ttk.Label(self.tab2, text="Last iteration :")
        label.grid(column=2, row=3, sticky='E')
        ilast = Entry(self.tab2)
        ilast.grid(column=3, row=3)

        label = ttk.Label(self.tab2, text="iScalar :")
        label.grid(column=0, row=4, sticky='E')
        iscalar = ttk.Combobox(self.tab2, values=["0", "1"])
        iscalar.grid(column=1, row=4, sticky='E')
        iscalar.current(0)

        label = ttk.Label(self.tab2, text="Restart:")
        label.grid(column=0, row=5, sticky='E')
        irestart = ttk.Combobox(self.tab2, values=["0", "1"])
        irestart.grid(column=1, row=5, sticky='E')
        irestart.current(0)

        label = ttk.Label(self.tab2, text="nstat :")
        label.grid(column=0, row=6, sticky='E')
        nstat = Entry(self.tab2)
        nstat.grid(column=1, row=6)

        label = ttk.Label(self.tab2, text="nvisu :")
        label.grid(column=2, row=6, sticky='E')
        nvisu = Entry(self.tab2)
        nvisu.grid(column=3, row=6)

        label = ttk.Label(self.tab2, text="Output :")
        label.grid(column=0, row=7, sticky='E')
        ioutput = Entry(self.tab2)
        ioutput.grid(column=1, row=7)

        label = ttk.Label(self.tab2, text="Checkpoint :")
        label.grid(column=0, row=8, sticky='E')
        icheckpoint = Entry(self.tab2)
        icheckpoint.grid(column=1, row=8)

        label = ttk.Label(self.tab2, text="Initial Noise :")
        label.grid(column=0, row=9, sticky='E')
        init_noise = Entry(self.tab2)
        init_noise.grid(column=1, row=9)

        label = ttk.Label(self.tab2, text="Inflow Noise :")
        label.grid(column=2, row=9, sticky='E')
        inflow_noise = Entry(self.tab2)
        inflow_noise.grid(column=3, row=9)

        label = ttk.Label(self.tab2, text="IIBM :")
        label.grid(column=0, row=10, sticky='E')
        iibm = ttk.Combobox(self.tab2, values=["0", "IBN U=0", "IBN POL"])
        iibm.grid(column=1, row=10)
        iibm.current(0)

        buttonCommit2 = Button(self.tab2, text="Check for errors", command=lambda: retrieve_input2())
        buttonCommit2.grid(column=2, row=11)

        #......................................ACCURACY......................................................................................

        label = ttk.Label(self.tab3, text="ifirstder :")
        label.grid(column=0, row=0, sticky='E')
        ifirstder = ttk.Combobox(self.tab3, values=["1", "2"])
        ifirstder.grid(column=1, row=0)
        ifirstder.current(0)

        label = ttk.Label(self.tab3, text="iseconder :")
        label.grid(column=2, row=0, sticky='E')
        iseconder = ttk.Combobox(self.tab3, values=["1", "2"])
        iseconder.grid(column=3, row=0)
        iseconder.current(0)

        label = ttk.Label(self.tab3, text="ilesmod :")
        label.grid(column=0, row=1, sticky='E')
        ilesmod = ttk.Combobox(self.tab3, values=["0", "1"])
        ilesmod.grid(column=1, row=1)
        ilesmod.current(0)

        label = ttk.Label(self.tab3, text="nu0nu :")
        label.grid(column=0, row=2, sticky='E')
        nu0nu = Entry(self.tab3)
        nu0nu.grid(column=1, row=2)

        label = ttk.Label(self.tab3, text="cnu :")
        label.grid(column=2, row=2, sticky='E')
        cnu = Entry(self.tab3)
        cnu.grid(column=3, row=2)

        label = ttk.Label(self.tab3, text="jles :")
        label.grid(column=0, row=3)
        jles = ttk.Combobox(self.tab3, values=["SNAG", "DMNSNAG"])
        jles.grid(column=1, row=3)
        jles.current(0)

        label = ttk.Label(self.tab3, text="smagcst :")
        label.grid(column=0, row=4, sticky='E')
        smagcst = Entry(self.tab3)
        smagcst.grid(column=1, row=4)

        label = ttk.Label(self.tab3, text="walecst :")
        label.grid(column=0, row=5, sticky='E')
        walecst = Entry(self.tab3)
        walecst.grid(column=1, row=5)

        label = ttk.Label(self.tab3, text="iwall :")
        label.grid(column=0, row=6, sticky='E')
        iwall = ttk.Combobox(self.tab3, values=["True", "False"])
        iwall.grid(column=1, row=6)
        iwall.current(0)


        buttonCommit3 = Button(self.tab3, text="Check for errors", command=lambda: retrieve_input3())
        buttonCommit3.grid(column=2, row=7)

        #......................................CASE......................................................................................

        label = ttk.Label(self.tab4, text="If TGV ")
        label.grid(column=0, row=0)
        label = ttk.Label(self.tab4, text="2D :")
        label.grid(column=0, row=1, sticky='E')
        d2 = ttk.Combobox(self.tab4, values=["True", "False"])
        d2.grid(column=1, row=1)
        d2.current(0)

        label = ttk.Label(self.tab4, text="If LOCK-EXCH ")
        label.grid(column=0, row=2)
        label = ttk.Label(self.tab4, text="pfront :")
        label.grid(column=0, row=3, sticky='E')
        pfront = Entry(self.tab4)
        pfront.grid(column=1, row=3)

        buttonCommit4 = Button(self.tab4, text="Check for errors", command=lambda: retrieve_input4())
        buttonCommit4.grid(column=1, row=4)


app = Root()
app.mainloop()