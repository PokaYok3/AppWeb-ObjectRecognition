#Imports
from utils.loadmodel import YoloModel
import cv2
import numpy as np
from flask import Flask,render_template,Response

app=Flask(__name__)
#Create cap instance
cap=cv2.VideoCapture(0) #Establish a connection with the camera

def aplicacion():
        
    model=YoloModel('utils/yolov5s.pt')
    classes = open('utils/coco.names').read().strip().split('\n')

    while True:

        #read the frame
        res,frame = cap.read()

        if not res:
            break
        else:
            #Predict the result
            results = model.predict(frame)
            predictions = results.pred[0]
            boxes = predictions[:, :4] # x1, y1, x2, y2
            scores = predictions[:, 4]
            categories = predictions[:, 5]
            #Draw the bounding boxes and the labels on the image
            for box, score, category in zip(boxes, scores, categories):
                color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
                x1 = int(box[0])
                y1 = int(box[1])
                x2 = int(box[2])
                y2 = int(box[3])
                #label = f"{classes[int(category.item())]}, Score: {score:.2f}" 
                label = f"{classes[int(category.item())]}" 
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
            
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            #cv2.imshow("Results",frame)
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(aplicacion(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)