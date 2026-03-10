import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input,decode_predictions
from tensorflow.keras.preprocessing import image
model=MobileNetV2(weights='imagenet')
def detect_species(img_path):
    img=image.load_img(img_path,target_size=(224,224))
    x=image.img_to_array(img)
    x=np.expand_dims(x,axis=0)
    x=preprocess_input(x)
    preds=model.predict(x)
    result=decode_predictions(preds,top=1)[0]
    species=result[0][1]
    confidence=result[0][2]
    return species,confidence