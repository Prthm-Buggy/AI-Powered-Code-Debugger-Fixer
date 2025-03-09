import pylint.lint
import json
import tempfile
import os

def analyze_code(code):
    # Save the user's code to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
        temp_file.write(code.encode('utf-8'))
        temp_file_path = temp_file.name

    # Run Pylint and capture the output
    pylint_args = [temp_file_path, "--output-format=json"]

    try:
        results = pylint.lint.Run(pylint_args, do_exit=False).linter.reporter.data
    except Exception as e:
        return {"error": str(e)}
    finally:
        os.remove(temp_file_path)  # Clean up

    return {"issues": results}
