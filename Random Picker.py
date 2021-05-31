# Random Winner Picker
# Mukhotho Vhonani Chrstopher
# 22 May 2021


# importing tkinter and randint
from tkinter import *
from random import randint

# defining random picker
randomPicker = Tk()
randomPicker.title("Random Winner Picker")
randomPicker.geometry("400x360")


# Picker Funcrion
def picker():

    # List of names
    names = ['Veli Mothwa', 'Ronwen Williams', 'Itumeleng Khune', 'Thibang Phete', 'Siyanda Xulu', 'Thulani Hlatshwayo', 'Mosa Lebusa', ' Innocent Maela', 'Sifiso Hlanti', 'Thapelo Morena', 'Craig Martin', 'Rivaldo Coetzee', 'Themba Zwane', 'Thulani Serero', 'Ben Motshwari', 'Bongani Zungu', 'Keagan Dolly', 'Percy Tau', 'Sipho Mbule', 'Andile Jali', 'Luther Singh', 'Dean Furman', 'Kermit Erasmus', 'Bradley Grobler', 'Ruzaigh Gamildien', 'Lyle Foster']

    totalNames = len(names)
    totalIndices = totalNames -1
    #Getting random number between 0 and total indices
    randomNum = randint(0, totalIndices)

    # Winner label
    winnerLabel = Label(randomPicker, text=names[randomNum], font=("Arial", 15))
    winnerLabel.pack(pady=50)



# Button to pick a winner
winButton = Button(randomPicker, text="Pick a Winner", font=("Arial", 20), command=picker)
winButton.pack(pady=20)

# Text  Label
textLabel = Label(randomPicker, text="The Winner Is:", font=("Arial", 20))
textLabel.pack(pady=20)

# calling randomPicker window
randomPicker.mainloop()