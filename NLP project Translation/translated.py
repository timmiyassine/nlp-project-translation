from flask import Flask, render_template, request,url_for
from transformers import MarianTokenizer, MarianMTModel

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/translated', methods=['POST','GET'])
def process():
	if request.method == "POST":

		original_select = request.form['original_select']
		original_text = request.form['original_text']
		translated_select = request.form['translated_select']

		if original_select != translated_select and original_text !="" :

			translated_text = original_text
			
			mname = f'Helsinki-NLP/opus-mt-{original_select}-{translated_select}'

			model = MarianMTModel.from_pretrained(mname)
			tok = MarianTokenizer.from_pretrained(mname)
		
			gen = model.generate(**tok.prepare_seq2seq_batch(translated_text, return_tensors="pt"))
			translate = tok.batch_decode(gen, skip_special_tokens=True)

			# translated Text
			return render_template('index.html', translated_text=translate[0],original_text=original_text,original_select=original_select,translated_select=translated_select)

		else :
			
			return render_template('index.html',translated_text=original_text,original_text=original_text,original_select=original_select,translated_select=translated_select)

if __name__ == '__main__':
	app.run(debug=True)