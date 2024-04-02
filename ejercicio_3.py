if __name__ == "__main__":
    n = int(input("Ingrese un numero mayor o igual que 2:  "))
    if n%2==0:
        for nums in range (n, 1, -2):
            print (nums)
    else:
        for nums in range (n-1, 1, -2):
            print(nums)