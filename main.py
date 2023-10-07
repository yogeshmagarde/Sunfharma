from flask import Flask, render_template, request
import speech_recognition as sr
import openpyxl

app = Flask(__name__)

# Load your Excel file here
excel_file = "Talk and bill ASR.xlsx"

def search_data_in_excel(text):
    try:
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active

        data = []

        for row in sheet.iter_rows(values_only=True):
            for cell_value in row:
                if text.lower() in str(cell_value).lower():
                    data.append(row)
                    break

        print({"ASR.xlsx_data":data})
        return data
    
    except:
        # print(ex)
        return ["data is not found"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    recognizer = sr.Recognizer()
    print(recognizer,"hello")

    ''' recording the sound '''
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 4 seconds")
        recorded_audio = recognizer.listen(source, timeout=10)
        print("Done recording")
    ''' Recognizing the Audio '''
    try:
        print("Recognizing the text")
        if recorded_audio:
            text = recognizer.recognize_google(recorded_audio,language="en-US")
            print("Decoded Text",text)
            search_result = search_data_in_excel(text)
            return render_template('index.html', text=text, search_result=search_result)

    except:
        return render_template('error.html',error_message="Error: Speak Again")

if __name__ == '__main__':
    app.run(debug=True)
