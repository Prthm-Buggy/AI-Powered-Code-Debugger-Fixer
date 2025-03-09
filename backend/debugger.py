import pylint.lint
from io import StringIO
import json

def analyze_code(code):
    # Save the user's code to a temporary file
    temp_file = "temp_code.py"
    with open(temp_file, "w") as f:
        f.write(code)

    # Run Pylint and capture the output
    output = StringIO()
    pylint_args = [temp_file, "--output-format=json"]
    
    try:
        pylint.lint.Run(pylint_args, do_exit=False)
        lint_results = json.loads(output.getvalue())
    except Exception as e:
        return {"error": str(e)}

    return {"issues": lint_results}
