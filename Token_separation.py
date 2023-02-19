# -*- coding: utf-8 -*-

X = input("enter the syntax : ").split(" ")
keywords = []
identifiers = []
operators = []
punctuations = []
numbers = [] 
punctuation = [',',';','"',"'",'.',':']
for i in X:
  if i in "intifelsewhiledoforlongcontinuereturn":
    print('< keyword,',i,'>')
    if i not in keywords:
      keywords.append(i) 
  elif i in "+-*/><=%":
    print('< operators,',i,'>')
    if i not in operators:
      operators.append(i)
  elif i.isnumeric():
    print('< numbers,',i,'>')
    if i not in numbers:
      numbers.append(i)    
  elif i in ":''.,;":
    print('< punctuations,',i,'>')
    if i not in punctuations:
      punctuations.append(i)
  else:
    if i not in identifiers:
      identifiers.append(i)
    print('< id'+str(identifiers.index(i)+1)+', ',i,'>')

