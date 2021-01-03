import sys

def input_numbers():
    list_N = []
    count = 1
    while len(list_N) < int(N):
        print("Enter the number {0}".format(count))
        list_N.append(int(input()))
        count = count + 1
        continue

    return list_N

def sum(list_N):
    sum = 0
    for i in range(len(list_N)):
        sum = sum + list_N[i] 

    return sum

def check(list_N, sum_old, K):
    operation = 1
    j = 0
    if sum_old % int(K) == 0:
        print("The sum is divisible by K, no need to change the list,  operation taken is {0}".format(0))
    else:
        while j <= 20:
            for i in range(len(list_N)):
                list_N[i] = list_N[i] + 1
                print("New list")
                print(list_N)
                sum_nw = sum(list_N)
                print('The new sum is {0}'.format(sum_nw))
                if sum_nw % int(K) == 0:
                    operation = operation + 1
                    print("The sum is divisible, Total count operations it took is {0}".format(operation))
                    break
                else:
                    if i == len(list_N) - 1:
                        print("Limit of the list reached.")
                        j = j + 1 
                        continue

def main(N, K):
    '''Main function.'''
    list_N = input_numbers()
    print("The integer in the list are {0}".format(list_N))
    sum_n = sum(list_N)
    print("Sum of the function is {0}".format(sum_n))

    check(list_N, sum_n, K)
    return None

if __name__ == "__main__":
    print("Enter the number total values to be entered.")
    N  = input()
    print("Enter the value of K.")
    K = input()
    main(N, K)