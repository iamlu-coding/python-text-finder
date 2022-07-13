from flask import render_template, request, Flask, abort
import os

from pkg_resources import require
from text_finder import TextFinder

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def find_text():
    if request.method == 'POST':
        dir_path = request.form['directory']
        text_value = request.form['textValue']

        # Return 404 if path doesn't exist
        if not os.path.exists(dir_path):
            return abort(404)

        search_obj = TextFinder(dir_path, text_value)
        search_obj._execute()
        is_text_found = search_obj.is_value_found()

        if is_text_found == 'Yes':
            # results_count = len(search_obj.get_results_list())
            data = {
                'results': search_obj.get_results_list(),
                'alert': 'success',
                'results_count': len(search_obj.get_results_list())
            }
            return render_template('index.html', data=data)
        else:
            data = {
                'alert': 'danger'
            }
            return render_template('index.html', data=data)
            
    else: # is logic for GET
        data = {}
        return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(port=8802, debug=True)