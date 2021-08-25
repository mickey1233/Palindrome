def isPalindrome(x):
    #return str(x) == str(x)[::-1]
    if str(x) == str(x)[::-1]:
        print(True)
    else:
        print(False)
    
def main():
    isPalindrome(-121)

if __name__ == '__main__':
    main()
 
