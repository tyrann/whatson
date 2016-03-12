import matplotlib.pyplot as plt
import numpy as np

def plot(anger, disgust, fear, joy, sadness):
    emotions = ("Anger", "Disgust", "Fear", "Joy", "Sadness")
    y_pos = np.arange(len(emotions))
    performance = (anger, disgust, fear, joy, sadness)

    plt.barh(y_pos, performance, align='center', alpha=0.4)
    plt.yticks(y_pos, emotions)
    plt.xlabel('Intensity')
    plt.title('Emotional intensities')

    plt.show()
