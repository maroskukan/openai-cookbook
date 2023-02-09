# OpenAI Cookbook

## Introduction

*The other day I found myself in a major city. I was out of town and exploring the downtown area. I had been there before, but it had been a few years since my last visit. As I walked around, I noticed something that I hadn’t noticed before: the prevalence of street art. Everywhere I looked, there were colorful murals, graffiti, and stencils adorning the walls of buildings and alleyways. I was amazed at the creativity and skill of the artists who had created these works of art.*

*It made me think about how street art is often seen as a form of vandalism or graffiti. But I also began to realize that it can be so much more than that. Street art has the power to transform a cityscape and create a sense of community and pride. It can be a way to express yourself, to share your story, or to make a statement. It can be a way to bring people together and to inspire dialogue and discussion.*

*Street art is a powerful form of expression and it can be a great way to bring color and life to an otherwise dull cityscape. It’s amazing to see how it can transform a city and bring people together.*


## Installation

In order to execute the scripts in the `recipes` folder, you need to make sure you have installed certain prerequsities.I highly recommend installing inside a virtual environment, for example using the [Simple Python Version Mamangement](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) tool.

```bash
# Download and Install Python 3.11.1
pyenv install 3.11.1

# Create and activate virtual envrionment
pyenv virtualenv 3.11.1 openai-cookbook
pyenv activate openai-cookbook

# Update pip, setuptools and install:
# - requests
# - openai
pip install --upgrade pip setuptools
pip install -r requirements.txt
```

## Usage

In order to interact with the OpenAI API using scripts in `recipes`, you need to provide an API key as environment variable.

```bash
export API_KEY="your-api-key"
```

### Model text-davinci-003

Start exploring the API with sample script:

```bash
./text-davinci-003.py
What is your question? (or 'exit' to quit) What model are you using to answer my questions?


We are using a variety of models to answer your questions, including regression models, machine learning models, and decision tree models.

What is your question? (or 'exit' to quit) exit

Exiting...
```