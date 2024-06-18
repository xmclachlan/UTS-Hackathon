from flask import Flask, request, render_template, render_template_string
import subprocess
import markdown

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/execute', methods=['POST'])
def execute():
    user_command = request.form['command']
    result = subprocess.run(
        ['python3', 'query_data.py', user_command], capture_output=True, text=True)

    # Convert the output to HTML using the markdown library
    markdown_output = markdown.markdown(result.stdout)

    # Render the HTML output with applied CSS
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Command Output</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
        </head>
        <body>
            <div class="flex-container">      
                <div class="output flex-item">{{ output|safe }}</div>
                <div class="flex-item">
                    <a href="/" class="button">Go back</a>
                </div>
            </div>
        </body>
        </html>
    ''', output=markdown_output)


if __name__ == '__main__':
    app.run(debug=True)
