import json

class EmotionTone:
    def __init__(self, anger, disgust, fear, joy, sadness):
        self.anger = anger
        self.disgust = disgust
        self.fear = fear
        self.joy = joy
        self.sadness = sadness

class WritingTone:
    def __init__(self, analytical, confident, tentative):
        self.analytical = analytical
        self.confident = confident
        self.tentative = tentative
class SocialTone:
    def __init__(
        self,
        openness_big5,
        conscientiousness_big5,
        extraversion_big5,
        agreeableness_big5,
        neuroticism_big5):

        self.openness_big5 = openness_big5
        self.conscientiousness_big5 = conscientiousness_big5
        self.extraversion_big5 = extraversion_big5
        self.agreeableness_big5 = agreeableness_big5
        self.neuroticism_big5 = neuroticism_big5

class WatsonTone:
    def __init__(self, etone, wtone, stone):
        self.etone = etone
        self.wtone = wtone
        self.stone = stone


def parse(json_data):
    tones = json_data["document_tone"]["tone_categories"]

    emotion_tone = tones[0]["tones"]
    writing_tone = tones[1]["tones"]
    social_tone = tones[2]["tones"]

    emotion = EmotionTone(
        emotion_tone[0]["score"],
        emotion_tone[1]["score"],
        emotion_tone[2]["score"],
        emotion_tone[3]["score"],
        emotion_tone[4]["score"]
    )

    writing = None

    social = None

    tone = WatsonTone(emotion, writing, social)

    return tone
