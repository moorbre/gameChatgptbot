import pyautogui
import time
import keyboard
from ChatgptHandler import ChatgptHandler

def cs_type_text(text, interval=0.001, input_limit=100, open_chat_key='enter', send_chat_key='enter', chat_closes_on_send=False):

    #pyautogui.press(open_chat_key)
    #time.sleep(0.5)

    chunks = split_string_on_spaces(text, input_limit)

    for chunk in chunks:
        pyautogui.typewrite(chunk)
        time.sleep(3)

def rocketleague_type_text(text, interval=0.001, input_limit=100, open_chat_key='enter', send_chat_key='enter', chat_closes_on_send=False):

    chunks = split_string_on_spaces(text, input_limit)

    for chunk in chunks:
        pyautogui.typewrite(chunk, interval=0.01)
        time.sleep(3)

def beta_rocketleague_type_text(text, interval=0.001, input_limit=100, open_chat_key='enter', send_chat_key='enter', chat_closes_on_send=False):

    #time.sleep(0.5)

    chunks = split_string_on_spaces(text, input_limit)

    pyautogui.typewrite(open_chat_key)
    for chunk in chunks:
        pyautogui.typewrite(chunk, interval=0.01)
        pyautogui.typewrite(open_chat_key)
        pyautogui.typewrite('enter')

def split_string_on_spaces(input_string, max_length=100):
    # Check if the input string is empty
    if not input_string:
        return []

    # Initialize an empty list to store the split strings
    result = []

    # Split the input string into words
    words = input_string.split()

    # Initialize variables to keep track of the current substring and its length
    current_substring = ""
    current_length = 0

    # Iterate through the words
    for word in words:
        # Check if adding the current word exceeds the maximum length
        if current_length + len(word) > max_length:
            result.append(current_substring.strip())
            current_substring = ""
            current_length = 0

        # Add the current word to the current substring
        current_substring += f"{word} "
        current_length += len(word) + 1  # Account for the space between words

    # Add the last substring to the result
    if current_substring:
        result.append(current_substring.strip())

    return result

def on_key_event(e): 
    if e.event_type == keyboard.KEY_DOWN:
        #print(e.name)

        if e.name == 'f1' and keyboard.is_pressed('ctrl'):
            text_to_type = "switch"
            cs_type_text(text_to_type, open_chat_key='', chat_closes_on_send=False)
        if e.name == 'f2' and keyboard.is_pressed('ctrl'):
            text_to_type = chatgptHandler.rocketleague_phrase()
            rocketleague_type_text(text_to_type, open_chat_key='t', input_limit=120, chat_closes_on_send=False)

        if e.name == 'f3' and keyboard.is_pressed('ctrl'):
            text_to_type = chatgptHandler.rocketleague_scored_against()
            rocketleague_type_text(text_to_type, open_chat_key='t', input_limit=120, chat_closes_on_send=False)

        if e.name == 'f4' and keyboard.is_pressed('ctrl'):
            text_to_type = chatgptHandler.rocketleague_scored()
            rocketleague_type_text(text_to_type, open_chat_key='t', input_limit=120, chat_closes_on_send=False)

        if e.name == 'f5' and keyboard.is_pressed('ctrl'):
            text_to_type = chatgptHandler.funfact_phrase()
            rocketleague_type_text(text_to_type, open_chat_key='enter', chat_closes_on_send=True)

        if e.name == 'f6' and keyboard.is_pressed('ctrl'):
            text_to_type = chatgptHandler.cs2_sean_excuse()
            cs_type_text(text_to_type, open_chat_key='y', input_limit=110, chat_closes_on_send=False)

        if e.name == 'f7' and keyboard.is_pressed('ctrl'):
            text_to_type = chatgptHandler.cs2_survived_excuse()
            cs_type_text(text_to_type, open_chat_key='y', input_limit=110, chat_closes_on_send=False)

        if e.name == 'f8' and keyboard.is_pressed('ctrl'):
            text_to_type = chatgptHandler.cs2_died_excuse()
            cs_type_text(text_to_type, open_chat_key='y', input_limit=110, chat_closes_on_send=False)

        if e.name == 'f9' and keyboard.is_pressed('ctrl'):
            text_to_type = chatgptHandler.pause_phrase()
            cs_type_text(text_to_type, open_chat_key='y', input_limit=110, chat_closes_on_send=True)

        if e.name == 'f10' and keyboard.is_pressed('ctrl'):
            text_to_type = chatgptHandler.wife_message()
            cs_type_text(text_to_type, open_chat_key='y', input_limit=500, chat_closes_on_send=True)

        if e.name == 'f12' and keyboard.is_pressed('ctrl'):
            chatgptHandler.refresh_client()


chatgptHandler = ChatgptHandler()
# Hook for the key event
keyboard.hook(on_key_event)
# Keep the script running
keyboard.wait('end')  # You can change 'esc' to the key you want to use to exit the script