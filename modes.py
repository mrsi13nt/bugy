import time,sys,os,subprocess
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.08)

def clear():
  os.system("clear")

def report(answer):
  if answer == "y":
    file_paths = ['outputs/subdomains.txt', 'outputs/dir.txt', 'outputs/part3_output.txt', 'outputs/waybackurls.txt', 'outputs/gau.txt', 'outputs/katana.txt', 'outputs/hakrawler.txt']

    with open('outputs/report.txt', 'w', encoding='utf-8') as output_file:
      for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as input_file:
          for line in input_file:
            output_file.write(line)
            output_file.write('\n')
    clear()
    print(subprocess.run("cat outputs/report.txt",shell=True))

  elif answer == "n":
    typingPrint("don't forget to check outputs file\n")
    typingPrint("Bye. :)")
  else:
    print("error")