with open('in.txt','r') as in_f, open('out.txt','w') as out_f:
    words = in_f.read().split(" ")
    if(len(words) == 0):
        # If there are no words in file, the max and min words are empty
        out_f.write("")
        out_f.write("")
    else:
        min_word = words[0]
        max_word = words[0]
        for word in words:
            if len(word) == 0:
                continue # Skip empty words
            if len(word) > len(max_word):
                max_word = word
            if len(word) < len(min_word):
                min_word = word
        out_f.write(max_word+'\n')
        out_f.write(min_word)
