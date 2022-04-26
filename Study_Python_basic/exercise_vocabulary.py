with open('vocabulary.txt', 'a') as f:
    eng_input = ""
    kor_input = ""

    while True:
        eng_input = input("영어 단어를 입력하세요: ")
        if eng_input == 'q':
            break;
        kor_input = input("한국어 뜻을 입력하세요: ")
        if kor_input == 'q':
            break;

        f.write('{}: {}\n'.format(eng_input, kor_input))
