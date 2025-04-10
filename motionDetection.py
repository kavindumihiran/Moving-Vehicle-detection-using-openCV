import cv2

#  import the video from the folder
video_path = "videoFile.mp4"
video = cv2.VideoCapture(video_path)

# If there is an error while importing the video,
if not video.isOpened():
    print("Error while loading the image")
    exit()

bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=40, detectShadows=True)    # History - NUmber of frames used to learn the background (Higher values means slower adapt to changes but background model becomes more stable)
                                                                                                         # varThreshold - Controls how much a pixel should differ from the background to be considered as foreground.
                                                                                                         # Enables shadow detection (shadows appear as dark gray in the mask) (=127)
# If the video is correctly uploaded
while True:
    ret, frame = video.read()

    # If the frames are over ret will be 0
    if not ret:
        break

    # resize each frame to match with the screen size
    frame = cv2.resize(frame, (1520,790))

    # convert the images into Gray scale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply gaussian blur to each frame                                  # # Apply median filtering
    frame_gausBlur = cv2.GaussianBlur(frame_gray, (5,5), 0, 0)           # frame_median = cv2.medianBlur(frame_gausBlur, 5)

    # Apply background subtraction
    fg_mask = bg_subtractor.apply(frame_gausBlur)

    val, shadow_mask = cv2.threshold(fg_mask, 120, 255, cv2.THRESH_BINARY)

    kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

    opened_image = cv2.morphologyEx(shadow_mask, cv2.MORPH_OPEN, kernal)
    closed_image = cv2.morphologyEx(opened_image, cv2.MORPH_CLOSE, kernal)

    contours, hiera = cv2.findContours(closed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 10000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

    # show the video 
    cv2.imshow("Video feed", frame)

    # wait to press the key 'q'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()