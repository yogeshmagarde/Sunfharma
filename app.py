# from flask import Flask, render_template, request

# import speech_recognition as sr

# app = Flask(__name__)


# @app.route('/')
# def recognize():
#     recognizer = sr.Recognizer()

#     ''' recording the sound '''
#     with sr.Microphone() as source:
#         print("Adjusting noise ")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         print("Recording for 4 seconds")
#         recorded_audio = recognizer.listen(source, timeout=4)
#         print("Done recording")

#     ''' Recognizing the Audio '''
#     try:
#         print("Recognizing the text")
#         text = recognizer.recognize_google(
#             recorded_audio, 
#             language="en-US"
#         )
#         print("Decoded Text : {}".format(text))
#         return text
#     except Exception as ex:
#         print(ex)
#         return "Error: Could not recognize speech"

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request

import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    recognizer = sr.Recognizer()

    ''' recording the sound '''
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 4 seconds")
        recorded_audio = recognizer.listen(source, timeout=4)
        print("Done recording")

    ''' Recognizing the Audio '''
    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )
        print("Decoded Text : {}".format(text))
        return text
    except Exception as ex:
        print(ex)
        return "Error: speak Again"

if __name__ == '__main__':
    app.run(debug=True)


