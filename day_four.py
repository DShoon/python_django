import os
import requests
def program():
  def input_url():
    input_x = input()
    input_x = input_x.lower()
    input_x = input_x.split(",")
    for i in range(len(input_x)):
      input_x[i] = input_x[i].strip()
      if "." in input_x[i]:
        continue
      else:
        print(input_x[i], "is not a valid URL")
        del input_x[i]

    return input_x

  def check_http(url):
    for idx, item  in enumerate(url):
      if "http://" in item:
        continue
      else:
         url[idx] = "http://"+url[idx]

    return url

  def IsItDown(url):
    try:
       for i in url:
         r = requests.head(i)
         if r.status_code < 400:
              print(i, "is up!")
              
         else:
              print(i, "is down!")
              

    except Exception:
       print(i, "is down!")
       return False

  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")
  clear = lambda: os.system('clear')
  IsItDown(check_http(input_url()))

  while True:

   print("Do you want to start over? y/n")
   ans = input()
   if ans == "y":
     clear()
     print("Welcome to IsItDown.py!")
     print("Please write a URL or URLs you want to check. (separated by comma)")
     IsItDown(check_http(input_url()))
   elif ans == "n":
     print("ok, bye!")
     break
   else:
     print("That is not valid answer")

program()