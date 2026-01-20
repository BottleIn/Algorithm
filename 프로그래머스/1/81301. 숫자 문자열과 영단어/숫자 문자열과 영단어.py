def solution(s):
    answer = ''
    eng_num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    find_word= ''
    
    for x in s:
        print(find_word)
        test_len = len(find_word)
        
        if test_len >= 3:
            for idx, num in enumerate(eng_num):
                if find_word == num:
                    answer += str(idx)
                    find_word = ''
                    break
        
        
        if test_len == 0 and x.isdigit(): #숫자로만 가져왔을 경우
            answer += x
            
            
        elif test_len != 0 and x.isdigit(): #검사 도중 숫자를 만난 경우
            for idx, num in enumerate(eng_num):
                if find_word == num:
                    answer += str(idx)
                    find_word = ''
                    break
            answer += x
        elif x.isalpha(): # 단어를 만난 경우
            find_word += x
    print('----')
    for idx, num in enumerate(eng_num):
        if find_word == num:
            answer += str(idx)
            find_word = ''
            break
    return int(answer)