#Author Ian Wright
#Email thewian27@gmail.com
#run this file to install

import sys

Instructions = '''
    
    setup.py install -> installs
    setup.py help    -> this help menu

'''
if len(sys.argv) > 1:
  cmd = sys.argv[1]
  if cmd.lower() != 'install':
    print(Instructions)
  elif cmd.lower() == 'help':
    print(Instructions)
  else:
    main()

def main():    
  file = "requirements"
  libs = []
  
  with open(file, 'r') as f:
    lines = f.readlines()
    
    for line in lines:
      cmd = f"pip install {line.replace('\n','')}"
      os.system(cmd)
      libs.append(line.replace('\n',''))
    
      if os.name == 'nt':
         os.system('cls')
      else:
        os.system('clear')
        print(f'[*] Installed {len(libs)} dependencies...')
  print('[*] Done installing InstagramSaver')
