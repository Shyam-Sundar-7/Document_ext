# C:\Program Files\Tesseract-OCR
from openai import OpenAI
from dotenv import load_dotenv
import os
import pytesseract as pyt
import cv2
from docx import Document
import numpy as np
pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

load_dotenv()
def image(file):
    img = cv2.imread(file)
    text = pyt.image_to_string(img)
    return text.strip()

def image2(file):
    nparr = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    text = pyt.image_to_string(img)
    return text.strip()


def extract_text_from_docx(docx_file):
    # Load the DOCX file
    doc = Document(docx_file)
    
    # Initialize an empty string to store the extracted text
    text = ""
    
    # Iterate through paragraphs in the document and concatenate the text
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    
    return text.strip()




def system_message(labels):
    return f"""
You are an expert in Natural Language Processing. Your task is to identify Named Entities (NER) in a Rental agreement document.
The possible Named Entities (NER) types are exclusively: ({", ".join(labels)})."""

def assisstant_message():
    return """EXAMPLE:
        Text:"House Rental Contract
KNOWN ALL MEN BY THESE PRESENTS:
This House Rental Contract, made and entered into this 20th day of May 2007 at Manila by and between:
Antonio Levy S. Ingles. Jr. and/or Mary Rose C. Ingles, of legal age, with residence and postal address at Unit 2006 EGI Taft Tower 2339 Taft Avenue, Malate, Manila, And herein referred to as the Owner(s),
� And �
GERALDINE O. GALINATO. of legal age, with residence and postal address at 6 Manganese Road, Pilar Village, Las Pinas, Metro Manila, And herein referred to as the
Resident(s),
WITNESSETH:
In consideration of the agreements of the Resident(s), known as: GERALDINE O. GALINATO. the Owner(s), known as: Antonio Levy S. Ingles. Jr. and/or Mary Rose C. Ingles, hereby rent their the dwelling/house located at Lot 6, Block 20, Royal South Townhomes, Marcos Alvarez Avenue, Talon 5, Las Pinas City, Metro Manila for the period commencing on the 20th day of May, 2007, and monthly thereafter until the 20th day of May, 2008, at which time this Agreement is terminated.
Resident(s), in consideration of Owner(s) permitting them to occupy the above property, hereby agrees to the following terms:
RENT: To pay as rental the sum of SIX THOUSAND FIVE HUNDRED PESOS IP 6.500.001 per month, due and payable in advance from the 20th day of every month.
FAILURE TO PAY ON TIME: Failure to pay the rent will result in being served a Notice to End Residential Tenancy. This Notice may be served if you have an outstanding balance from failure to pay your rent. This Notice may also be served from being habitually late in paying your rent regardless of the balance owed. Once the Notice to End Residential Tenancy is received, you will have a prescribed time to pay all of the amount overdue on your rent. A three-dav grace period will be allowed for late payment. Failure to pay the monthly rental within the grace period is subject to FIVE (5%) PERCENT interest per month of delay as penalty.
Habitual failure of the Resident(s) to pay within the prescribed time shall result in the Owner(s) taking immediate legal action to evict the Resident(s) from the premises and seize the security deposit.
SECURITY DEPOSIT: Resident(s) agrees to pay a deposit in the amount of SIX THOUSAND FIVE HUNDRED PESOS (P 6.500.001 to secure Resident(s)�s pledge of full compliance with the terms of this agreement. Note: THE DEPOSIT MAY NOT BE USED BY TENANT TO PAY THE RENT DURING THE TENANCY. The security deposit will be used at the end of the tenancy to compensate the Owner(s) for any damages or unpaid rent or charges, and will be repaired or replaced at Resident(s)�s expense with funds other than the deposit.
METHOD OF PAYMENT: The initial advance payment of rent and deposit under this contract be PAID IN CASH at least 7 days before the date of moving-in. Thereafter, monthly rent payments must be paid by POST DATED CHECKS payable to ANTONIO LEVY S. INGLES. JR. until a first check is dishonored and returned unpaid. Regardless of cause, no other additional payments may afterwards be made by check. Checks returned will not be redeposited. The Resident(s) will be notified by a 3 day notice, and will be required to pay the amount due in cash."
        {{
    "Agreement Value": 6500,
    "Agreement Start Date": 0.860034722,
    "Agreement End Date": 0.860046296,
    "Renewal Notice (Days)": 15,
    "Party One": "Antonio Levy S. Ingles, Jr. and/or Mary Rose C. Ingles",
    "Party Two": "GERALDINE Q. GALINATO"
        }}
    --"""

def user_message(text):
    return f"""
TASK:
    Text: {text}
"""

OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def run_openai_task(labels, text):
    messages = [
          {"role": "system", "content": system_message(labels=labels)},
          {"role": "assistant", "content": assisstant_message()},
          {"role": "user", "content": user_message(text=text)}
      ]

    # TODO: functions and function_call are deprecated, need to be updated
    # See: https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools

    client = OpenAI()

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    return completion.choices[0].message.content