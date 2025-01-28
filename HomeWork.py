# Q1
def find_div(n):
    for i in range(1, n):
        if n % i == 0:
            print(i, end=" ")
    print()


find_div(20)


# Q2
def numbers():
    total, count = 0, 0

    while True:
        num = int(input(f"Please enter number #{count + 1}: "))

        if num < 0:
            print("Thank you, Goodbye.")
            break

        count += 1
        total += num
        avg = total / count

        print(f"Avg = {avg:.2f} sum = {total}")


numbers()


# Q3
def words():
    words_dic = {}

    while True:
        word = input("Please enter a word: ").lower()

        if word in words_dic:
            words_dic[word] += 1
        else:
            words_dic[word] = 1

        if words_dic[word] == 3:
            print("You entered the same word 3 times. Goodbye...")
            break


words()


# Q4
def compare(lis1, lis2):
    min_len = min(len(lis1), len(lis2))

    balance = 0

    for i in range(min_len):
        if lis1[i] > lis2[i]:
            balance += 1
        elif lis1[i] < lis2[i]:
            balance -= 1

    if balance > 0:
        print("List 1 is bigger")
    elif balance < 0:
        print("List 2 is bigger")
    else:
        print("Both lists are equal")


list1 = [3, 5, 30, 0]
list2 = [1000, 5, 29, -5]

compare(list1, list2)
