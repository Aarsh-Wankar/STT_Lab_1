def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1 

    return fibonacci(n-1) + fibonacci(n-2) #fixed infinite recursion

# def gibberish(n):
#     vector<int> h(n);           #C++!!!!????
#     for(int i = 0; i<n; i++){
#         h[i] = i;
#     }
#     return h;

def main():
    n = int(input("Enter a number: "))
    return fibonacci(n)

if __name__ == "main":
    main()
    # gibberish(10)