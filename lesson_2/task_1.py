user_input = int(input("Enter seconds: "))
hour = user_input // 3600
minute = user_input // 60 % 60
seconds = user_input % 60
print(f'{hour:02d}:{minute:02d}:{seconds:02d}')