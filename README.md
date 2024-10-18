# Cover Letter Generator
This is a web-application which generates cover letters using a fine-tuned version of Llama3.2. 

## Usage Instructions:

### Step 1: Setting up the environment

Run the command on your terminal `pip install -r requirements.txt` to install all the necessary libraries and packages for the project.
If you are using MacOS, some of the packages may not be available, therefore consider using online environments for finetuning the model

### Step 2: Setting up HuggingFace

Create a .env file and setup your HuggingFace API Key as: 
`HUGGINGFACE_API_KEY = 'your API Key'`

### Step 3: Run the application:

Run the command on your terminal `streamlit run app.py`

## Resources

Orignal Dataset Link: https://huggingface.co/datasets/ShashiVish/cover-letter-dataset

Dataset Link: https://huggingface.co/datasets/dhruvvaidh/cover-letter-dataset-llama3

Huggingface Model Link: https://huggingface.co/dhruvvaidh/cover-letter-gen-llama3 
