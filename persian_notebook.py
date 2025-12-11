import sys
name = input('لطفاً اسم زیباتون رو وارد کنید\n')
print(f'سلام {name} عزیز، به دفترچه ی خاطرات خودتون خوشآمدید')
list_for_good_and_bad = []
list_for_memories = []
number_that_user_should_input = int(input('لطفاً تعداد خاطراتی که در این لحظه میخواید وارد کنید رو بنویسید\n'))
for my in range(number_that_user_should_input):
    memory = input('لطفاً خاطره ی خودتون رو وارد کنید\n')
    list_for_memories.append(memory)
len1 = len(list_for_memories)
print(f'{name} عزیز، تعداد خاطراتی که امروز وارد کردید {len1} و خاطراتی که وارد کردید {list_for_memories} هست، امیدوارم از این سبک نمایش خوشت بیاد')
print(f'{name} عزیز حالا با توجه به این خاطرات، میخوام که خوب و بد بودنشونم مشخص کنی، یا اگه میخوای تغییرشون بدی، اگه خوب و بد بودنش رو مشخص کنی، اینها جلوی خاطره نمایش داده میشه، اما اگه بخوایی تغییر بدی یکی از خاطره هات رو، لیست جدیدی از خاطراتت رو میبینی، واژه هایی که میتونی وارد کنی، تغییرش میدم، خوب یا بد بودن رو مشخص میکنم، اگه که حتی یک کلمه تغییر، یا خوب و بد رو هم وارد کنی اشکالی نداره')
user_input = input('حالا توی این ادیت باکس چیزهایی که میخوای رو وارد کن، خوب یا بد بودن خاطرات، یا تغییر دادن خاطرات')
if 'تغییر' in user_input:
    change1 = int(input('لطفاً شماره ی خاطره ای که میخوای تغییرش بدی رو وارد کن\n'))
    if change1 >= len(list_for_memories):
        print('شماره ی خاطره توی این لیست نیست')
        pass
        sys.exit()
    change2 = input('لطفاً خاطره ی جدید رو وارد کن\n')
    list_for_memories[change1] = change2
    print(list_for_memories)
elif 'خوب یا بد' in user_input or 'خوب' in user_input or 'بد' in user_input:
    for few in range(number_that_user_should_input):
        user_input1 = input('خوب بودن یا نبودن خاطره رو مشخص کن\n')
        list_for_good_and_bad.append(user_input1)
    for few2 in range(len(list_for_memories)):
        print(f'خاطره ی {few2} {list_for_memories[few2]} هست که به نظر تو خاطره {list_for_good_and_bad[few2]} بوده')