
def add_to_dict(obj, key=None, value=None):
  if type(obj) is not dict: 
    print("You need to send a dictionary. You sent:", type(obj))
  elif value==None or key==None:
    print("You need to send a word and a definition.")
  elif key in obj:
    print(key, "is already on the dictionary. Won't add.")
  else:
    obj[key] = value
    print(key, "has been added.") 
  pass

def get_from_dict(obj, key=None):
    if type(obj) is not dict: 
      print("You need to send a dictionary. You sent:", type(obj))
    elif key==None:
      print("You need to send a word to search for.")
    elif obj.get(key) is None:
      print(key, "was not found in this dict")
    else:
      print(key, ":" , obj[key])
    pass

def update_word(obj, key=None, value=None):
    if type(obj) is not dict: 
      print("You need to send a dictionary. You sent:", type(obj))
    elif value==None or key==None:
      print("You need to send a word and a definition to update.")
    elif obj.get(key) is None:
      print(key, "is not on the dict. Can't update non-existing word.")
    else:
      obj.update(key=value)
      print(key, "has been updated to:", value)
    pass

def delete_from_dict(obj, key=None):
    if type(obj) is not dict: 
      print("You need to send a dictionary. You sent:", type(obj))
    elif key==None:
      print("You need to specify a word to delete.")
    elif obj.get(key) is None:
      print(key, "is not in this dict. Won't delete.")
    else:
      del obj[key]
      print(key, "has been deleted.") 
    pass


import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")


print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")
