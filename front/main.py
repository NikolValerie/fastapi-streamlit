import requests
import streamlit as st
import json

def main():

    st.title("Image classification")

    image = st.file_uploader("Choose an image", type=['jpg', 'jpeg'])

    if st.button("Classify!") and image is not None:
        st.image(image)
        files = {"file": image.getvalue()}
        res = requests.post("http://127.0.0.1:8002/classify", files=files)
        st.write(json.loads(res.text)['prediction'])

    txt = st.text_input('here')

    if st.button('send'):
        dat = {'text' : txt}
        res = requests.post("http://127.0.0.1:8003/clf_text", json=dat)

if __name__ == '__main__':
    main()
