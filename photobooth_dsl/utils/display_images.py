import cv2


def compare_images(og_window_title, og_image, mod_window_title, mod_image):

    cv_og_image = cv2.imread(og_image)
    cv2.imshow(og_window_title, cv_og_image)

    cv_mod_image = cv2.imread(mod_image)
    cv2.imshow(mod_window_title, cv_mod_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()