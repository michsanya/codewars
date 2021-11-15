def title_case(title, minor_words=''):
    title_dif = title.split(' ')
    minor_words_dif = minor_words.split(' ')
    n = 0
    for i in title_dif:
        title_dif[n] = title_dif[n].capitalize()
        for j in minor_words_dif:
            if i.lower() == j.lower():
                title_dif[n] = title_dif[n].lower()
        n = n+1
    title_dif[0] = title_dif[0].capitalize()
    return ' '.join(title_dif)




print(title_case('THE WIND IN THE WILLOWS', 'The in a'))
