with open('rw.txt') as t:
    content = t.read().replace(' ','\n')
    print(content)
