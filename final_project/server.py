from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translator = translator()
    translation = translator.english_to_french(textToTranslate)
    return translation

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translator = translator()
    translation = translator.french_to_english(textToTranslate)
    return translation

@app.route("/")
def renderIndexPage():
    context = {'message': 'Hello, World!'}
    html = render_template('index.html',context)
    return Response(html, content_type='text/html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
