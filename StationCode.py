from tkinter import *


def std():
    import  requests


    root = Tk()
    root.configure(bg="#FFE4C4")
    root.geometry("400x400")

    lable = Label(root, text="Hii There!! Here you can convert Station Name to its code", bg="#FFE4C4", fg="blue")
    lable.config(font=(" Comic Sans MS", 10, 'bold'))
    lable.pack(side=TOP)


    frame = Frame(root)
    frame.config(bg='#FFE4C4')
    frame.pack(side=TOP, pady="20")

    lable1 = Label(frame, text="Enter Station Name", bg="#FFE4C4")
    lable1.grid(row=0, column=0)
    entry = Entry(frame)
    entry.config(text="Enter Station Name")
    entry.grid(row=0, column=1)

    def name_to_code():
        apikey = "f6bp3rpifm"
        station = entry.get()
        complete_url = "https://api.railwayapi.com/v2/name-to-code/station/" + station + "/apikey/" + apikey + "/"

        response_ob = requests.get(complete_url)
        result = response_ob.json()
        if result["response_code"] == 200:
            code = result["stations"][0]["code"]
            lable3.configure(text="Code of station:-" + str(code))

    lable3 = Label(frame, text="Code of station:-", bg='#FFE4C4')
    lable3.grid(row=4, column=0)
    button = Button(frame, text="submit", command=name_to_code)

    button.grid(row=2, column=1)






