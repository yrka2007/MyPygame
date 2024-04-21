from flask import Flask, request, render_template

import random
import string

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('generate.html')


@app.route('/genpassword', methods=['GET', 'POST'])
def genpassword():
    minpasslen = 8
    maxpasslen = 30

    passlen = int(request.form.get('passlen'))

    include_numbers = request.form.get('includenumbers')
    include_special_chars = request.form.get('includespecialchars')
    include_uppercase_letters = request.form.get('includeuppercaseletters')

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    print(include_numbers, include_special_chars, include_uppercase_letters)

    char_sets = [lowercase_letters]

    if include_numbers == 'on':
        char_sets.append(digits)
    if include_special_chars == 'on':
        char_sets.append(special_chars)
    if include_uppercase_letters == 'on':
        char_sets.append(uppercase_letters)

    all_chars = ''.join(char_sets)

    password = random.choices(all_chars, k=passlen)
    password = ''.join(password)

    return render_template('generate.html', generatedpassword=password)


if __name__ == '__main__':
    app.run(debug=True)
