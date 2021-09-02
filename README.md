# NLP project translation


## Build Your Own Machine Translation Service with Transformers
###### Using the latest Helsinki NLP models available in the Transformers library to create a standardized machine translation service

Machine translation is in demand within the enterprise environment. It’s vital that global companies are able to share documents, notes, emails, and other texts with people across the world in a gamut of different languages.

Arguably even more important is the need to democratize information alongside globalization. Regardless of your spoken language, you should have access to the same open source publications, healthcare info, tools, and knowledge as those whose primary language is widely spoken, like English.

![image](https://user-images.githubusercontent.com/28071950/131914204-24fc36f5-a155-47f5-9eb8-8756bffa72b0.png)


## Dynamic Language Translation in Python
Now that we have a better way to manage the languages we support, let’s get to the meat of the problem, then a class and associated methods to manage our translations.

We need a couple of functions here:

    ► translate text given a source language and target language (duh)
    ► load and manage models we don’t have into memory (I use a simple dict)
    ► get supported languages (what languages did we download for this app?)

## Creation of the web application
    To achieve our goal, which is to create a translation application, we have thought of creating a web application connected to our bookstore which is used to translate a text in French into English and vice versa.
![1](https://user-images.githubusercontent.com/28071950/131918751-3cbf809e-d5e6-43ec-97d8-4d8fc9366cc1.PNG) 
![2](https://user-images.githubusercontent.com/28071950/131918709-ba75253b-abd8-40ae-a4dd-e474c0947184.PNG)

## Notebook 
In this step we will project the Flask part, Flask is an open-source micro framework for web development in Python.
#### Templates in Flask
Flask uses the Jinja2 template system, which allows you to generate any textual format (HTML, CSS ...).
Templates are stored in a templates directory, located in the same directory as the Python file defining the application.
To apply a template, all you have to do is call the flask.render_template function passing it + the name of the template (relative to the templates directory), and + the list of variables used by the template:
from flask import Flask, render_template, request,url_for
from transformers import MarianTokenizer, MarianMTModel

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/translated', methods=['POST','GET'])
def process():

## Hugging Face Translation models: Helsinki-NLP
In this step we will project the Flask part, Flask is an open-source micro framework for web development in Python.

More recently, Huggingface released over 1,000 pre-trained language models from Helsinki University. For anyone looking to create their own AWS or Google translate API, it’s never been easier. So, I figured I’d capitalize on others’ hard work. This is the functional equivalent of “let’s wrap machine learning in a flask API and docker image” but, whatever, it’s fun. Let’s do it.

##### Machine Translation with Transformers

Huggingface has done an incredible job making SOTA (state of the art) models available in a simple Python API for copy + paste coders like myself. To translate text locally, you just need to pip install transformers and then use the snippet below from the transformers docs. https://huggingface.co/transformers/model_doc/marian.html

mname = f'Helsinki-NLP/opus-mt-{original_select}-{translated_select}'

model = MarianMTModel.from_pretrained(mname)
tok = MarianTokenizer.from_pretrained(mname)

gen = model.generate(**tok.prepare_seq2seq_batch(translated_text, return_tensors="pt"))
translate = tok.batch_decode(gen, skip_special_tokens=True)

Helsinki-NLP/opus-mt-en-fr
![7](https://user-images.githubusercontent.com/28071950/131919753-87657814-42db-485a-b619-a9d99fcce086.PNG)

##### Machine translation is mainly an equipment that helps specialists or translators to accomplish a pattern. However, it is not a replacement for the old translation systems, rather it is a substantive modification. Many machine translators offer their services considerably for free, which makes them much more attractive.

### REPORT: 
[NLP TRANSLATION.pdf](https://github.com/timmiyassine/nlp-project-translation/blob/main/Report/NLP%20TRANSLATION.pdf)

Our Team
        - YASSINE TIMMI
        - ZAKARIA BENZEROUAL
Supervised By :    
        - Pr. ABDELHAK MAHMOUDI
