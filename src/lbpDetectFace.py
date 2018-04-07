import numpy as np
import cv2


def detect_faces(f_cascade, colored_img, scale_factor=1.1):
    img_copy = np.copy(colored_img)
    # convert to gray
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

    faces = f_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=6)

    return faces


def draw_faces(img, faces):
    # draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img


def get_largest_face(img, faces):
    # draw and crop largest face
    largest_face = 0
    a = b = c = d = 0
    for (x, y, w, h) in faces:
        if (w*h) >= largest_face:
            largest_face = w*h
            a = x
            b = y
            c = w
            d = h

    crop_img = img[b:b + d, a:a + c]
    return crop_img
