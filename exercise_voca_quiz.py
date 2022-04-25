with open('vocabulary.txt', 'r') as f:
    for line in f:
        split_line = line.strip().split(': ')
        eng_word = split_line[0]
        kor_word = split_line[1]

        answer = input("{}: ".format(kor_word))
        if eng_word == answer:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(eng_word))
