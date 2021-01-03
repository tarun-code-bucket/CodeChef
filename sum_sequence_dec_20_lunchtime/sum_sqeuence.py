'''This script takes input as the following parameter:
N : Total number of numbers in a list.
K : The number which has to be used a divisor.
limit : The limit of the while loop to run.

Description : Take the N as the input of the list, limit of the while loop and K as the divisor.
Call the sum function and check the divisibility by K if not increment the value of i in for loop by 1.
If the value of j is less than the limit ,then continue the while loop to check the divisibility. 
'''
def input_numbers():
    "Get the numbers."
    list_N = []
    count = 1
    while len(list_N) < int(N):
        print("Enter the number {0}".format(count))
        list_N.append(int(input()))
        count = count + 1
        continue

    return list_N

def sum(list_N):
    "Get the sum."
    sum = 0
    for i in range(len(list_N)):
        sum = sum + list_N[i] 

    return sum

def check(list_N, sum_old, K, limit):
    "Check the numbers in th elist if it is divisible by K and limit is less than loop."
    operation = 1
    j = 0
    if sum_old % int(K) == 0:
        print("The sum is divisible by K, no need to change the list,  operation taken is {0}".format(0))
    else:
        while j <= limit:
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

def main(N, K, limit):
    "Main function."
    list_N = input_numbers()
    print("The integer in the list are {0}".format(list_N))
    sum_n = sum(list_N)
    print("Sum of the function is {0}".format(sum_n))
    check(list_N, sum_n, K, limit)
    return None

if __name__ == "__main__":
    "Main entry point, which calls the main function."
    print("Enter the number total values to be entered.")
    N  = input()
    print("Enter the limit of the loop.")
    limit = input()
    print("Enter the value of Divisor (K).")
    K = input()
    main(N, K, limit)