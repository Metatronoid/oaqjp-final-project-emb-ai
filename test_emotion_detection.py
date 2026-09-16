import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        joy_response = emotion_detector("I am glad this happened")["dominant_emotion"]
        anger_response = emotion_detector("I am really mad about this")["dominant_emotion"]
        disgust_response = emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        sadness_response = emotion_detector("I am so sad about this")["dominant_emotion"]
        fear_response = emotion_detector("I am really afraid that this will happen")["dominant_emotion"]

        self.assertEqual(joy_response, "joy")
        self.assertEqual(anger_response, "anger")
        self.assertEqual(disgust_response, "disgust")
        self.assertEqual(sadness_response, "sadness")
        self.assertEqual(fear_response, "fear")

unittest.main()