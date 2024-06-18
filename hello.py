from flask import Flask, request, render_template, render_template_string
import subprocess
import markdown

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/execute', methods=['POST'])
def execute():
    user_command = request.form['command']
    result = subprocess.run(
        ['python3', 'query_data.py', user_command], capture_output=True, text=True)

    # Convert the output to HTML using the markdown library
    markdown_output = markdown.markdown(result.stdout)

    # Render the HTML output
    return render_template_string('''
        <div>{{ output|safe }}</div>
        <a href="/">Go back</a>
    ''', output=markdown_output)


if __name__ == '__main__':
    app.run(debug=True)
