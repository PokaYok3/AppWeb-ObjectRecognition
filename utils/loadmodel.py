import yolov5
#class model Yolov5
class YoloModel:
    def __init__(self,path='yolov5s.pt'):
        try:
            self.model = yolov5.load(path)  # Load from specified path
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None  # Set to None if loading fails
        self.model = yolov5.load('yolov5s.pt') #Pretrained model
        self.model.conf = 0.25  # NMS confidence threshold
        self.model.iou = 0.45  # NMS IoU threshold
        self.model.multi_label = True  # Multiple labels per box (adds 0.5ms/img)
    def returnmodel(self):
        return self.model
    def predict(self, img):
        return self.model(img)
    def showresults(self, results):
        results.show()
    def save(self, results,save_dir='results/'):
        results.save(save_dir)


