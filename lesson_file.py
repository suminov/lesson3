with open('referat.txt', 'r', encoding='utf-8') as myfile:
  content = myfile.read()
  print(len(content))
  print(len(set(content.split())))
  with open('referat2.txt', 'w', encoding='utf-8') as myfile2:
    myfile2.write(content.replace('.', '!'))