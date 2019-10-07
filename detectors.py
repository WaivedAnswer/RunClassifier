import abc
import model_paths

from imageai.Prediction import ImagePrediction


class ObstacleDetector(abc.ABC):
    @abc.abstractmethod
    def classify(self, img):
        pass


class PredictionDetector(ObstacleDetector):
    obstacleTypes = ["horizontal_bar", "parallel_bars", "pole", "swing", "crane"]
    CUT_OFF = 80.0

    def __init__(self):
        self.prediction = ImagePrediction()
        self.prediction.setModelTypeAsInceptionV3()
        self.prediction.setModelPath(model_paths.inceptionPath)

        self.prediction.loadModel()

    def __isObstacle__(self, prediction, percent):
        return prediction in self.obstacleTypes and percent > self.CUT_OFF

    def classify(self, img):
        predictions, probability_percent = self.prediction.predictImage(input_type="array",
                                                                        image_input=img,
                                                                        result_count=2)

        for index in range(len(predictions)):
            prediction = predictions[index]
            percent = probability_percent[index]
            if self.__isObstacle__(prediction, percent):
                return prediction

        return None
