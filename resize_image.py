import cv2
import sys

def resize_image(input_image_path, output_image_path, width, height):
    # Read the input image
    image = cv2.imread(input_image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return
    
    # Resize the image to the specified width and height
    image = cv2.resize(image, (width, height))
    # Save the resized image to the specified output path
    cv2.imwrite(output_image_path, image)
    print(f"Image saved to {output_image_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python resize_image.py <input_image_path>  <width> <height>")
        sys.exit(1)
    
    input_image_path = sys.argv[1]
    output_image_path = input_image_path #sys.argv[2]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    
    resize_image(input_image_path, output_image_path, width, height)
