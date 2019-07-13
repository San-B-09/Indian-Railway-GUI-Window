import requests, json, tkinter
tk = tkinter

class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}

        for F in (MainPage, PNRPage, LiveStatus):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #adding the railway icon
        photo = tk.PhotoImage(file='C://Users//bijaw//Desktop//railway icon.gif')
        image_label = tk.Label(self, image=photo)
        image_label.image = photo
        image_label.grid(row=1, column=3)

        #title of our GUI
        label = tk.Label(self, text="INDIAN RAILWAYS", fg='#191970')
        label.config(font=('Broadway', 40))
        label.grid(row=0, column=3)  # displaying the name

        label2 = tk.Label(self, text='BOOK YOUR TICKET', fg='#8B0000')
        label2.config(font=('Times New Roman', 25))
        label2.grid(row=2, column=3)

        #from
        from_prompt = tk.Label(self, text="From :", fg='#696969')
        from_prompt.config(font=('Times New Roman', 12))
        from_entry = tk.Entry(self)
        from_entry.config(font=('Times New Roman', 12))

        #to
        to_prompt = tk.Label(self, text="To :", fg='#696969')
        to_prompt.config(font=('Times New Roman', 12))
        to_entry = tk.Entry(self)
        to_entry.config(font=('Times New Roman', 12))

        #date
        date_prompt = tk.Label(self, text="Date (dd-mm-yyyy) :", fg='#696969')
        date_prompt.config(font=('Times New Roman', 12))
        date_entry = tk.Entry(self)
        date_entry.config(font=('Times New Roman', 12))

        from_prompt.grid(row=3, column=2, sticky="E")
        to_prompt.grid(row=4, column=2, sticky="E")
        date_prompt.grid(row=5, column=2, sticky="E")
        from_entry.grid(row=3, column=3)
        to_entry.grid(row=4, column=3)
        date_entry.grid(row=5, column=3)

        #check buttons
        div_bool, jour_bool, flex_date = 0, 1, 2  # setting divyang, flexible wiht date and journalist concession to zero
        flex_w_date = tk.Checkbutton(self, text="Flexible with Date", fg='#696969', variable=flex_date)
        flex_w_date.config(font=('Times New Roman', 12))
        flex_w_date.grid(row=7, column=2, sticky="E")
        divyang = tk.Checkbutton(self, text="Divyang", fg='#696969', variable=div_bool)
        divyang.config(font=('Times New Roman', 12))
        divyang.grid(row=7, column=3, sticky="E")
        journalist = tk.Checkbutton(self, text="Journalist Concession", fg='#696969', variable=jour_bool)
        journalist.config(font=('Times New Roman', 12))
        journalist.grid(row=7, column=4, sticky="E")

       #drop down list of train classes
        menu_frame = tk.Frame(self)
        menu_frame.grid(row=6, column=3, sticky=("N", "W", "E", "S"))

        choices = {'All Classes', 'Anubhuti Class (EA)', 'AC First Class (1A)', 'Exec. Chair Car (EC)',
                   'AC 2 Tier (2A)', 'First Class (FC)', 'AC 3 Tier (3A)', 'AC 3 Economy (3E)', 'AC Chair car (CC)',
                   'Sleeper (SL)', 'Second Sitting (2S)'}
        class_var = tk.StringVar(self)  # tkinter variable
        class_var.set('All Classes')  # set the default option

        popupMenu = tk.OptionMenu(menu_frame, class_var, *choices)
        tk.Label(menu_frame, text="Choose a Class :", fg='#696969').grid(row=6, column=2, sticky="E")
        popupMenu.grid(row=6, column=5, sticky="E")

        # on changed dropdown value
        def change_dropdown(*args):
            print(class_var.get())

        # link function to change dropdown
        class_var.trace('w', change_dropdown)

        # buttons directing to different windows

        find_train = tk.Button(self, text='Find Trains', bg='blue', fg='white')
        # find_train.config(font=('Times New Roman', 12))
        pnr = tk.Button(self, text="PNR Status", bg='blue', fg='white', command=lambda: controller.show_frame(PNRPage))
        # pnr.config(font=('Times New Roman', 12))
        liv_status = tk.Button(self, text='Live Status', bg='blue', fg='white',
                               command=lambda: controller.show_frame(LiveStatus))
        # liv_status.config(font=('Times New Roman', 12))

        find_train.grid(row=8, column=3)
        pnr.grid(row=10, column=2)
        liv_status.grid(row=10, column=4)


class PNRPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title_label = tkinter.Label(self, text='PNR ENQUIRY', fg='#191970')
        title_label.config(font=('Broadway', 30))
        title_label.grid(row=0, column=1, columnspan = 3)

        '''photo2 = tk.PhotoImage(self, file='C://Users//bijaw//Desktop//output-onlinepngtools.gif')
        image_label2 = tk.Label(self, image=photo2)
        image_label2.image = photo2
        image_label2.grid(row=1, column=2)'''

        expression = ""
        # 'StringVar()' is used to get the instance of input field
        global input_text
        input_text = tkinter.StringVar()
        tkinter.Label(self, text="PNR No.: ").grid(row=2, column = 1, columnspan =2 )
        pnr_entry = tk.Entry(self, textvariable=input_text)
        pnr_entry.config(font=('Times New Roman', 12))
        pnr_entry.grid(row=2, column=2, columnspan = 2)
        submit = tkinter.Button(self, text="Submit", fg="#4169E1", command=lambda: pnr())
        submit.config(font=('Times New Roman', 12))
        submit.grid(row=3, column=1)
        clear = tkinter.Button(self, text="Clear", fg="#4169E1", command=lambda: btn_clear())
        clear.config(font=('Times New Roman', 12))
        clear.grid(row=3, column=2)
        back = tk.Button(self, text="Back to Main Page", fg="#D3D3D3", command=lambda: controller.show_frame(MainPage))
        back.config(font=('Times New Roman', 12))
        back.grid(row=3, column=3)

        '''def show_text():
            global expression
            expression = input_text.get()
            tk.Label(self, text = expression).grid(row = 2, column = 0)'''

        def btn_clear():
            input_text.set("")

        def pnr():
            global expression

            expression = input_text.get()
            if (expression != ""):
                # window1.hide()
                # tkinter.Label(window2, text=expression).pack()
                info_list, passenger_lst = pnr_status()

                l0 = tkinter.Label(self, text="You enquired for PNR No.: " + expression, bg="#6495ED",width=150)
                l0.grid(row=4, column=0, columnspan=5, pady=10)

                if (type(info_list).__name__ == "str"):
                    t=1
                    ll = tkinter.Label(self, text=info_list, fg="red")
                    ll.config(font=('Times New Roman', 12))
                    ll.grid(row=5, column=0, columnspan=5)
                    #back = tkinter.Button(window2, text="Back", fg="orange", command=window2.quit()).grid(row=4, column=0)
                    j = 6
                    c = 2
                else:
                    t=2
                    l1 = tkinter.Label(self, text="Train Number", bg="#F0E68C", width=30)
                    l1.config(font=('Times New Roman', 12))
                    l1.grid(row=5, column=0)
                    l2 = tkinter.Label(self, text="Train Name", bg="#F0E68C", width=30)
                    l2.config(font=('Times New Roman', 12))
                    l2.grid(row=5, column=1)
                    l3 = tkinter.Label(self, text="Boadring Date", bg="#F0E68C", width=30)
                    l3.config(font=('Times New Roman', 12))
                    l3.grid(row=5, column=2)
                    l4 = tkinter.Label(self, text="From", bg="#F0E68C", width=30)
                    l4.config(font=('Times New Roman', 12))
                    l4.grid(row=5, column=3)
                    l5 = tkinter.Label(self, text="To", bg="#F0E68C", width=30)
                    l5.config(font=('Times New Roman', 12))
                    l5.grid(row=5, column=4)
                    l6 = tkinter.Label(self, text="Reservation Upto", bg="#F0E68C", width=30)
                    l6.config(font=('Times New Roman', 12))
                    l6.grid(row=7, column=0)
                    l7 = tkinter.Label(self, text="Boarding Point", bg="#F0E68C", width=30)
                    l7.config(font=('Times New Roman', 12))
                    l7.grid(row=7, column=1)

                    l8 = tkinter.Label(self, text=info_list[0], bg="#F0E68C", width=30)
                    l8.config(font=('Times New Roman', 12))
                    l8.grid(row=6, column=0, pady = 10)
                    l10 = tkinter.Label(self, text=info_list[1], bg="#F0E68C", width=30)
                    l10.config(font=('Times New Roman', 12))
                    l10.grid(row=6, column=1, pady = 10)
                    l11 = tkinter.Label(self, text=info_list[2], bg="#F0E68C", width=30)
                    l11.config(font=('Times New Roman', 12))
                    l11.grid(row=6, column=2, pady = 10)
                    l12 = tkinter.Label(self, text=info_list[3], bg="#F0E68C", width=30)
                    l12.config(font=('Times New Roman', 12))
                    l12.grid(row=6, column=3, pady = 10)
                    l13 = tkinter.Label(self, text=info_list[4], bg="#F0E68C", width=30)
                    l13.config(font=('Times New Roman', 12))
                    l13.grid(row=6, column=4, pady = 10)
                    l14 = tkinter.Label(self, text=info_list[5], bg="#F0E68C", width=30)
                    l14.config(font=('Times New Roman', 12))
                    l14.grid(row=8, column=0, pady = 10)
                    l15 = tkinter.Label(self, text=info_list[6], bg="#F0E68C", width=30)
                    l15.config(font=('Times New Roman', 12))
                    l15.grid(row=8, column=1, pady = 10)

                    l16 = tkinter.Label(self, text="Passenger No.", bg="#F0E68C", width=30)
                    l16.config(font=('Times New Roman', 12))
                    l16.grid(row=9, column=0,  pady = 10)
                    l17 = tkinter.Label(self, text="Current Status", bg="#F0E68C", width=30)
                    l17.config(font=('Times New Roman', 12))
                    l17.grid(row=9, column=1,  pady = 10)
                    l18 = tkinter.Label(self, text="Booking Status", bg="#F0E68C", width=30)
                    l18.config(font=('Times New Roman', 12))
                    l18.grid(row=9, column=2,  pady = 10)
                    j = 10
                    c = 3
                    l = ["0" for i in range(len(passenger_lst)*3)]
                    i = 0
                    if(passenger_lst != "0"):
                        for passenger in passenger_lst:
                            l[i] = tkinter.Label(self, text=(passenger['no']) + 1, width=30)
                            l[i].grid(row=j, column=0)
                            i += 1
                            l[i] = tkinter.Label(self, text=passenger['current_status'], width=30)
                            l[i].grid(row=j, column=1)
                            i += 1
                            l[i] = tkinter.Label(self,  text=passenger['booking_status'], width=30)
                            l[i].grid(row=j, column=2)
                            j += 1
                            i += 1
                New_pnr = tk.Button(self, text="New PNR", fg="purple", command=lambda: clear())
                New_pnr.grid(row=j, column=c)

            def clear():
                l0.grid_remove()
                if(t==1):
                    ll.grid_remove()
                elif(t==2):
                    l1.grid_remove()
                    l2.grid_remove()
                    l3.grid_remove()
                    l4.grid_remove()
                    l5.grid_remove()
                    l6.grid_remove()
                    l7.grid_remove()
                    l8.grid_remove()
                    l10.grid_remove()
                    l11.grid_remove()
                    l12.grid_remove()
                    l13.grid_remove()
                    l14.grid_remove()
                    l15.grid_remove()
                    l16.grid_remove()
                    l17.grid_remove()
                    l18.grid_remove()
                    for i in range(len(l)):
                        l[i].grid_remove()
                New_pnr.grid_remove()


class LiveStatus(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title_label2 = tkinter.Label(self, text='LIVE STATUS ENQUIRY', fg='#191970')
        title_label2.config(font=('Broadway', 30))
        title_label2.grid(row=0, column=2)
        '''photo3 = tkinter.PhotoImage(self, file='railway_mascot.png')
        image_label3 = tkinter.Label(self, image=photo3)
        image_label3.grid(row=1, column=2)'''
        expression = ""
        # 'StringVar()' is used to get the instance of input field
        global input_train, station, date
        input_train = tkinter.StringVar()
        station = tkinter.StringVar()
        date = tkinter.StringVar()
        tkinter.Label(self, text="Train No.: ", font=('Times New Roman', 12)).grid(row=2, column=1)
        train = tk.Entry(self, textvariable=input_train)
        train.config(font=('Times New Roman', 12))
        train.grid(row=2, column=2)
        tkinter.Label(self, text="Station : ", font=('Times New Roman', 12)).grid(row=3, column=1)
        tkinter.Label(self, text="(Station Initials)", font=('Times New Roman', 12)).grid(row=3, column=3)
        stn = tk.Entry(self, textvariable=station)
        stn.config(font = ('Times New Roman', 12))
        stn.grid(row=3, column=2)
        #stn.insert(0, "Station initials")
        tkinter.Label(self, text="Date: ").grid(row=4, column=1)
        tkinter.Label(self, text="(dd-mm-yyyy)").grid(row=4, column=3)
        dt = tk.Entry(self, textvariable=date)
        dt.config(font=('Times New Roman', 12))
        dt.grid(row=4, column=2)
        t = 100
        #dt.insert(0,"dd-mm-yyyy")
        submit = tkinter.Button(self, text="Submit", fg="#4169E1", command = lambda: train_status())
        submit.config(font=('Times New Roman', 12))
        submit.grid(row=5, column=1)
        clear = tkinter.Button(self, text="Clear", fg="#4169E1", command = lambda: btn_clear())
        clear.config(font=('Times New Roman', 12))
        clear.grid(row=5, column=2)
        back = tk.Button(self, text = "Back to Main Page",fg="#D3D3D3", command = lambda: controller.show_frame(MainPage))
        back.config(font=('Times New Roman', 12))
        back.grid(row = 5, column = 3)
        def btn_clear():
            input_train.set("")
            station.set("")
            date.set("")

        '''def show_text():
            global trn, stan, dat
            trn = input_train.get()
            stan = station.get()
            dat = date.get()
            tk.Label(self, text = trn).grid(row = 4, column = 0)
            tk.Label(self, text=stan).grid(row=5, column=0)
            tk.Label(self, text=dat).grid(row=6, column=0)'''

        def train_status():
            global train_number, station_code, current_date, t
            train_number = input_train.get()
            station_code = station.get()
            current_date = date.get()
            x = lambda :clear()
            if train_number == "" or station_code == "" or current_date == "":
                t = 4
                lt3 = tk.Label(self, text="Please enter all the fields!!", fg="red")
                lt3.config(font=('Times New Roman', 14))
                lt3.grid(row=6, column=1, columnspan=3)

            elif(len(train_number) != 5 or not(train_number.isdigit())):
                t = 0
                lt1 = tk.Label(self, text="Please enter the correct Train number!!", fg="red")
                lt1.config(font=('Times New Roman', 14))
                lt1.grid(row=6, column=1,columnspan=3)
            elif(station_code.islower() or not(station_code.isalpha())):
                t = 1
                lt2 = tk.Label(self, text="Please enter the correct Train number!!", fg="red")
                lt2.config(font=('Times New Roman', 14))
                lt2.grid(row=6, column=1, columnspan=3)
            else:
                    status = live_status()
                    #print(status)
                    if (type(status).__name__ == "str"):
                        t = 2
                        ll = tk.Label(self, text=status, fg="red")
                        ll.config(font=('Times New Roman', 14))
                        ll.grid(row=6, column=1, columnspan=3)
                    else:
                        t = 3
                        l1 = tkinter.Label(self, text="Train Name")
                        l1.config(font=('Times New Roman', 14))
                        l1.grid(row=6, column=1)
                        l2 = tkinter.Label(self, text=status["Train Name"], bg="#F0E68C")
                        l2.config(font=('Times New Roman', 12))
                        l2.grid(row=7, column=1)
                        l3 = tkinter.Label(self, text="Current Status")
                        l3.config(font=('Times New Roman', 14))
                        l3.grid(row=6, column=2)
                        l4 = tkinter.Label(self, text=status["current status"], bg="#F0E68C")
                        l4.config(font=('Times New Roman', 12))
                        l4.grid(row=7, column=2)

                    New_pnr = tk.Button(self, text="New Search", fg="#8A2BE2", command=lambda: clear())
                    New_pnr.grid(row=8, column=2)

            def clear():
                global t
                if(t == 0):
                    lt1.grid_remove()
                    input_train.set("")
                    station.set("")
                    date.set("")
                elif (t == 1):
                    lt2.grid_remove()
                    input_train.set("")
                    station.set("")
                    date.set("")
                elif (t == 2):
                    ll.grid_remove()
                    input_train.set("")
                    station.set("")
                    date.set("")
                elif (t == 3):
                    l1.grid_remove()
                    l2.grid_remove()
                    l3.grid_remove()
                    l4.grid_remove()
                    input_train.set("")
                    station.set("")
                    date.set("")
                elif (t == 4):
                    lt3.grid_remove()
                    input_train.set("")
                    station.set("")
                    date.set("")
                New_pnr.grid_remove()


def live_status():
    global train_number, station_code, current_date
    api_key = "dcliff0rc4"

    # base_url variable to store url
    base_url = "https://api.railwayapi.com/v2/live/train/"

    # enter train_number here
    #train_number = "12791"

    # enter current date in dd-mm-yyyy format
    #current_date = "24-06-2019"

    #station_code = "CD"

    # complete_url variable to
    # store complete url address
    complete_url = base_url + train_number + "/station/" + station_code + "/date/" + current_date + "/apikey/" + api_key + "/"

    # get method of requests module
    # return response object
    response_ob = requests.get(complete_url)

    # json method of response object convert
    # json format data into python format data
    result = response_ob.json()
    #print(result)
    # Now result contains list of nested dictionaries
    # Check the value of "response_code" key is equal
    # to "200" or not if equal that means record is
    # found otherwise record is not found
    if result["response_code"] == 200:

        # train name is extracting from
        # the result variable data
        train_name = result["train"]["name"]

        # store the value or data of
        # "route" key in variable y
        # y = result["route"]

        # source station name is extracting
        # from the y variable data

        # store the value of "position"
        # key in variable position
        position = result["position"]

        # print following values
        return{"Train Name": str(train_name), "current status": str(position)}

    else:
        return "Record Not Found for the requested Train"


def pnr_status():
    api_key = "dcliff0rc4"
    # base_url variable to store url
    base_url = "https://api.railwayapi.com/v2/pnr-status/pnr/"

    # Enter valid pnr_number
    global expression

    #"8120074488"
    # Stores complete url address
    complete_url = base_url + expression + "/apikey/" + api_key + "/"

    # get method of requests module
    # return response object
    response_ob = requests.get(complete_url)
    # json method of response object convert
    # json format data into python format data
    result = response_ob.json()

    # now result contains list
    # of nested dictionaries
    if result["response_code"] == 200:

        # train name is extracting
        #   from the result variable data
        train_name = result["train"]["name"]

        # train number is extracting from
        # the result variable data
        train_number = result["train"]["number"]

        # from station name is extracting
        # from the result variable data
        from_station = result["from_station"]["name"]

        # to_station name is extracting from
        # the result variable data
        to_station = result["to_station"]["name"]

        # boarding point station name is
        # extracting from the result variable data
        boarding_point = result["boarding_point"]["name"]

        # reservation upto station name is
        # extracting from the result variable data
        reservation_upto = result["reservation_upto"]["name"]

        # store the value or data of "pnr"
        # key in pnr_num variable
        pnr_num = result["pnr"]

        # store the value or data of "doj" key
        # in variable date_of_journey variable
        date_of_journey = result["doj"]

        # store the value or data of
        # "total_passengers" key in variable
        total_passengers = result["total_passengers"]

        # store the value or data of "passengers"
        # key in variable passengers_list
        passengers_list = result["passengers"]

        # store the value or data of
        # "chart_prepared" key in variable
        chart_prepared = result["chart_prepared"]

        # tkinter.Label(window2, text=expression)



        return [train_number, train_name, date_of_journey, from_station, to_station, reservation_upto, boarding_point], passengers_list

        # print following values
        '''print(" train name : " + str(train_name)
          + "\n train number : " + str(train_number)
          + "\n from station : " + str(from_station)
          + "\n to station : " + str(to_station)
          + "\n boarding point : " + str(boarding_point)
          + "\n reservation upto : " + str(reservation_upto)
          + "\n pnr number : " + str(pnr_num)
          + "\n date of journey : " + str(date_of_journey)
          + "\n total no. of passengers: " + str(total_passengers)
          + "\n chart prepared : " + str(chart_prepared))

        # looping through passenger list
        for passenger in passengers_list:
            # store the value or data
            # of "no" key in variable
            passenger_num = passenger["no"]

            # store the value or data of
            # "current_status" key in variable
            current_status = passenger["current_status"]

            # store the value or data of
            # "booking_status" key in variable
            booking_status = passenger["booking_status"]

            # print following values
            print(" passenger number : " + str(passenger_num)
              + "\n current status : " + str(current_status)
              + "\n booking_status : " + str(booking_status))'''

    else:
        return "record is not found for given request", "0"


app = Window()

app.mainloop()