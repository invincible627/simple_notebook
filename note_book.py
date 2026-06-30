import sys
language = input("Select language. Type pe or persian for Persian, and en or english for English\n")
if language.lower() == "en" or language.lower() == "english":
    name = input("Please enter your beautiful name\n")
    print(f"Hello dear {name}, welcome to your memories notebook")
    list_for_good_and_bad = []
    list_for_memories = []
    number_that_user_should_input = int(input("Please write the number of memories you want to enter now\n"))
    for my in range(number_that_user_should_input):
        memory = input("Please enter your memory\n")
        list_for_memories.append(memory)
    len1 = len(list_for_memories)
    print(f"Dear {name}, the number of memories you entered today is {len1} and the memories you entered are {list_for_memories}, I hope you like this display style")
    print(f"Dear {name} now based on these memories, I want you to specify if they are good or bad, or if you want to change them, if you specify good or bad, they will be displayed next to the memory, but if you want to change one of your memories, you will see a new list of your memories, the words you can enter, change, specify good or bad, even if you enter one word change or good and bad, it\"s fine")
    user_input = input("Now in this edit box, enter what you want, good or bad of memories, or changing memories")
    if "change" in user_input:
        change1 = int(input("Please enter the number of the memory you want to change\n"))
        if change1 >= len(list_for_memories):
            print("The memory number is not in this list")
            pass
            sys.exit()
        change2 = input("Please enter the new memory\n")
        list_for_memories[change1] = change2
        print(list_for_memories)
    elif "good or bad" in user_input or "good" in user_input or "bad" in user_input:
        for few in range(number_that_user_should_input):
            user_input1 = input("Specify if the memory is good or not\n")
            list_for_good_and_bad.append(user_input1)
        for few2 in range(len(list_for_memories)):
            print(f"Memory {few2} {list_for_memories[few2]} is which to you was {list_for_good_and_bad[few2]} memory")
elif language.lower() == "pe" or language.lower() == "persian":
    name = input("لطفاً اسم زیباتون رو وارد کنید\n")
    print(f"سلام {name} عزیز، به دفترچه ی خاطرات خودتون خوشآمدید")
    list_for_good_and_bad = []
    list_for_memories = []
    number_that_user_should_input = int(input("لطفاً تعداد خاطراتی که در این لحظه میخواید وارد کنید رو بنویسید\n"))
    for my in range(number_that_user_should_input):
        memory = input("لطفاً خاطره ی خودتون رو وارد کنید\n")
        list_for_memories.append(memory)
    len1 = len(list_for_memories)
    print(f"{name} عزیز، تعداد خاطراتی که امروز وارد کردید {len1} و خاطراتی که وارد کردید {list_for_memories} هست، امیدوارم از این سبک نمایش خوشت بیاد")
    print(f"{name} عزیز حالا با توجه به این خاطرات، میخوام که خوب و بد بودنشونم مشخص کنی، یا اگه میخوای تغییرشون بدی، اگه خوب و بد بودنش رو مشخص کنی، اینها جلوی خاطره نمایش داده میشه، اما اگه بخوایی تغییر بدی یکی از خاطره هات رو، لیست جدیدی از خاطراتت رو میبینی، واژه هایی که میتونی وارد کنی، تغییرش میدم، خوب یا بد بودن رو مشخص میکنم، اگه که حتی یک کلمه تغییر، یا خوب و بد رو هم وارد کنی اشکالی نداره")
    user_input = input("حالا توی این ادیت باکس چیزهایی که میخوای رو وارد کن، خوب یا بد بودن خاطرات، یا تغییر دادن خاطرات")
    if "تغییر" in user_input:
        change1 = int(input("لطفاً شماره ی خاطره ای که میخوای تغییرش بدی رو وارد کن\n"))
        if change1 >= len(list_for_memories):
            print("شماره ی خاطره توی این لیست نیست")
            pass
            sys.exit()
        change2 = input("لطفاً خاطره ی جدید رو وارد کن\n")
        list_for_memories[change1] = change2
        print(list_for_memories)
    elif "خوب یا بد" in user_input or "خوب" in user_input or "بد" in user_input:
        for few in range(number_that_user_should_input):
            user_input1 = input("خوب بودن یا نبودن خاطره رو مشخص کن\n")
            list_for_good_and_bad.append(user_input1)
        for few2 in range(len(list_for_memories)):
            print(f"خاطره ی {few2} {list_for_memories[few2]} هست که به نظر تو خاطره {list_for_good_and_bad[few2]} بوده")
else:
    print("invalid language, please restart program again")
    print("زبان وارد شده نادرست است. لطفاً برنامه را دوباره اجرا کنید")