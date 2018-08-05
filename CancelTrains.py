from tkinter import *

def can():
    import requests, json
    root = Tk()

    root.geometry("500x600")
    lable = Label(root, text="Welcome to Cancelled Train(s) Information Panel", fg="#00008B")
    lable.config(font=(" Comic Sans MS", 15, "bold"), bg="#EEC591")
    lable.pack(side=TOP)

    lable = Label(root, text="Enter Date:")
    lable.pack()

    entry = Entry(root)
    entry.config(text="DD-MM-YYYY")
    entry.pack()

    def cancelled():
        apikey = "f6bp3rpifm"
        date = entry.get()
        complete_url = "https://api.railwayapi.com/v2/cancelled/date/" + date + "/apikey/" + apikey + "/"

        response_obj = requests.get(complete_url)
        result = response_obj.json()

        c_t = result["trains"]

        if result["response_code"] == 200:
            for train in c_t:
                y = len(c_t)
                for i in range(0, y):
                    name = result["trains"][i - 1]["name"]
                    lable22 = Label(root, text="Name of Cancelled Train:-")

                    lable22.configure(text="Name of Cancelled Train:- " + str(name))
                    lable22.pack()

    button = Button(root, text="Show", command=cancelled)
    button.pack()

    root.config(bg="#EEC591")