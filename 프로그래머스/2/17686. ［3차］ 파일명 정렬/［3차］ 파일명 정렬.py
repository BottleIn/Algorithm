def solution(files):
    temp = []
    for i, file in enumerate(files):
        # 1. HEAD, NUMBER 분리
        head = ""
        number = ""
        
        # HEAD 찾기
        idx = 0
        while idx < len(file) and not file[idx].isdigit():
            head += file[idx]
            idx += 1
            
        # NUMBER 찾기 (최대 5자)
        while idx < len(file) and file[idx].isdigit() and len(number) < 5:
            number += file[idx]
            idx += 1
            
        temp.append((head.lower(), int(number), i))

    # 3. 정렬 (1순위: head, 2순위: number)
    temp.sort(key=lambda x: (x[0], x[1]))

    # 4. 정렬된 결과의 인덱스를 이용해 원본 파일명 반환
    return [files[x[2]] for x in temp]