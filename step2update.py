import cv2
import mediapipe as mp
import numpy as np


mp_selfie_segmentation = mp.solutions.selfie_segmentation
segment = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)


bg_image = cv2.imread("img2.jpg")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

prev_mask = None
SMOOTHING = 0.7

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    bg_resized = cv2.resize(bg_image, (frame.shape[1], frame.shape[0]))

    results = segment.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    mask = results.segmentation_mask


    if prev_mask is None:
        prev_mask = mask
    else:
        mask = SMOOTHING * prev_mask + (1 - SMOOTHING) * mask
        prev_mask = mask


    mask = cv2.GaussianBlur(mask, (7, 7), 0)


    mask_3ch = np.repeat(mask[:, :, np.newaxis], 3, axis=2)


    output = (frame * mask_3ch + bg_resized * (1 - mask_3ch)).astype(np.uint8)

    cv2.imshow("Virtual Background", output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
