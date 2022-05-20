import os
import nbformat
FINAL_IPYNB='final_notebook.ipynb'
for file in os.listdir():
    if file.endswith(".ipynb") and file!=FINAL_IPYNB:
        print(file)
        if os.path.exists(FINAL_IPYNB):
            first_notebook = nbformat.read(FINAL_IPYNB, 4)
            second_notebook = nbformat.read(file, 4)
            final_notebook = nbformat.v4.new_notebook(metadata=first_notebook.metadata)
            final_notebook.cells = first_notebook.cells + second_notebook.cells
        else:
            second_notebook = nbformat.read(file, 4)
            final_notebook = nbformat.v4.new_notebook(metadata=second_notebook.metadata)
            final_notebook.cells = second_notebook.cells
        nbformat.write(final_notebook, FINAL_IPYNB)