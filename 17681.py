def solution(n, arr1, arr2):
    arr3 = [0] * n
    for i in range(n):
        num = arr1[i] | arr2[i]
        s = ''
        for _ in range(n):
            s += '#' if num%2 else ' '
            num //= 2
        arr3[i] = s[::-1]

    return arr3


# another solution
def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
        # a12 부분만 한 줄 코드로 바꾸면 이렇게 됨.
        #a12 = str(bin(i|j)[2:]).rjust(n,'0').replace('1','#').replace('0',' ')


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]) 
                == ["#####", "# # #", "### #", "#  ##", "#####"])
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]) 
                == ["######", "###  #", "##  ##", " #### ", " #####", "### # "])
