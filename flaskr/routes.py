from flask import render_template, flash, render_template, request, redirect
from werkzeug.utils import secure_filename
from .model import extract_vector, get_extract_model
from .utils import allowed_file
import os
from .constants import *
import flaskr.search_image as si

def home(model = None):
    index, _, all_paths = si.load_index()

    if request.method == 'POST':
        if 'input_image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['input_image']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if model == None:
            flash('Not found model')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(os.getcwd(), UPLOAD_FOLDER, filename)
            file.save(save_path)
            model = get_extract_model()
            search_vector = extract_vector(model, save_path)
            q = int(request.form.get("quantity"))
            D, I = si.search(index, search_vector, all_paths, q)
            return render_template('home.html', img_name=filename, d=D, images=I)

        return render_template('home.html')

    return render_template('home.html')
