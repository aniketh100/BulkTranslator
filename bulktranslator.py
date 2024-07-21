from googletrans import Translator
import PyPDF2
from fpdf import FPDF
import subprocess
from gtts import gTTS
from playsound import playsound
from langdetect import detect

def bulk():
    path = "C:/Users/Aniketh/PycharmProjects/programfolder2/SignLanguage/Sign-Language-To-Text-Conversion-main"

    subprocess.call(["php",path+"/tfpdf.php"],shell = True)

    font_path = 'C:/Users/Aniketh/PycharmProjects/programfolder2/font/unifont/'

    s = input("BULK TRANSLATOR MENU : \n\t Type 'TEXT' for translating a text file\n\t Type 'PDF' for translating a PDF file\n\t Type 'MAN' for giving manual text input\nEnter your choice : ")
    tr = Translator()
    if(s == 'TEXT' or s == 'text'):
        filename = input("Enter file path or name : ")
        fp = open(filename, 'r')
        contents = fp.read()  

    elif(s == 'PDF' or s == 'pdf'):
        filename = input("Enter file path or name  : ")
        fp = open(filename,'rb')
        fpreader = PyPDF2.PdfFileReader(fp)
        page = fpreader.getPage(0)
        contents = page.extractText()

    elif(s == 'MAN' or s== 'man'):
        contents = input("Enter text : ")

    else:
        print("Invalid input\n")

    lang = input("Enter language code you would like to translate to (fr for french, es for spanish etc) : ")

    #contents = str(contents.encode('utf-8'))
    result = tr.translate(contents, dest = lang)
    s = result.text
    print(s)

    ch = input("Type 'SAVEPDF' to save as a pdf file or 'SAVETEXT' to save as text file : ")

    if(ch == 'SAVEPDF' or ch == 'savepdf'):
        pdf = FPDF()
        pdf.add_page()

        if lang == 'kn':
            pdf.add_font('Malige', '', font_path + 'malige-n.ttf', uni=True)
            pdf.set_font('Malige', size=14)
            pdf.multi_cell(h=14, align='L', w=0, txt=s, border=0)
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
            pdf.add_font('DejaVu','',font_path+'DejaVuSans.ttf',uni=True)
            pdf.set_font('DejaVu',size = 14)
            pdf.multi_cell(h=14, align='L', w=0, txt=s, border=0)
            pdf.output('translatedfile.pdf')
            print("Translated file saved as translatedfile.pdf")



    elif (ch == 'SAVETEXT' or ch == 'savetext'):
        fq = open(path+'/translated.txt','w',encoding = 'utf-8')
        fq.write(s)
        print("Translated file saved as translated.txt")



def txt_open():
    filename = input("Enter the file path: ") 
    try:
        with open(filename, 'r') as fp:
            contents = fp.read()
        return contents
    except:
        try:
            with open(filename, 'rb') as fp:
                fpreader = PyPDF2.PdfFileReader(fp)
                page = fpreader.getPage(0)
                contents = page.extractText()
            return contents
        except:
            return None

def translation(text, target_language):
    try:
        translator = Translator()
        translated = translator.translate(text, dest=target_language)
        translation_text = translated.text

        output_audio = gTTS(text=translation_text, lang=target_language, slow=True)
        output_audio.save(f"output_{target_language}.mp3")

        print(f"Translation ({target_language}): {translation_text}")
        print(f"Translation audio saved as 'output_{target_language}.mp3'")
    except:
        print("Invalid text or language code, please check your input.")

if __name__ == "__main__":
    #bulk()
    text = txt_open()
    if text:
        target_language = input("Enter the target language code (e.g., 'fr' for French): ")
        translation(text, target_language)
