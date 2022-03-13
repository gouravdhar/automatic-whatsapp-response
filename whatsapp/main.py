import pyautogui as pt
from time import sleep
import pyperclip

sleep(1)
global x, y

position = pt.locateOnScreen("smilie.png", confidence=.6)
x = position[0]
y = position[1]

def get_received_message():
    position = pt.locateOnScreen("smilie.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+100, y-45, duration=0.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(100, -170)
    pt.click()
    received_message = pyperclip.paste()

    print("Received Message: "+received_message)
    return received_message

def send_message(message):
    position = pt.locateOnScreen("smilie.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+100, y+50, duration=0.5)
    pt.click()
    pt.typewrite(message, interval = 0.01)
    pt.typewrite("\n", interval = 0.01)

def process_response(message):
    mes = str(message).lower()
    if "?" in str(mes):
        return "Nhi btaunga!"
    elif "Good morning" in str(mes):
        return "Good Night"
    elif "Hi" in str(message):
        return "Hi"
    else:
        return "Sb Badhiya hai"

def check_for_unread_messages():
    while True:
        try:
            position = pt.locateOnScreen("unread.png", confidence = 0.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(1)
        except(Exception):
            print("No new messages")

        if pt.pixelMatchesColor(int(x+100), int (y-35), (255, 255, 255), tolerance = 10):
            print("is_white - new message")
            received_message = get_received_message()
            message_to_send = process_response(received_message)
            send_message(message_to_send)
        else:
            print("no new message")
            


check_for_unread_messages()

