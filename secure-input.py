import getch

def secureInput(prompt='', mask=''):
  output = ''
  print(prompt, end='', flush=True)

  while True:
    keyboard_input = getch.getch()
    if keyboard_input == '\n':
      break

    print(mask, end='', flush=True)
    output += keyboard_input
  
  return ('\n' + output)


if __name__ == '__main__':
  username = str(input("Enter your username: "))
  password = str(secureInput("Enter your password: ", '*'))

  print(password)
