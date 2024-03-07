# Document Extraction - USEReady Assignment

## Table of Contents

1. [extraction_(doc,png,jpg)_to_text.ipynb](extraction_(doc,png,jpg)_to_text.ipynb):
   - This notebook explains the process of extracting text from image (PNG, JPG) and document (DOC) files. It utilizes pytesseract for image files and the open-docx library for document files to extract the text. Additionally, it demonstrates the creation of training and testing CSV files with attributes such as the file name and extracted text.

2. [using_openai.ipynb](using_openai.ipynb):
   - This notebook outlines the steps for implementing the zero-shot prompting method to extract the required labels from files or images. It discusses the performance of this method, highlighting its effectiveness in certain cases and limitations in others.

3. [one_shot_prompting.ipynb](one_shot_prompting.ipynb):
   - This notebook utilizes OpenAI chat completion with a prompting approach. It involves three roles: the system (acting as the NLP extractor), the assistance (providing examples), and the user (providing input text). The notebook compares the results obtained from this approach with those from the zero-shot prompting method.

To make the it as a running application, I have implemented the streamlit application.
Here helper_function.py contains all the functions necessary to be included in the main app.py
This is to make sure the app.py is relaible to read and short.


## Running the Streamlit Application

To run the Streamlit application:

1. Clone the repository:
   ```
   git clone https://github.com/Shyam-Sundar-7/Document_ext.git
   ```

2. Create a virtual environment and install the dependencies from requirements.txt.

    ```
    python -m venv env
    source env/bin/activate  # Activate the virtual environment
    pip install -r requirements.txt
    ```

3. Store the OpenAI API key in a .env file (create it if it does not exist):

    ```
    OPENAI_API_KEY=sk-**************************************
    ```

4. Run the Streamlit application using the following command:

    ```
    streamlit run app.py
    ```

# Streamlit Local execution video:
[Streamlit](https://github.com/Shyam-Sundar-7/Document_ext/assets/101181076/b7c3dc7f-da64-4e54-a158-2bbdddca0a3d)
