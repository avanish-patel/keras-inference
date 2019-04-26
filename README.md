# Image classification RESTful API
* An Image classification model serving using
1. Flask Web Framework
2. Keras NN Library
3. ResNet50 Pre-trained model

Run App using following command in terminal:
```
python keras-server.py
```

To hit the POST requst with image using cURL use following commands and it will show the prediction result in terminal:

For image dog.jpg
```
$ curl -X POST -F image=@dog.jpg 'http://localhost:8080/predict'
{
    "predictions": [
        {
            "label": "space_shuttle",
            "probability": 0.9999829530715942
        },
        {
            "label": "missile",
            "probability": 0.000014048131561139598
        },
        {
            "label": "projectile",
            "probability": 0.0000029701782295887824
        },
        {
            "label": "drilling_platform",
            "probability": 5.245008871668233e-10
        },
        {
            "label": "warplane",
            "probability": 2.0919946330799633e-10
        }
    ],
    "success": true
}
```
For rocket.jpeg
```
$ curl -X POST -F image=@rocket.jpeg 'http://localhost:8080/predict'
{
  "predictions": [
    {
      "label": "space_shuttle",
      "probability": 0.9999829530715942
    },
    {
      "label": "missile",
      "probability": 1.4048131561139598e-05
    },
    {
      "label": "projectile",
      "probability": 2.9701782295887824e-06
    },
    {
      "label": "drilling_platform",
      "probability": 5.245008871668233e-10
    },
    {
      "label": "warplane",
      "probability": 2.0919946330799633e-10
    }
  ],
  "success": true
}
```