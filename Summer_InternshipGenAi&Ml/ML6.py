import cv2

def apply_cool_filters():
    # Load the face cascade and sunglasses image
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    sunglasses = cv2.imread('d:\1.JPG', -1)  # Load with alpha channel

    # Start webcam, try different indices if 0 doesn't work
    cap = cv2.VideoCapture(0)  
    if not cap.isOpened():
        print("Error opening video stream or file")
        return

    while True:
        ret, frame = cap.read()
        if not ret:  # Check if a frame was successfully read
            print("Can't receive frame (stream end?). Exiting ...")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            # Resize sunglasses to fit the face width
            sunglasses_resized = cv2.resize(sunglasses, (w, int(h/3)))

            # Determine region of interest (ROI)
            roi = frame[y:y+sunglasses_resized.shape[0], x:x+sunglasses_resized.shape[1]]

            # Create masks
            sunglasses_mask = sunglasses_resized[:, :, 3]
            sunglasses_mask_inv = cv2.bitwise_not(sunglasses_mask)
            roi_bg = cv2.bitwise_and(roi, roi, mask=sunglasses_mask_inv)
            roi_fg = cv2.bitwise_and(sunglasses_resized[:, :, 0:3], sunglasses_resized[:, :, 0:3], mask=sunglasses_mask)

            # Add the sunglasses to the ROI
            dst = cv2.add(roi_bg, roi_fg)
            frame[y:y+sunglasses_resized.shape[0], x:x+sunglasses_resized.shape[1]] = dst

        # Display the resulting frame
        cv2.imshow('Cool Filters', frame)

        # Break the loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

apply_cool_filters()
   
