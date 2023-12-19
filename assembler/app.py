from flask import Flask, render_template, request, jsonify, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/parsa')
def parsaAssembler():
    return render_template('indexp.html')

@app.route('/sina')
def sinaAssembler():
    return render_template('indexs.html')


@app.route('/assemblerVS',methods=['POST'])
def run_sinascript():
    data = request.get_json()
    input_data = data['input']
    with open('AssemblyProject1.txt', 'w') as f:
        f.write(input_data)
    result = subprocess.check_output(['python', 'assembler.py', input_data], universal_newlines=True)
    return jsonify({'output': result})

@app.route('/assemblerVP', methods=['POST'])
def run_script():
    data = request.json
    input_data = data['input']
    with open('AssemblyProject1.txt', 'w') as f:
        f.write(input_data)

    result = subprocess.check_output(['python', 'assembler.py', input_data], universal_newlines=True)

    return jsonify({'output': result})

if __name__ == '__main__':
    app.run(debug=True)
