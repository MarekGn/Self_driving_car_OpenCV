import cv2
import time
from Controls import straight, right, left
from ScreenGetter import get_screen
from ImageProcessing import process_img


def run():
    wait_before_start()
    while True:
        screen = get_screen()
        new_screen, original_image, m1, m2 = process_img(screen)
        cv2.imshow('window', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
        if m1 < 0 and m2 < 0:
            right()
        elif m1 > 0 and m2 > 0:
            left()
        else:
            straight()
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


def wait_before_start():
    for i in list(range(5))[::-1]:
        print(i+1)
        time.sleep(1)


if __name__ == '__main__':
    run()
