import matplotlib.pyplot as plt
import numpy as np

def plot_emotions(etone):
    emotions = ("Anger", "Disgust", "Fear", "Joy", "Sadness")
    y_pos = np.arange(len(emotions))
    emotion_array = (etone.anger, etone.disgust, etone.fear, etone.joy, etone.sadness)
    font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 22}
    plt.rc('font', **font)
    bars = plt.barh(y_pos, emotion_array, align='center', alpha=1)
    bars[0].set_color('#ff9b79')
    bars[1].set_color('#c8ffe7')
    bars[2].set_color('#c6ffb4')
    bars[3].set_color('#feffad')
    bars[4].set_color('#8192e5')

    plt.xlim([0, 1])

    plt.yticks(y_pos, emotions)
    plt.xlabel('Intensity')
    plt.title('Emotional intensities')

    plt.savefig('../out/figure.png')

    # Clear figure
    plt.clf()
