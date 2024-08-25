import cv2

def apply_filters(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Apply different filters
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img, (15, 15), 0)
    edges = cv2.Canny(img, 100, 200)

    # Display results
    cv2.imshow('Original', img)
    cv2.imshow('Gray', gray)
    cv2.imshow('Blur', blur)
    cv2.imshow('Edges', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
apply_filters('c:\Users\Pathak\Documents\user_signup.png')
