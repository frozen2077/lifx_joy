import cv2
import numpy as np
import colorsys

def rgb_to_hsv(rgb):
  """
  Converts an RGB color value to HSV.

  Args:
      rgb (tuple): A tuple containing the RGB values (red, green, blue) in the range of 0 to 255.

  Returns:
      tuple: A tuple containing the HSV values (hue, saturation, value).
  """
  r, g, b = rgb  # Unpack the RGB values
  r, g, b = r / 255.0, g / 255.0, b / 255.0  # Convert each to a range from 0 to 1
  h, s, v = colorsys.rgb_to_hsv(r, g, b)
  h = (int)(h * 360)  # Convert hue to degrees
  s = (int)(s * 100)
  v = (int)(v * 100)
  return [h, s, v, 1500]


def image_to_hsv_matrix(image_path, target_size=(5, 6)):
  """
  Converts an image to a 6x5 pixel representation and extracts its HSV values.

  Args:
      image_path (str): Path to the image file.
      target_size (tuple, optional): Desired output size (width, height). Defaults to (5, 6).

  Returns:
      numpy.ndarray: A 6x5 numpy array containing the average HSV values for each downsampled region.
  """

  # Read the image
  image = cv2.imread(image_path)

  # Resize the image to the target size
  resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
  hsv_image = resized_image[:,:,::-1]
  hsv_image = ([rgb_to_hsv(hsv_image[i,j]) for i in range(hsv_image.shape[0]) for j in range(hsv_image.shape[1])])
  print(hsv_image)

  return hsv_image


if __name__ == "__main__":
    image_path = "D:\\Desktop\\4.jpg"  # Replace with your image path
    print(image_to_hsv_matrix(image_path))

