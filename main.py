print("Правильно!")
  score = score + 1
else:
  print("Неправильно.")

print(questions[5])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[5].lower():
  print("Правильно!")
  score = score + 1
else:
  print("Неправильно.")

print(questions[6])
user_answer = input("Введи свой ответ: ")
if user_answer.lower() == answers[6].lower():
  print("Правильно!")
  score = score + 1
else:
  print("Неправильно.")


# Допиши код вместо "..."
if score>5:
  print("Это отличный результат! Ты много знаешь о стартапах.")
elif score>3:
  print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о стартапах.")
else:
  print("Видимо, ты только начинаешь свой путь к стартапам! Ты ещё много чего узнаешь о мире, где мы живём.")