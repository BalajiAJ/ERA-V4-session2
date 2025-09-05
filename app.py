from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# ------------------------
# Tokenizers
# ------------------------
def char_tokenizer(text):
    return list(text)

def word_tokenizer(text):
    return re.findall(r"\w+|\s+|[^\w\s]", text)

def subword_tokenizer(text):
    words = re.findall(r"\w+|\s+|[^\w\s]", text)
    tokens = []
    for w in words:
        if w.strip() and len(w) > 4:
            mid = len(w) // 2
            tokens.append(w[:mid])
            tokens.append(w[mid:])
        else:
            tokens.append(w)
    return tokens

TOKENIZERS = {
    "Character": char_tokenizer,
    "Word": word_tokenizer,
    "Subword": subword_tokenizer
}

# ------------------------
# One-Hot Encoding (Word Level Only)
# ------------------------
def one_hot_encode_words(text):
    words = re.findall(r"\w+", text)
    vocab = sorted(set(words))
    vocab_index = {w: i for i, w in enumerate(vocab)}
    one_hot = []
    for w in words:
        vector = [0] * len(vocab)
        vector[vocab_index[w]] = 1
        one_hot.append(vector)
    return words, vocab, one_hot

# ------------------------
# Routes
# ------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tokenize", methods=["POST"])
def tokenize():
    data = request.get_json()
    text = data.get("text", "")
    method = data.get("method", "Word")

    tokenizer = TOKENIZERS.get(method, word_tokenizer)
    tokens = tokenizer(text)

    # Word-level stats for metrics
    words = re.findall(r"\w+", text)
    num_tokens = len(tokens)
    num_words = len(words)
    avg_token_len = sum(len(t) for t in tokens) / num_tokens if num_tokens else 0
    fertility_ratio = num_tokens / num_words if num_words else 0

    # One-hot encoding always at word level
    vocab, one_hot = one_hot_encode_words(text)[1:]
    
    return jsonify({
        "tokens": tokens,
        "metrics": {
            "num_tokens": num_tokens,
            "num_words": num_words,
            "avg_token_len": round(avg_token_len, 2),
            "fertility_ratio": round(fertility_ratio, 2)
        },
        "one_hot_words": words,
        "vocab": vocab,
        "one_hot": one_hot
    })

if __name__ == "__main__":
    app.run(debug=True)
