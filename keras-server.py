# import the neccessary packages
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import flask
import io

# initialize flask app and model
app = flask.Flask(__name__)
model = None

# load pretrained keras model
def load_model():
    global model
    model = ResNet50(weights='imagenet')

def prepare_image(image, target):
    # if image is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    return image

@app.route("/predict", methods=["POST"])
def predict():
    # init the data dictionary that will be returned
    data = {"success": False}

    #ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image in PIL format
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))

            # preprocess image and prepare it for classification
            image = prepare_image(image, target=(224,224))

            # classify the input image and init the list of predictions to return
            preds = model.predict(image)
            results = imagenet_utils.decode_predictions(preds)
            data["predictions"] = []

            # loop over the results and add to list of returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True
    
    # return the data dictionary as a JSON responose
    return flask.jsonify(data)

# if this is the main thread of execution first laod the
# model and then start the server
if __name__ == "__main__":
    print("🚀 Loading Keras model and Flask starting server...")
    print("🚀 Please wait until server has fully started...")
    load_model()
    app.run(host='0.0.0.0',port=8080,debug=False, threaded=False)



    





