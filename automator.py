import keyboard
import pyautogui
import time
import json

def record_macro():
    macro = []
    start = time.time()

    while True:
        event = keyboard.read_event()
        if event.name == 'esc':
            break

        delay = time.time() - start
        start = time.time()

        if event.event_type == 'down':
            macro.append({
                'type': 'key',
                'key': event.name,
                'delay': delay
            })
        
    with open("macro.json", "w") as f:
        json.dump(macro, f)
    
    print("Recording saved to macro.json.")

def play_macro():
    with open("macro.json", "r") as f:
        macro = json.load(f)

    print("Running macro in 3 seconds...")
    time.sleep(3)

    for action in macro:
        time.sleep(action['delay'])

        if action['type'] == 'key':
            pyautogui.press(action['key'])
if __name__ == "__main__":
    mode = input("Enter 'r' to record or 'p' to play: ").strip().lower()

    if mode == 'r':
        record_macro()
    elif mode == 'p':
        play_macro()
    else:
        print("Invalid option.")