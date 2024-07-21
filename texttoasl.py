from tkinter import *
from PIL import ImageTk, Image

def main():
    pictures = {
        'A': '0.jpg',
        'B': '1.jpg',
        'C': '2.jpg',
        'D': '3.jpg',
        'E': '4.jpg',
        'F': '5.jpg',
        'G': '6.jpg',
        'H': '7.jpg',
        'I': '8.jpg',
        'J': '9.jpg',
        'K': '10.jpg',
        'L': '11.jpg',
        'M': '12.jpg',
        'N': '13.jpg',
        'O': '14.jpg',
        'P': '15.jpg',
        'Q': '16.jpg',
        'R': '17.jpg',
        'S': '18.jpg',
        'T': '19.jpg',
        'U': '20.jpg',
        'V': '21.jpg',
        'W': '22.jpg',
        'X': '23.jpg',
        'Y': '24.jpg',
        'Z': '25.jpg'
    }
    a = input("enter the text to be translated ")

    words = a.split()
    for i in words:
        print(i)
        for j in i:
            j = j.upper()

            # Create an instance of tkinter window
            win = Tk()

            # Define the geometry of the window
            win.geometry("700x500")

            frame = Frame(win, width=600, height=400)
            frame.pack()
            frame.place(anchor='center', relx=0.5, rely=0.5)

            # Create an object of tkinter ImageTk
            img = ImageTk.PhotoImage(Image.open("C:/Users/Aniketh/Downloads/Asl alph/Asl Alphabet/" + pictures[j]))

            # Create a Label Widget to display the text or Image
            label = Label(frame, image=img, highlightbackground='white')
            label.pack()

            win.mainloop()

if __name__ == '__main__':
    main()