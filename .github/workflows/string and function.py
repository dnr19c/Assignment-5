def insert_middle(string, w):
     return string[:2] + w + string[2:]

     print(insert_middle('[[]]', 'hello world'))
     print(insert_middle('{{}}', 'Hii how are you'))
     print(insert_middle('<<>>', 'HTML'))
