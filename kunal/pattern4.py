def pattern(no_of_rows):
    for i in range(no_of_rows+1):
        for j in range(1,i+1):
            if j!=i:
                print(str(j),end=" ")
            else:
                print(str(j))


n=int(input())
pattern(n)
