# NLP project translation


## Build Your Own Machine Translation Service with Transformers
###### Using the latest Helsinki NLP models available in the Transformers library to create a standardized machine translation service

Machine translation is in demand within the enterprise environment. It’s vital that global companies are able to share documents, notes, emails, and other texts with people across the world in a gamut of different languages.

Arguably even more important is the need to democratize information alongside globalization. Regardless of your spoken language, you should have access to the same open source publications, healthcare info, tools, and knowledge as those whose primary language is widely spoken, like English.

![image](https://user-images.githubusercontent.com/28071950/131914204-24fc36f5-a155-47f5-9eb8-8756bffa72b0.png)

More recently, Huggingface released over 1,000 pre-trained language models from Helsinki University. For anyone looking to create their own AWS or Google translate API, it’s never been easier. So, I figured I’d capitalize on others’ hard work. This is the functional equivalent of “let’s wrap machine learning in a flask API and docker image” but, whatever, it’s fun. Let’s do it.
### Machine Translation with Transformers
Huggingface has done an incredible job making SOTA (state of the art) models available in a simple Python API for copy + paste coders like myself. To translate text locally, you just need to pip install transformers and then use the snippet below from the transformers docs. https://huggingface.co/transformers/model_doc/marian.html

###### from transformers import MarianTokenizer, MarianMTModel
###### from typing import List
###### src = 'fr'  # source language
###### trg = 'en'  # target language
###### sample_text = "où est l'arrêt de bus ?"
###### mname = f'Helsinki-NLP/opus-mt-{src}-{trg}'

###### model = MarianMTModel.from_pretrained(mname)
###### tok = MarianTokenizer.from_pretrained(mname){
###### batch = tok.prepare_translation_batch(src_texts=[sample_text])  # don't need tgt_text for inference
###### gen = model.generate(**batch)  # for forward pass: model(**batch)
###### words: List[str] = tok.batch_decode(gen, skip_special_tokens=True)  # returns "Where is the the bus stop ?"

## Dynamic Language Translation in Python
Now that we have a better way to manage the languages we support, let’s get to the meat of the problem, then a class and associated methods to manage our translations.

We need a couple of functions here:

    ► translate text given a source language and target language (duh)
    ► load and manage models we don’t have into memory (I use a simple dict)
    ► get supported languages (what languages did we download for this app?)

## Création de l’application web
    Pour arriver à notre objectif, qui a la réalisation d’une application de traduction nous avons pensé à la création d’une application web connecté à notre librairie  qui sert à la traduction d’un texte en français vers l’anglais et vice versa. 
![1](https://user-images.githubusercontent.com/28071950/131918751-3cbf809e-d5e6-43ec-97d8-4d8fc9366cc1.PNG) ![2](https://user-images.githubusercontent.com/28071950/131918709-ba75253b-abd8-40ae-a4dd-e474c0947184.PNG)


