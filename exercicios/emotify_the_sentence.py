def emotify(txt):
    if 'smile' in txt:
        txt = txt.replace('smile', )
    elif 'grin' in txt:
        txt = txt.replace('grin', ':)')
    elif 'sad' in txt:
        txt = txt.replace('sad', ':(')
    elif 'mad' in txt:
        txt = txt.replace('mad', ':P')
    return txt

txt = 'Make me sad'
print(emotify(txt))
