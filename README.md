# Python Text Finder App
App is a web based app, that can read excel and text files to find if specific text exists in file.  


![Logo](https://github.com/iamlu-coding/python-text-finder/blob/main/app-screen-shot.png)

## Run Locally

Clone the project

```bash
  git clone https://github.com/iamlu-coding/python-text-finder.git
```

Go to the project directory

```bash
  cd python-text-finder
```

Create Virtual Environment
```bash
python -m venv env
```
Activiate Virtual Environments

Windows
```bash
source env/Script/activate
```
Mac/Linux
```bash
source env/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```

## Compile to .exe

To make app executable.
For newer Python version (3.10) you may receive error. 

```bash
  pyinstaller app.py or pyinstaller app.py --exclude-module _bootlocale
```
    