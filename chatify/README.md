# Why is this folder here?

This folder contains additional code and materials that are used to add [Chatify](https://github.com/ContextLab/chatify) support to the Neuromatch course materials.  If you're a Neuromatch student or "just visiting," you can likely ignore this directory.

# Developer instructions

This folder is organized as follows:

```
chatify
├── README.md: this file
├── background.md: a markdown file to be inserted into each tutorial notebook
├── install_and_load_chatify.py: a code cell to be inserted into each tutorial notebook; installs and loads chatify (provides LLM support for notebooks)
├── install_davos.py: a code cell to be inserted into each tutorial notebook; installs and loads davos (used for dependency management)
├── process_notebooks.py: script for inserting the background, davos, and chatify cells into existing notebooks
└── requirements.txt: dependencies needed for the process_notebooks scripts and for chatify
```

You'll probably want to do one of two things:
1. Inject chatify support into tutorial materials.  To do that, install the requirements in this folder (`pip install -r requirements.txt`) and then run the `process_notebooks.py` script (`python process_notebooks.py`).
2. Edit the background text and/or code that gets injected into the tutorial notebooks.  Simply edit `background.md`, `install_davos.py`, and/or `install_and_load_chatify.py` and re-run the `process_notebooks.py` script.  Existing "chatified" notebooks will be updated, and not-yet-chatified notebooks will be injected with the modified content.

If you want to add something cool, consider submitting a [pull request](https://github.com/ContextLab/course-content/pulls) so that others can benefit from your efforts!  And of course, if you encounter a problem, feel free to submit an [issue](https://github.com/ContextLab/course-content/issues) describing what's going on so that we can fix it!