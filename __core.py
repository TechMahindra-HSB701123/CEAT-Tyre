with open('poem.txt') as f:
    k=f.read()
with open('core.txt', 'w') as f:
    f.write(k)  