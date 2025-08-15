import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

# 🎨 رسم سبونج بوب
spongebob = r"""
      .--..--..--..--..--..--.
   .' \  (`._   (_)     _   \
 .'    |  '._)         (_)  |
 \ _.')\      .----..---.   |
 |(_.'  |     /    .-\-.  \  |
 \     0|    /    ( O| O) | |
  |  _  |  .-/     '-'   | |
  | (_) | .'|     ___|_  | |
  |     | |'.    [_____ ]| |
  | _   | | |    |     | | |
  |     | | |    |_____| | |
  |     | | |    |     | | |
  '-._  | | |    |     | | |
      `-.| |    |     | | |
         `-|    |     | | |
           |    |     | |
"""

# 🐢 دالة الكتابة البطيئة
def slow_print(text, delay=0.04, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# 📜 القصة
story = """
There was someone named rayanosamaahmad who loved SpongeBob so much.
But he had many questions hidden deep in his mind — questions that only the wisest could answer.
He decided to challenge you.
If you answer them correctly, he will give you pieces of a secret flag.
"""

# ❓ الأسئلة والإجابات
questions = [
    ("What is the word that Basit repeats in the song?", "Road"),
    ("When does the toy store open?", "10AM"),
    ("The name of the cafe where SpongeBob takes a selfie?", "Turkish coffee"),
    ("Name of the very first on-line editor credited in the Editorial Department?", "Dan Aguilar"),
    ("What is the second most reviewed work that Dan has participated in in the same field?", "8.8")
]

# 🏁 أجزاء الفلاج (Base64 جاهزة من عندك)
flag_parts = [
    "NGhhdHN7NXAwbkczXw==",
    "TDB2M3Nf",
    "UkB5NG5f",
    "YW5kXw==",
    "Il8wNSFudH0="
]

# 🚀 البداية
print(Fore.YELLOW + spongebob)
slow_print(story, delay=0.03, color=Fore.WHITE)
print(Fore.GREEN + "=" * 50)

# 🔄 حلقة الأسئلة
for i, (q, answer) in enumerate(questions):
    attempts = 3
    while attempts > 0:
        slow_print(f"Q{i+1}: {q}", color=Fore.CYAN)
        user_input = input(Fore.GREEN + "> " + Style.RESET_ALL).strip().lower()

        if user_input.strip().lower().replace(" ", "") == answer.strip().lower().replace(" ", ""):
            slow_print(f"✅ Correct! Here is {flag_parts[i]}", color=Fore.WHITE)
            print(Fore.GREEN + "-" * 50)
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(Fore.RED + f"❌ Wrong! Attempts left: {attempts}")
            else:
                print(Fore.RED + "💀 No attempts left for this question! Exiting...")
                sys.exit()

# 🎉 النهاية
slow_print("🎉 Congratulations! You have all parts of the flag", color=Fore.GREEN)
print(Fore.GREEN + "=" * 50)
