import sys
import getch

def secureInput(prompt=''):
  password = ''

  while True:
    secure_password = getch.getch()
    password += secure_password
    sys.stdout.write(prompt + ''.join(secure_password))
    print('*', flush=True)

    if secure_password == '\r':
      return ('\n' + password)


if __name__ == '__main__':
    username = str(input("Enter your username: "))
    password = str(secureInput("Enter your password: "))
    print(password)
