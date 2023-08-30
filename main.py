import streamlit as st
import pickle
from mlm import extract_features

loaded_model = pickle.load(open('model.pkl', 'rb'))

st.title('Malicious URL Detection')
url_input = st.text_input('Enter the URL')

if st.button('Predict'):
    if url_input:
        features = extract_features(url_input)
        prediction = loaded_model.predict([features])

        if int(prediction[0]) == 0:
            res = "SAFE"
        elif int(prediction[0]) == 1:
            res = "DEFACEMENT"
        elif int(prediction[0]) == 2:
            res = "PHISHING"
        elif int(prediction[0]) == 3:
            res = "MALWARE"

        st.write(f'Prediction: {res}')
    else:
        st.write('Please enter a URL')
