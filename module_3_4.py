def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    print(same_words)


result_1 = ['richiest', 'orichalcum', 'cheers', 'richies']
result_2 = ['Able', 'Mable', 'Disable', 'Bagel']
single_root_words('rich', *result_1)
single_root_words('Disablement', *result_2)


