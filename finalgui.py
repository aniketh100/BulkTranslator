from tkinter import *
import Application
import bulktranslator
from tkinter import scrolledtext
import texttoasl
import tkinter as tk
import speech_recognition as sr
from tkinter import filedialog as fd
import googletrans
from googletrans import Translator
from gtts import gTTS
from langdetect import detect
import os
import PyPDF2
from fpdf import FPDF
from playsound import playsound  # pip install PyObjC for better sound, apparently
import textblob
import subprocess


from fpdf import FPDF




root = Tk()

'''
temp1 = 0
def ASL_txt():
    temp1=1
'''


def home():
    root.geometry('600x800')
    frame_h = Frame(root, width=600, height=800)
    frame_h.pack()

    head = Label(frame_h, text="LINGUISTIC MULTI-TOOL", font=("Verdana", 20), bd = 1, justify = 'center',padx = 100)
    head.place(x=30, y=10)

    quit = Button(frame_h, padx=205, pady=15, text='Quit', bd='5', command=root.destroy, activebackground = 'gray')
    quit.place(x=50, y=550)

    b1 = Button(frame_h, padx=190, pady=15, text='ASL to Text', bd='5', command=lambda: ASL_txt(), activebackground = 'gray')
    b1.place(x=50, y=70)

    b2 = Button(frame_h, padx=190, pady=15, text='Text to ASL', bd='5', command=lambda: txt_ASL(), activebackground = 'gray')
    b2.place(x=50, y=150)

    b3 = Button(frame_h, padx = 180, pady=15, text='Text to speech', bd='5', command=lambda: txt_sp(), activebackground = 'gray')
    b3.place(x=50, y=230)

    b4 = Button(frame_h, padx=180, pady=15, text='Speech to text', bd='5', command=lambda: sp_txt(), activebackground = 'gray')
    b4.place(x=50, y=310)

    b5 = Button(frame_h, padx=180, pady=15, text='Bulk Translator', bd='5', command=lambda: bulk(), activebackground = 'gray')
    b5.place(x=50, y=390)

    b6 = Button(frame_h, padx=188, pady=15, text='Help/Guide', bd='5', command = lambda:help(),activebackground = 'gray')
    b6.place(x=50, y=470)

    def help():
        print('''Hello user! glad you are using our linguistic multi-tool
We have various features available for different purposes.

1.) American Sign Language To text Convertor:
    Through our tool you can convert sign language to
    text, helping both the users to understand and learn
    sign language and communicate with one another. To use
    it, simply hold out your hand in the black and white
    area, and make a sign, which will then be translated
    to the corresponding text.

2.) Text to American Sign Language Convertor:
    Similiar to the above, you enter desired text you want
    to convert to sign language. Once entered, you will
    be shown signs corresponding to each letter in a word.
    A popup window will be shown for Each letter(The letters
    will be displayed in the console). To see the sign for
    the next letter, close the current popup.

3.) Text To speech Convertor:
    As the name suggests, converts inputted text from user
    or text from imported file, to user needed voice.
    Enter text in the given text box. On clicking on the 
    convert button, your text is translated to speech in 
    your desired language. You can also input a txt/pdf 
    file, where the text will be read and translated aloud
    
4.) Speech To Text:
    As the name suggests, Converts inputted speech from user
    to user specific translated language in text. A user can 
    either speek through a microphone or input a mp3 file
    to translate to text, in their desired language.
    
5.) Bulk Convertor:
    Inputs a txt/pdf file, or takes a manual input from user
    Converts the given text inputted to their desired given 
    language in the form of pdf.
    
''')

    def ASL_txt():
        root.destroy()
        Application.main()

    def txt_ASL():

        root.destroy()
        texttoasl.main()

    def txt_sp():
        frame_h.destroy()
        frame3 = Frame(root, width=900, height=550)
        frame3.pack()
        root.geometry('900x550')

        def back_func():
            back_btn.destroy()
            frame3.destroy()
            home()
        back_btn = Button(frame3, padx=20, pady=5, text='Back', command=lambda: back_func())
        back_btn.place(x=5, y=5)

        heading = Label(frame3, text='Text to Speech Convertor', font=("Arial", 28), bd='2')
        heading.place(x=300, y=10)

        f_out = ""

        t1 = Text(frame3, width=85, height=10, font=("Times New Roman", 20), highlightbackground='black')
        t1.insert(tk.END, f_out)
        t1.place(x=20, y=80)

        d_lang = "abc"

        language = ''

        def txt_open():
            """ke=[]
            language = googletrans.LANGUAGES
            for i in (language.values()):
                ke.append(i)

            for key, value in language.items():
                if (value == clicked1.get()):
                    li = key
            for key, value in language.items():
                if (value == clicked2.get()):
                    tl = key
            tlr = Translator()"""

            filename = fd.askopenfilename(title="Open a file")
            global contents
            contents=''

            try:
                fp = open(filename, 'r')
                contents = fp.read()
                t1.insert(tk.END, contents)
                print(contents)
            except:

                fp = open(filename, 'rb')
                fpreader = PyPDF2.PdfFileReader(fp)
                page = fpreader.getPage(0)
                contents = page.extractText()
                t1.insert(tk.END, contents)
                print(contents)


        def translation():
            try:
                global language
                contents = t1.get("1.0", "end-1c")
                print(contents)
                contents=contents.lower()

                language=detect(contents)


                language = language[0:2:1]
                b=googletrans.LANGUAGES

                myobj = gTTS(text=contents, lang=language, slow=True)
                myobj.save("C:/Users/Aniketh/PycharmProjects/programfolder2/SignLanguage/Sign-Language-To-Text-Conversion-main/outputmp3.mp3")
            except:
                print("invalid text, please enter meaningful sentences")

            playsound("C:/Users/Aniketh/PycharmProjects/programfolder2/SignLanguage/Sign-Language-To-Text-Conversion-main/outputmp3.mp3")

        """b1 = Button(frame3, text='Click to Detect Language', width=20, height=3, command=lambda: detected_lang())
        b1.place(x=200, y=390)"""

        b2 = Button(frame3, text='Click to Play Translation', width=20, height=3, command=lambda: translation())
        b2.place(x=530, y=390)

        b3 = Button(frame3, text='Translate a txt/pdf', width=20, height=3, command=lambda: txt_open())
        b3.place(x=200, y=390)

    def sp_txt():
        frame_h.destroy()
        frame4 = Frame(root, width=800, height=550)
        frame4.pack()
        root.geometry('800x550')

        def back_func():
            back_btn.destroy()
            frame4.destroy()
            home()

        back_btn = Button(frame4, padx=20, pady=5, text='Back', command=lambda: back_func())
        back_btn.place(x=5, y=5)


        l1 = Label(frame4, text='Choose Input language:', font=("Arial", 28))
        l1.place(x=50, y=50)

        l2 = Label(frame4, text='Choose Output language:', font=("Arial", 28))
        l2.place(x=50, y=150)

        language = googletrans.LANGUAGES
        ke = ["Chooose language"]

        for i in (language.values()):
            ke.append(i)

        # print(ke)
        def disp_val1(choice1):
            choice1 = ke[0]
            choice1 = clicked1.get()
            print(choice1)

        clicked1 = StringVar()
        clicked1.set(ke[0])
        drop1 = OptionMenu(frame4, clicked1, *ke, command=disp_val1)
        drop1.place(x=550, y=60)

        def disp_val2(choice2):
            choice2 = ke[0]
            choice2 = clicked2.get()
            print(choice2)

        def swaplang():
            choice1 = clicked2.get()
            choice2 = clicked1.get()

            clicked1.set(choice1)
            clicked2.set(choice2)

        def micro_func():
            global string1
            for key, value in language.items():
                if (value == clicked1.get()):
                    li = key
            for key, value in language.items():
                if (value == clicked2.get()):
                    tl = key

            # tlr = Translator()
            r = sr.Recognizer()

            with sr.Microphone() as source:

                # seconds of non-speaking audio before
                # a phrase is considered complete
                print('Listening')
                r.adjust_for_ambient_noise(source, duration=0.5)

                audio = r.listen(source)
                try:
                    print("Recognizing")
                    Query = r.recognize_google(audio, language=li)

                    out = textblob.TextBlob(Query)
                    out = out.translate(from_lang=li, to=tl)
                    print("the text is printed='", out, "'")

                    f_out = Label(frame4, text='Speech output : \t' + str(out))
                    f_out.place(x=260, y=370)

                    f_dest = Button(frame4, text='Clear Output', command=lambda: f_out.destroy())
                    f_dest.place(x=260, y=490)

                    f_swap = Button(frame4, text='Swap', command=lambda: swaplang())
                    f_swap.place(x=550, y=100)

                except Exception as e:
                    print(e)
                    print("Say that again sir")

        def file_func():

            for key, value in language.items():
                if (value == clicked1.get()):
                    li = key
            for key, value in language.items():
                if (value == clicked2.get()):
                    tl = key
            tlr = Translator()

            filename = fd.askopenfilename(title="Open a file")

            r = sr.Recognizer()
            '''filename = Entry(frame4)
            filename.place(x = 260, y = 350)'''

            with sr.AudioFile(filename) as source:

                # seconds of non-speaking audio before
                # a phrase is considered complete
                print('Listening')
                r.adjust_for_ambient_noise(source, duration=0.5)

                audio = r.record(source)
                try:
                    print("Recognizing")
                    Query = r.recognize_google(audio, language=li)
                    out = textblob.TextBlob(Query)
                    out = out.translate(from_lang=li, to=tl)
                    print("the text is printed='", out, "'")

                    f_out = Label(frame4, text='Speech output : \t' + str(out))
                    f_out.place(x=260, y=370)

                    f_dest = Button(frame4, text='Clear Output', command=lambda: f_out.destroy())
                    f_dest.place(x=260, y=490)


                except Exception as e:
                    print(e)
                    print("Say that again sir")

        clicked2 = StringVar()
        clicked2.set(ke[0])
        drop2 = OptionMenu(frame4, clicked2, *ke, command=disp_val2)
        drop2.place(x=550, y=160)

        b1 = Button(frame4, padx=25, pady=10, text='Click me to start taking mic input', command=lambda: micro_func())
        b1.place(x=250, y=220)

        b2 = Button(frame4, padx=25, pady=10, text='Click me to Input an audio file', command=lambda: file_func())
        b2.place(x=260, y=300)

        '''f_txt = Text(frame4, width=200, height=50, font=("Times New Roman", 17))
        f_txt.insert(tk.END, f_out)
        f_txt.place(x=5, y=400)'''

    def bulk():
        root.destroy()


        subprocess.call(["php", "tfpdf.php"], shell=True)
        font_path = 'C:/Users/Aniketh/PycharmProjects/programfolder2/font/unifont/'

        s = input(
            "BULK TRANSLATOR MENU : \n\t Type 'TEXT' for translating a text file\n\t Type 'PDF' for translating a PDF file\n\t Type 'MAN' for giving manual text input\nEnter your choice : ")
        tr = Translator()
        if (s == 'TEXT' or s == 'text'):
            filename = input("Enter file path or name : ")
            fp = open(filename, 'r')
            contents = fp.read()

        elif (s == 'PDF' or s == 'pdf'):
            filename = input("Enter file path or name  : ")
            fp = open(filename, 'rb')
            fpreader = PyPDF2.PdfFileReader(fp)
            page = fpreader.getPage(0)
            contents = page.extractText()

        elif (s == 'MAN' or s == 'man'):
            contents = input("Enter text : ")

        else:
            print("Invalid input\n")

        lang = input("Enter language code you would like to translate to (fr for french, es for spanish etc) : ")

        # contents = str(contents.encode('utf-8'))
        result = tr.translate(contents, dest=lang)
        s = result.text
        print(s)

        ch = input("Type 'SAVEPDF' to save as a pdf file or 'SAVETEXT' to save as text file : ")

        if (ch == 'SAVEPDF' or ch == 'savepdf'):
            pdf = FPDF()
            pdf.add_page()

            if lang == 'kn':
                pdf.add_font('Malige', '', font_path + 'malige-n.ttf', uni=True)
                pdf.set_font('Malige', size=14)
                for x in s:
                    pdf.cell(h=14, align='L', w=3, txt=x, border=0)
                    if x == '\n':
                        pdf.ln()
                pdf.output('translatedfile.pdf')
                print("Translated file saved as translatedfile.pdf")

            elif lang == 'ta':
                pdf.add_font('Hindi', '', font_path + 'Lohit-Tamil.ttf', uni=True)
                pdf.set_font('Hindi', size=14)
                pdf.multi_cell(h=14, align='L', w=0, txt=s, border=0)
                pdf.output('translatedfile.pdf')
                print("Translated file saved as translatedfile.pdf")

            elif lang == 'te':
                pdf.add_font('Telugu', '', font_path + 'Lohit-Telugu.ttf', uni=True)
                pdf.set_font('Telugu', size=14)
                for x in s:
                    pdf.cell(h=14, align='L', w=3, txt=x, border=0)
                    if x == '\n':
                        pdf.ln()
                pdf.output('translatedfile.pdf')
                print("Translated file saved as translatedfile.pdf")

            elif lang == 'ml':
                pdf.add_font('Malayalam', '', font_path + 'RaghuMalayalamSans2.ttf', uni=True)
                pdf.set_font('Malayalam', size=14)
                pdf.multi_cell(h=14, align='L', w=0, txt=s, border=0)
                pdf.output('translatedfile.pdf')
                print("Translated file saved as translatedfile.pdf")

            elif lang == 'hi':
                pdf.add_font('Hindi', '', font_path + 'Mangal Regular.ttf', uni=True)
                pdf.set_font('Hindi', size=16)
                for x in s:
                    pdf.cell(h=14, align='L', w=3, txt=x, border=0)
                    if x == '\n':
                        pdf.ln()
                pdf.output('translatedfile.pdf')
                print("Translated file saved as translatedfile.pdf")
            else:
                pdf.add_font('DejaVu', '', font_path + 'DejaVuSans.ttf', uni=True)
                pdf.set_font('DejaVu', size=14)
                pdf.multi_cell(h=14, align='L', w=0, txt=s, border=0)
                pdf.output('translatedfile.pdf')
                print("Translated file saved as translatedfile.pdf")



        elif (ch == 'SAVETEXT' or ch == 'savetext'):
            fq = open('translated.txt', 'w', encoding='utf-8')
            fq.write(s)
            print("Translated file saved as translated.txt")


home()
root.mainloop()

