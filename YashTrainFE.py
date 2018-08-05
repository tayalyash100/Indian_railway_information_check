from tkinter import *

def liv():

    import requests, json
    yash = Tk()

    yash.title("Live Train Web App")

    yash.geometry("600x600")

    yash.config(bg="#F0F8FF")

    lable1 = Label(yash, text="Welcome to Indian Railway Live Train Status Panel", bg="#F0F8FF", fg="#CD3333")
    lable1.config(font=("Comic Sans MS bold", 15,))
    lable1.place(x=100, y=100)

    lable2 = Label(yash, text='Enter Train No: ', bg="#F0F8FF", fg="green")
    lable2.grid(row=0, column=0)
    entry = Entry(yash, text="hiii")

    entry.grid(row=0, column=1)
    lable3 = Label(yash, text='Enter Date:        ', bg="#F0F8FF", fg="green")
    lable3.grid(row=1, column=0)
    entry1 = Entry(yash, )

    entry1.grid(row=1, column=1)

    lable3 = Label(yash, text="Developed by Yash Tayal")
    lable3.place(x=100, y=400)

    def live():
        api_key = "f6bp3rpifm"
        base_url = "https://api.railwayapi.com/v2/live/train/"
        train_number = entry.get()
        current_date = entry1.get()
        complete_url = base_url + train_number + "/date/" + current_date + "/apikey/" + api_key + "/"

        response_ob = requests.get(complete_url)
        result = response_ob.json()

        if result["response_code"] == 200:

            train_name = result["train"]["name"]
            y = result["route"]
            source_station = y[0]["station"]["name"]
            destination_station = y[len(y) - 1]["station"]["name"]
            position = result["position"]
            lable_3.configure(text=str(train_name))
            lable_4.configure(text=str(source_station))
            lable_5.configure(text=str(destination_station))
            lable_6.configure(text=str(position))
        else:
            lable_3.configure(text="Error")
            lable_4.configure(text="Error")
            lable_5.configure(text="Error")
            lable_6.configure(text="Error")

    lable_3 = Label(yash, text="pahale upper value dal", width=50, font=("bold", 8), fg='black', bg='#F0F8FF')
    lable_3.place(x=180, y=430)
    lable_4 = Label(yash, text="pahale upper value dal", width=50, font=("bold", 8), fg='black', bg='#F0F8FF')
    lable_4.place(x=180, y=450)
    lable_5 = Label(yash, text="pahale upper value dal", width=50, font=("bold", 8), fg='black', bg='#F0F8FF')
    lable_5.place(x=180, y=470)
    lable_6 = Label(yash, text="pahale upper value dal", width=50, font=("bold", 8), fg='black', bg='#F0F8FF')
    lable_6.place(x=180, y=490)

    Button(yash, text="Khojo", width=20, bg='brown', fg='white', command=live).place(x=250, y=300)

