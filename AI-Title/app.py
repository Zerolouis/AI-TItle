# coding=utf8
import string

import torch
from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import numpy as np
import translators.server as ts
from transformers import RobertaTokenizer, RobertaForSequenceClassification, T5Tokenizer, T5ForConditionalGeneration

type_list = ['C#', 'Java', 'JS', 'Python']

def softmax(x):
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp, axis = 0, keepdims = True)
    s = x_exp / x_sum
    return s.tolist()

def predict(tokenizer, model, text):
    tokens_pt2 = tokenizer.encode_plus(text,return_tensors="pt", max_length=300, padding="max_length", truncation=True)
    input_ids = tokens_pt2['input_ids']
    attention_mask = tokens_pt2['attention_mask']
    with torch.no_grad():
        outputs = model(input_ids=input_ids,
                        attention_mask=attention_mask)['logits']
        logit = outputs[0].numpy().tolist()
        logit = softmax(logit)
        _, y = torch.max(outputs, dim=1)
    return logit, type_list[y.item()]

def get_title(tokenizer, model, prefix, input_text):
    input_ids = tokenizer(prefix+": "+input_text ,return_tensors="pt", max_length=512, padding="max_length", truncation=True)
    summary_text_ids = model.generate(
        input_ids=input_ids["input_ids"],
        attention_mask=input_ids["attention_mask"],
        bos_token_id=model.config.bos_token_id,
        eos_token_id=model.config.eos_token_id,
        length_penalty=1.2,
        top_k=5,
        top_p=0.95,
        max_length=48,
        min_length=2,
        num_beams=3,
        num_return_sequences=3
    )
    result_list = []
    for i, beam_output in enumerate(summary_text_ids):
        title = tokenizer.decode(beam_output, skip_special_tokens=True)
        if (title[-1] in string.punctuation):
            title = title[:-1] + " " + title[-1]
        result_list.append(title)
    return result_list

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['WTF_CSRF_CHECK_DEFAULT'] = False
from flask.json import JSONEncoder as _JSONEncoder

class JSONEncoder(_JSONEncoder):
    def default(self, o):
        import decimal
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(JSONEncoder, self).default(o)
app.json_encoder = JSONEncoder
CORS(app, supports_credentials=True)

@app.route('/so',methods=['POST'])
def so():
    time_start = time.time()
    code = request.values.get('code')
    desc = request.values.get('desc')
    desc = ts.alibaba(desc, from_language="zh", to_language="en")
    input_text = ' '.join(code.split()[:256]) + " <code> " + ' '.join(desc.split()[:256])
    logit,pred_label = predict(class_tokenizer, class_model, input_text)
    input_text = ' '.join(desc.split()[:256]) + " <code> " + ' '.join(code.split()[:256])
    title_list = get_title(gen_tokenizer, gen_model, pred_label, input_text)
    title_list = [ts.alibaba(title, from_language="en", to_language="zh") for title in title_list]
    time_end = time.time()
    logit_list = []
    for i in range(len(logit)):
        logit_list.append({"value":logit[i],"name":type_list[i]})
    return jsonify({'logit':logit_list,'prediction':pred_label,'title_1':title_list[0],
                    'title_2':title_list[1], 'title_3':title_list[2], 'time':round(time_end - time_start,2)})

@app.route('/co', methods=['POST'])
def co():
    time_start = time.time()
    code = request.values.get('code')
    desc = request.values.get('desc')
    incomplete_title = request.values.get('incomplete_title')
    # desc = ts.alibaba(desc, from_language="zh", to_language="en")
    input_text = ' '.join(code.split()[:256]) + " <code> " + ' '.join(desc.split()[:256])
    logit, pred_label = predict(class_tokenizer, class_model, input_text)
    input_text = incomplete_title+' <mask> <body>'+''.join(desc.split()[:256]) + " <code> " + ' '.join(code.split()[:256])
    title_list = get_title(gen_tokenizer, gen_model, pred_label, input_text)
    # title_list = [ts.alibaba(title, from_language="en", to_language="zh") for title in title_list]
    time_end = time.time()
    logit_list = []
    for i in range(len(logit)):
        logit_list.append({"value": logit[i], "name": type_list[i]})
    return jsonify({'logit': logit_list, 'prediction': pred_label, 'title_1': incomplete_title+title_list[0],
                    'title_2': incomplete_title+title_list[1], 'title_3': incomplete_title+title_list[2], 'time': round(time_end - time_start, 2)})

if __name__ == '__main__':
    class_tokenizer = RobertaTokenizer.from_pretrained('shaoyuyoung/Title-Classification')
    class_model = RobertaForSequenceClassification.from_pretrained("shaoyuyoung/Title-Classification")  # BERT 配置文件
    gen_model = T5ForConditionalGeneration.from_pretrained("shaoyuyoung/QTC4SO")
    gen_tokenizer = T5Tokenizer.from_pretrained("shaoyuyoung/QTC4SO")
    app.run(port=5000)
