import cv2
import numpy as np
import pyautogui
import time #匯入相關模組

def click_image(image, pos,  action, timestamp, offset=10):
    img = cv2.imread(image)
    height, width, channels = img.shape
    pyautogui.moveTo(pos[0]+ offset , pos[1]+ offset , timestamp)
    pyautogui.click(button=action) 

def imagesearch(image, precision=0.5): #設定一個函式
    im = pyautogui.screenshot()
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        print("沒找到")
        return [50,50]
    print(max_val)    
    return max_loc   

pp =imagesearch("./test.jpg")
click_image("./test.jpg", pp, "left", 1) 

#返回圖片座標 
#尋找1.png的圖。(把圖跟程式放同一個目錄下)
#要點右鍵的話，就把"left"改成 "right", 最後的參數1，代表滑鼠移動到目標的時候。設越長，滑鼠移動越慢。