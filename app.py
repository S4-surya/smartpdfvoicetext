from flask import Flask, render_template, request
import PyPDF2
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    explanation = None
    audio = None

    if request.method == "POST":

        pdf = request.files["pdf"]

        filepath = "temp.pdf"
        pdf.save(filepath)

        text = ""

        reader = PyPDF2.PdfReader(filepath)

        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content

        sentences = text.split(".")
        explanation = " ".join(sentences[:5])

        tts = gTTS(explanation)

        audio = "output.mp3"
        tts.save(audio)

    return render_template("index.html", explanation=explanation, audio=audio)

if __name__ == "__main__":
    app.run()
