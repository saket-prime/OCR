import streamlit as st
from PIL import Image
import pytesseract



st.markdown("-----")
selection = st.selectbox(' ', ['Select an option','Upload an image', 'Scan Image using camera'])
col1, col2 = st.columns(2)
data = None
text = None
# with col1:
if selection == 'Scan Image using camera':
         data = st.camera_input(label = "scan textual image")
elif selection == 'Upload an image':
         data = st.file_uploader('upload Image', type=['png','jpg','jpeg'])
# with col2:
if data:
         st.image(data)
         img = Image.open(data)
         text = pytesseract.image_to_string(img)
st.markdown("-----")

if text:
    st.code(text, language = 'text')
    
    

# myconfig = r"--psm 6 --oem 1"

# img = cv2.imread('images/img2.jpg')
# # height, width, _ = img.shape

# data = pytesseract.image_to_data(img, config = myconfig, output_type= Output.DICT)

# amount_boxes = len(data['text'])
# for i in range(amount_boxes):
#     if float(data['conf'][i]) > 50:
#         (x, y , width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
#         img = cv2.rectangle(img, (x, y), (x+width, y+height), (0,255,0), 2)
#         img = cv2.putText(img, data['text'][i], (x, y+height+10),cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

# cv2.imshow("img", img)
# cv2.waitKey(0)









# import streamlit as st
# import pytesseract
# from pytesseract import Output
# from PIL import Image
# import numpy as np
# import cv2

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

# myconfig = r"--psm 6 --oem 3"

# st.markdown("-----")
# selection = st.selectbox(' ', ['Select an option','Upload an image', 'Scan Image using camera'])
# col1, col2 = st.columns(2)
# data = None
# text = None
# # with col1:
# if selection == 'Scan Image using camera':
#          data = st.camera_input(label = "scan textual image")
# elif selection == 'Upload an image':
#          data = st.file_uploader('upload Image', type=['png','jpg','jpeg'])
         

# if data:
#     image = Image.open(data)
#     st.image(image, caption='Input', use_column_width=True)
#     img_array = np.array(image)
#     cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))

#     img = cv2.imread('out.jpg')
#     # height, width, _ = img.shape

#     data = pytesseract.image_to_data(img, config = myconfig, output_type= Output.DICT)

#     amount_boxes = len(data['text'])
#     for i in range(amount_boxes):
#         if float(data['conf'][i]) > 50:
#             (x, y , width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
#             img = cv2.rectangle(img, (x, y), (x+width, y+height), (0,255,0), 2)
#             img = cv2.putText(img, data['text'][i], (x, y+height+10),cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

#     # cv2.imshow("img", img)
#     st.image(img)
    

#     text = pytesseract.image_to_string(image, config=myconfig, output_type= Output.STRING)

# if text:
#     st.code(text, language = 'text')
# else:
#     st.subheader('No Readable Text Discovered')