import sys
name = input('Please enter your beautiful name\n')
print(f'Hello dear {name}, welcome to your memories notebook')
list_for_good_and_bad = []
list_for_memories = []
number_that_user_should_input = int(input('Please write the number of memories you want to enter now\n'))
for my in range(number_that_user_should_input):
    memory = input('Please enter your memory\n')
    list_for_memories.append(memory)
len1 = len(list_for_memories)
print(f'Dear {name}, the number of memories you entered today is {len1} and the memories you entered are {list_for_memories}, I hope you like this display style')
print(f'Dear {name} now based on these memories, I want you to specify if they are good or bad, or if you want to change them, if you specify good or bad, they will be displayed next to the memory, but if you want to change one of your memories, you will see a new list of your memories, the words you can enter, change, specify good or bad, even if you enter one word change or good and bad, it\'s fine')
user_input = input('Now in this edit box, enter what you want, good or bad of memories, or changing memories')
if 'change' in user_input:
    change1 = int(input('Please enter the number of the memory you want to change\n'))
    if change1 >= len(list_for_memories):
        print('The memory number is not in this list')
        pass
        sys.exit()
    change2 = input('Please enter the new memory\n')
    list_for_memories[change1] = change2
    print(list_for_memories)
elif 'good or bad' in user_input or 'good' in user_input or 'bad' in user_input:
    for few in range(number_that_user_should_input):
        user_input1 = input('Specify if the memory is good or not\n')
        list_for_good_and_bad.append(user_input1)
    for few2 in range(len(list_for_memories)):
        print(f'Memory {few2} {list_for_memories[few2]} is which to you was {list_for_good_and_bad[few2]} memory')