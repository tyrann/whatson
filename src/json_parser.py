import json


class EmotionTone:
    def __init__(self, anger, disgust, fear, joy, sadness):
        self.anger = anger
        self.disgust = disgust
        self.fear = fear
        self.joy = joy
        self.sadness = sadness

    def __str__(self):
        return "Anger: {}, Disgust: {}, Fear: {}, Joy: {}, Sadness: {}".format(
            self.anger, self.disgust, self.fear, self.joy, self.sadness)

class WritingTone:
    def __init__(self, analytical, confident, tentative):
        self.analytical = analytical
        self.confident = confident
        self.tentative = tentative

    def __str__(self):
        return "Analytical: {}, Confident: {}, Tentative: {}".format(
            self.analytical, self.confident, self.tentative)

class SocialTone:
    def __init__(
        self,
        openness,
        conscientiousness,
        extraversion,
        agreeableness,
        neuroticism):

        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism

    def __str__(self):
        return ("Openness: {}, Conscientiousness: {}, Extraversion: {}, " +
            "Agreeableness: {}, Neuroticism: {}").format(
            self.openness, self.conscientiousness, self.extraversion,
            self.agreeableness, self.neuroticism)

class WatsonTone:
    def __init__(self, etone, wtone, stone):
        self.etone = etone
        self.wtone = wtone
        self.stone = stone

FAKE_TONES = [
    WatsonTone(EmotionTone(0, 0.5, 0.2, 0, 0), WritingTone(0, 0, 0), SocialTone(0, 0, 0, 0, 0))
]


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

    writing = WritingTone(
        writing_tone[0]["score"],
        writing_tone[1]["score"],
        writing_tone[2]["score"]
    )

    social = SocialTone(
        social_tone[0]["score"],
        social_tone[1]["score"],
        social_tone[2]["score"],
        social_tone[3]["score"],
        social_tone[4]["score"]
    )

    tone = WatsonTone(emotion, writing, social)

    return tone
