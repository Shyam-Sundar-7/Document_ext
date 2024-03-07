import streamlit as st
from helper_functions import image2, extract_text_from_docx, run_openai_task
labels = [
    "Agreement Value",
    "Aggrement Start Date",
    "Aggrement End Date",
    "Renewal Notice (Days)",
    "Party One",
    "Party Two"
]

# Define function to extract components and display results
def extract_and_display_components(file, text):
    st.text_area("Extracted Text", text, height=400)  
    if st.button("Extract Components"):
        with st.spinner("Extracting components..."):
            extracted_components = run_openai_task(labels=labels, text=text)
        st.text_area("Extracted Components", extracted_components, height=200)
        st.success("Successfully Extracted Components")

# Main content of the application
def main():
    st.title("Document Extraction - USEReady Assignment")

    st.header("Upload Document")
    file = st.file_uploader("Choose a file")
    if file is not None:
        file_extension = file.name.split(".")[-1]
        text = ""
        if file_extension in ["png", "jpg"]:
            st.write("The uploaded file is a PNG or JPG image.")
            text = image2(file)
        elif file_extension == "docx":
            st.write("The uploaded file is a DOCX document.")
            text = extract_text_from_docx(file)
        else:
            st.write("The uploaded file is not a PNG, JPG, or DOCX file.")
        extract_and_display_components(file, text)

if __name__ == "__main__":
    main()
