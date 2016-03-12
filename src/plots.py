import matplotlib.pyplot as plt
import numpy as np

colors = {
    'red': '#ff9b79',
    'light-blue': '#c8ffe7',
    'green': '#c6ffb4',
    'yellow': '#feffad',
    'dark-blue': '#8192e5'
}

def plot_emotions(etone):
    params = ("Anger", "Disgust", "Fear", "Joy", "Sadness")
    y_pos = np.arange(len(params))
    emotion_tuple = (etone.anger, etone.disgust, etone.fear, etone.joy, etone.sadness)

    bars = plt.barh(y_pos, emotion_tuple, align="center")
    bars[0].set_color(colors['red'])
    bars[1].set_color(colors['light-blue'])
    bars[2].set_color(colors['green'])
    bars[3].set_color(colors['yellow'])
    bars[4].set_color(colors['dark-blue'])

    plt.xlim([0, 1])

    plt.yticks(y_pos, params)
    plt.xlabel('Intensity')
    plt.title('Emotional intensities')

    plt.savefig('../out/figure.png')

    # Clear figure
    plt.clf()

def plot_writing(wtone):
    params = ("Analytical", "Confident", "Tentative")
    y_pos = np.arange(len(params))
    writing_tuple = (wtone.analytical, wtone.confident, wtone.tentative)

    bars = plt.barh(y_pos, writing_tuple, align="center")
    bars[0].set_color(colors['yellow'])
    bars[1].set_color(colors['green'])
    bars[2].set_color(colors['light-blue'])

    plt.xlim([0, 1])

    plt.yticks(y_pos, params)
    plt.xlabel('Intensity')
    plt.title('Writing characteristics')

    plt.savefig('../out/figure.png')

    # Clear figure
    plt.clf()

def plot_social(stone):
    params = ("Openness", "Conscientiousness", "Extraversion", "Agreeableness",
        "Neuroticism")
    y_pos = np.arange(len(params))
    social_tuple = (stone.openness, stone.conscientiousness, stone.extraversion,
        stone.agreeableness, stone.neuroticism)

    bars = plt.barh(y_pos, social_tuple, align="center")
    bars[0].set_color(colors['dark-blue'])
    bars[1].set_color(colors['green'])
    bars[2].set_color(colors['light-blue'])
    bars[3].set_color(colors['yellow'])
    bars[4].set_color(colors['red'])
    plt.xlim([0, 1])

    plt.yticks(y_pos, params)
    plt.xlabel('Intensity')
    plt.title('Social characteristics')

    plt.savefig('../out/figure.png')

    # Clear figure
    plt.clf()
