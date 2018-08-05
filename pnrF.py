from tkinter import *


def ppnnrr():
    import requests, json

    root1 = Tk()



    root1.geometry('500x600')
    lable100 = Label(root1, text="Developed by Yash Tayal")
    lable100.pack(side=BOTTOM, fill=X)

    lable000 = Label(root1, text="Welcome to Indian Railway Online Panel", fg="purple")
    lable000.config(font=("Comic Sans MS", 18, 'bold'))
    lable000.pack(fill=X)

    lable200 = Label(root1, text="Hello friends we have tried to develop a user friendly railway app")
    lable200.config(font=('none', 12, 'bold'))
    lable200.pack(fill=X, )
    framee = Frame(root1)
    framee.pack(side=TOP, pady=100)
    lable300 = Label(framee, text="Enter your PNR Number")
    lable300.grid(row=0, column=0)
    entry = Entry(framee)
    entry.grid(row=0, column=2)

    def pnr_status():
        api_key = "f6bp3rpifm"
        base_url = "https://api.railwayapi.com/v2/pnr-status/pnr/"
        pnrr = entry.get()
        complete_url = base_url + pnrr + "/apikey/" + api_key + "/"

        response_ob = requests.get(complete_url)
        result = response_ob.json()

        if result["response_code"] == 200:
            no_pass = result["total_passengers"]
            pnr=result["pnr"]
            doj=result["doj"]
            chart_prepared=result["chart_prepared"]
            boardingStn=result["boarding_point"]["name"]
            res_ut=result["reservation_upto"]["name"]
            journycls=result["journey_class"]["name"]
            passenger_list=result["passengers"]
            for passengers in passenger_list:
                passenger_num = passengers["no"]
                lable01 = Label(root1, text="Passenger No.")
                lable1 = Label(root1, text="Current Status:-")
                lable2 = Label(root1, text="Booking Status")
                lable01.place(x=350 + int((passenger_num) * 200), y=300 )
                lable1.place(x=350 + int((passenger_num) * 200), y=350 )
                lable2.place(x=350 + int((passenger_num) * 200), y=400 )


                current_status=passengers["current_status"]
                booking_status=passengers["booking_status"]
                lable01.configure(text="Passenger No.:-"+str(passenger_num))
                lable1.configure(text="Current Status:-"+str(current_status))
                lable2.configure(text="Booking Status"+str(booking_status))









            from_station=result["from_station"]["name"]
            lable40.configure(text="Total Passengers are  " + str((no_pass)))
            lable50.configure(text=("PNR Number-: " +str(pnr)))
            lable60.configure(text=("DOJ:-" + str(doj)))
            lable70.configure(text=("Chart status :- " +str(chart_prepared)))
            lable80.configure(text=("Departing station:-" +str(from_station)))
            lable90.configure(text="Resevation Upto:-"+ str(res_ut))
            lable100.configure(text="Journey Class:-"+str(journycls))







        else:
            lable40.configure(text="error")

    lable40 = Label(root1, text="Total Passengers are...")
    lable40.place(x=50, y=300)
    lable50 = Label(root1, text="PNR Number-:...")
    lable50.place(x=50, y=350)
    lable60 = Label(root1, text="DOJ:-...")
    lable60.place(x=50, y=400)
    lable70 = Label(root1, text="Chart status...")
    lable70.place(x=50, y=450)
    lable80 = Label(root1, text="Departing station:-...")
    lable80.place(x=50, y=500)
    lable90 = Label(root1, text="Resevation Upto:-...")
    lable90.place(x=250, y=300)
    lable100 = Label(root1, text="Journey Class:-...")
    lable100.place(x=250, y=350)







    buttonpnr = Button(framee, text="show PNR Status", command=pnr_status)
    buttonpnr.grid(row=2,column=2)





