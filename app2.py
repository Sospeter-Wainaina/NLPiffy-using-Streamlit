import streamlit as st

#NLP Packages
import spacy
import time
# from textblob import textblob

def text_analyzer(my_text):
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(my_text)

    tokens = [token.text for token in docx]
    return tokens
      
def main():
    '''NLP App with streamlit'''
    st.title("NLPiffy with Streamlit")
    st.subheader("Natural Language Processing on the go")

# Tokenization
    if st.checkbox("Show Tokens and Lemma"):
        st.subheader("Tokenize your text")
        message = st.text_area("Enter your text","Type here...")

        if st.button("Tokenize"):
            with st.spinner("Tokenizing... Please wait"):

                time.sleep(5)
            nlp_result = text_analyzer(message)
            st.success(nlp_result)
# Named Entity Recognition

# Sentiment Analysis

# Text Summarization




if __name__ == '__main__':
    main()