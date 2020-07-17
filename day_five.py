import os
import requests
from bs4 import BeautifulSoup

def program():
  os.system("clear")
  url = "https://www.iban.com/currency-codes"


  def extract_data(url):
      result = requests.get(url)

      soup = BeautifulSoup(result.text,'html.parser')
      output_rows = []

      table = soup.find("table", {"class" : "table table-bordered downloads tablesorter"})  
      table_body = table.find('tbody')

      rows = table_body.find_all('tr')

      for row in rows:
        columns = row.find_all('td')
        output_row = []
        
        for column in columns:
            output_row.append(column.text)
        output_rows.append(output_row)
    
      no_currency_idx = []
      for row in range(len(output_rows)):
        if output_rows[row][1] == 'No universal currency':
          no_currency_idx.append(row)

      for index in no_currency_idx:
        del output_rows[index]

      return output_rows

  output_rows = extract_data(url)

  print("Hello! Please choose select a country by number:")
  for row in range(len(output_rows)):
     print("#", row, output_rows[row][0].capitalize())

  while True:
      try:
        input_number = int(input("#: "))
        if input_number not in range(len(output_rows)):
           print("Choose a number from the list.")
        else:
          print("You chose", output_rows[input_number][0].capitalize())
          print("The currency code is", output_rows[input_number][2].upper())
          break
            
      except:
              print("That wasn't a number.") 


program()