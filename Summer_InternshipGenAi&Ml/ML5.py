import numpy as np
import matplotlib.pyplot as plt

def create_custom_image():
    # Create a 100x100 RGB image with random colors
    image = np.random.rand(100, 100, 3)
    
    # Set a particular area to a specific color (e.g., red)
    image[25:75, 25:75] = [1, 0, 0]  # Red color
    
    plt.imshow(image)
    plt.show()

create_custom_image()
