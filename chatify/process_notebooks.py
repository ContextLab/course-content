import os
from glob import glob as lsdir

import nbformat as nbf
from chatify import Chatify
from tqdm import tqdm
import numpy as np

import pickle

source_repo = 'NeuromatchAcademy'
mod_repo = 'ContextLab'


def get_tutorial_notebooks(basedir):
    return lsdir(os.path.join(basedir, 'tutorials', '*', '*Tutorial*.ipynb'))


def chatified(fname):
    notebook = nbf.read(fname, nbf.NO_CONVERT)
    header_cell = notebook['cells'][0]
    return mod_repo in header_cell['source']


def get_text(fname):
    with open(os.path.join(os.getcwd(), 'chatify', fname), 'r') as f:
        return ''.join(f.readlines())


def inject_chatify(fname):
    notebook = nbf.read(fname, nbf.NO_CONVERT)
    new_notebook = notebook.copy()

    # update header cell
    header_cell = new_notebook['cells'][0]
    if 'id' in header_cell['metadata']:
        del header_cell['metadata']['id']
    header_cell['source'] = header_cell['source'].replace(source_repo, mod_repo)

    # insert background cell
    background_cell = nbf.v4.new_markdown_cell(source=get_text('background.md'), metadata={'execution': {}})
    del background_cell['id']

    # insert davos cell
    davos_cell = nbf.v4.new_code_cell(source=get_text('install_davos.py'), metadata={'cellView': 'form', 'execution': {}})
    del davos_cell['id']

    # insert chatify cell
    chatify_cell = nbf.v4.new_code_cell(source=get_text('install_and_load_chatify.py'), metadata={'cellView': 'form', 'execution': {}})
    del chatify_cell['id']

    if chatified(fname):
        new_notebook.cells[0] = header_cell
        new_notebook.cells[1] = background_cell
        new_notebook.cells[2] = davos_cell
        new_notebook.cells[3] = chatify_cell
    else:
        new_notebook.cells.insert(1, background_cell)
        new_notebook.cells.insert(2, davos_cell)
        new_notebook.cells.insert(3, chatify_cell)

    # Write the file
    nbf.write(
        new_notebook,
        fname,
        version=nbf.NO_CONVERT,
    )


# def cache_responses(fname, tutor=None, prompts=None):
#     if tutor is None:
#         tutor = Chatify()
    
#     if prompts is None:
#         prompts = tutor._read_prompt_dir()['tutor']
    
#     notebook = nbf.read(fname, nbf.NO_CONVERT)
#     for cell in notebook['cells']:
#         if cell['cell_type'] == 'code':
#             for _, prompt in prompts.items():
#                 tutor._cache(cell['source'], prompt)

def compress_code(text):
    return '\n'.join([line.strip() for line in text.split('\n') if len(line.strip()) > 0])


def get_code_cells(fname):
    notebook = nbf.read(fname, nbf.NO_CONVERT)
    return [compress_code(cell['source']) for cell in notebook['cells'] if cell['cell_type'] == 'code']


tutorials = get_tutorial_notebooks(os.getcwd())
tutor = Chatify()
prompts = tutor._read_prompt_dir()['tutor']
code_cells = []

for notebook in tqdm(tutorials):
    inject_chatify(notebook)
    code_cells.extend(get_code_cells(notebook))

savefile = os.path.join(os.getcwd(), 'chatify', 'cache.pkl')
if os.path.exists(savefile):
    with open(savefile, 'rb') as f:
        cache = pickle.load(f)
else:
    cache = {}

tmpfile = os.path.join(os.getcwd(), 'chatify', 'tmp.pkl')
for cell in tqdm(np.unique(code_cells)):
    if cell not in cache:
        cache[cell] = {}
    
    for name, content in prompts.items():
        if name not in cache[cell]:
            cache[cell][name] = tutor._cache(cell, content)

            with open(tmpfile, 'wb') as f:
                pickle.dump(cache, f)

with open(savefile, 'wb') as f:
    pickle.dump(cache, f)

os.remove(tmpfile)