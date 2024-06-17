from flask import Flask, render_template, request
import subprocess
import shlex  # Import shlex for safer command line parsing

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/execute', methods=['POST'])
def execute_command():
    try:
        user_input = request.form['user_input']

        # Construct the command with user input appended
        command = f"echo {shlex.quote(user_input)}"

        # Execute command and capture output
        result = subprocess.run(command, shell=True,
                                capture_output=True, text=True)
        output = result.stdout

        return render_template('result.html', user_input=user_input, output=output)

    except Exception as e:
        error_message = f"Error executing command: {str(e)}"
        return render_template('error.html', error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)
