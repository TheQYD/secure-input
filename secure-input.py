import getch
import keyboard

def secureInput(prompt='', mask=''):
  output = ''
  #print(prompt, end='', flush=True)

  while True:

    print('\r' + prompt, end='', flush=True)
    keyboard_input = getch.getch()
    
    if keyboard_input == '\n':
      break
    
    elif keyboard_input == '2':
      output = output[:-1]
    
    else:
      output += keyboard_input
    

    #print(mask, end='', flush=True)
    #output += keyboard_input
  return ('\n' + output)


if __name__ == '__main__':
  username = str(input("Enter your username: "))
  password = str(secureInput("Enter your password: ", '*'))

  print('\n' + password)
