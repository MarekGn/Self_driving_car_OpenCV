import pyautogui
import time


def straight():
    pyautogui.keyDown("up")
    time.sleep(0.02)
    pyautogui.keyUp("up")
    pyautogui.keyUp("left")
    pyautogui.keyUp("right")


def right():
    pyautogui.keyDown("right")
    pyautogui.keyDown("up")
    pyautogui.keyUp("up")
    pyautogui.keyUp("right")


def left():
    pyautogui.keyDown("left")
    pyautogui.keyDown("up")
    pyautogui.keyUp("up")
    pyautogui.keyUp("left")
