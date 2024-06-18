from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)


@app.route('/')
def home():
    return render_template_string('''
        <form action="/run_script" method="post">
            <label for="input">Enter your input:</label>
            <input type="text" id="input" name="input">
            <input type="submit" value="Run Script">
        </form>
    ''')


@app.route('/run_script', methods=['POST'])
def run_script():
    user_input = request.form['input']
    result = subprocess.run(
        ['python3', 'query_data.py', user_input], capture_output=True, text=True)
    return f'<pre>{result.stdout}</pre><pre>{result.stderr}</pre>'


if __name__ == '__main__':
    app.run(debug=True)
