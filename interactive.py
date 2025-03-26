# This is from copilot.
#Install the necessary libraries:

# pip install ipympl ipywidgets

# Enable the ipympl backend:

%matplotlib widget
# Create an interactive plot with a slider:

import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
from ipywidgets import interact

def update_plot(frequency):
    t = np.linspace(0, 1, 1000)
    y = np.sin(2 * np.pi * frequency * t)
    plt.figure(figsize=(10, 4))
    plt.plot(t, y)
    plt.title(f'Sine Wave with Frequency {frequency} Hz')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

interact(update_plot, frequency=widgets.FloatSlider(value=1.0, min=0.1, max=10.0, step=0.1))
Function to save the plot:

def save_plot(frequency, filename):
    t = np.linspace(0, 1, 1000)
    y = np.sin(2 * np.pi * frequency * t)
    plt.figure(figsize=(10, 4))
    plt.plot(t, y)
    plt.title(f'Sine Wave with Frequency {frequency} Hz')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.savefig(filename)
    print(f"Plot saved as {filename}")

# Example usage: Save the plot with a specific frequency and filename
save_plot(5.0, 'sine_wave.png')
Explanation:
Interactive Plot: The interact function from ipywidgets creates a slider to adjust the frequency of the sine wave. The plot updates in real-time as you move the slider.
Saving the Plot: The save_plot function generates a plot with the specified frequency and saves it to a file. You can call this function with the desired frequency and filename to save the plot.
Would you like to try this out, or do you need further assistance with any part of the code?

# Display the image

display(Image(filename='sine_wave.png'))

# Alternatively, you can use Matplotlib to load and display the image:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load and display the image
img = mpimg.imread('sine_wave.png')
plt.imshow(img)
plt.axis('off')  # Hide the axis
plt.show()
Example:
# Using IPython.display
from IPython.display import Image, display

# Display the image
display(Image(filename='sine_wave.png'))

# Using Matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load and display the image
img = mpimg.imread('sine_wave.png')
plt.imshow(img)
plt.axis('off')  # Hide the axis
plt.show()