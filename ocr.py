import streamlit as st
import pytesseract
from pytesseract import Output
from PIL import Image
import numpy as np
import cv2

# ''' psm
# 0 = Orientation and script detection (OSD) only.
# 1 = Automatic page segmentation with OSD.
# 2 = Automatic page segmentation, but no OSD, or OCR. (not implemented)
# 3 = Fully automatic page segmentation, but no OSD. (Default)
# 4 = Assume a single column of text of variable sizes.
# 5 = Assume a single uniform block of vertically aligned text.
# 6 = Assume a single uniform block of text.
# 7 = Treat the image as a single text line.
# 8 = Treat the image as a single word.
# 9 = Treat the image as a single word in a circle.
# 10 = Treat the image as a single character.
# 11 = Sparse text. Find as much text as possible in no particular order.
# 12 = Sparse text with OSD.
# 13 = Raw line. Treat the image as a single text line,
#      bypassing hacks that are Tesseract-specific.
# '''

# ''' oem
# 0 = Original Tesseract only.
# 1 = Neural nets LSTM only.
# 2 = Tesseract + LSTM.
# 3 = Default, based on what is available.
# '''

# ---------WEB DEVELOPMENT USING STREAMLIT-----------------


st.set_page_config(page_title="Eyetech", layout="wide")

with st.container():
    
    left, right = st.columns((2))
    
    with left:

        st.title("Eyetech")
        st.write('##')
        
        title = '''<h5 style = "font-weight: 550; text-size-adjust: 100%;font-size: 35px; padding-bottom: 40px;">
                The <span style = "color:#06283D;"> Eyetech is an Optical Character Recognition </span> Web Application</h5>'''
        st.markdown(title,unsafe_allow_html = True)
        
        subtitle = '''<p style = "font-size: 17px; padding-bottom: 20px; padding-right:0;">It is a computer vision
                tech designed to extract texts from images while providing you multiple options to scan the image 
                depending on the content of the image. </p>'''
        st.markdown(subtitle,unsafe_allow_html = True)
        
        st.write('##')
        
    with right:
        
        st.image("home.png")

    st.write("---")
    
    # -------------HOW IT WORKS------------
    
    
with st.container():
    st.header("How it works!")
    st.write("""
                 Eyetech is an OCR technology. In the most basic form, it takes some inputs and produces extracted texts as outputs.
                 Following steps explain in detail how it woks:
                 
                 - There are two input fields overall , first allows you to make a selection between two given choices.
                 - This selection determines how application will take images as inputs, either using camera or using file uploader.
                 - Once the application recieves images, it will automatically scan the image and produce two outputs.
                 - First will be the actual image uploaded, in which all the recognised texts will be enclosed in a rectangular
                   and the text written below it.
                 - Second will be plain texts recognized from the image, Which can be copied.
                 - Now, Second input is also a selection between 3 to 13, defaulted at 6.
                 - This selection allows you to navigate through the different methods in which your image will be scanned.
                 - This may produce different outputs or no outputs based on the selection you made.
                 - This is provided to cover the different ways the texts are structured in images.
                 - Before using this selection, it is important to understand how each selection will allow the program
                   to scan your image.
                 
                 """)
    code = '''
                3 = Fully automatic page segmentation, but no OSD. (Default)
                4 = Assume a single column of text of variable sizes.
                5 = Assume a single uniform block of vertically aligned text.
                6 = Assume a single uniform block of text.
                7 = Treat the image as a single text line.
                8 = Treat the image as a single word.
                9 = Treat the image as a single word in a circle.
                10 = Treat the image as a single character.
                11 = Sparse text. Find as much text as possible in no particular order.
                12 = Sparse text with OSD.
                13 = Raw line. Treat the image as a single text line.
            '''
    
    st.code(code, language="")
    
    st.write('''
             - Most of them are self-explanatory but, do navigate through the methods to get the best results.
             - There is another field(slider) which allows you to adjust confidence factor of the first output that is image.
             - It may produce different image output based on the confidence factor you have adjusted to.
             - Do note that this does not affect the second output.
             
             ''')
    
    st.write("---")
    
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    
st.title("OCR")

col1, col2 = st.columns(2)
data = None
text = None

# ----------ACCEPTING INPUTS-----------

with col1:
    selection = st.selectbox(' ', ['Select an option','Upload an image', 'Scan Image using camera'])
    if selection == 'Scan Image using camera':
        data = st.camera_input(label = "scan textual image")
    elif selection == 'Upload an image':
        data = st.file_uploader('upload Image', type=['png','jpg','jpeg'])
            
with col2:
    psm = st.selectbox(' ', [ '3','4','5','6','7','8','9','10','11','12', '13',]) #accepting psm value
    conf = st.slider('confidence', 0, 100, 30)
    
    

myconfig = fr"--psm {psm} --oem 3" #Applying psm value
            
with col1:
    
    if data:
        
        
        image = Image.open(data)
        st.image(image, caption='Input', use_column_width=True)
        
        img_array = np.array(image)
        cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))
        img = cv2.imread('out.jpg')
        

        data = pytesseract.image_to_data(img, config = myconfig, output_type= Output.DICT)
        amount_boxes = len(data['text'])
        for i in range(amount_boxes):
            if float(data['conf'][i]) > conf:
                (x, y , width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
                img = cv2.rectangle(img, (x, y), (x+width, y+height), (0,255,0), 2)
                img = cv2.putText(img, data['text'][i], (x, y+height+10),cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
                
                
                
        with col2:
            st.image(img)
        
        text = pytesseract.image_to_string(image, config=myconfig, timeout=5, output_type= Output.STRING)
        if text:
            st.code(text, language = 'text')
        else:
            st.subheader('No Readable Text Discovered')
