from word import questions
import random

word = random.choice(list(questions))
question = questions[word]
zvezdochki = '*' * len(word)
 
zvezdochki = list(zvezdochki)  

print(question)

while ('*' in zvezdochki):
    print(''.join(zvezdochki))  
    user_answer = input('Введите букву/слово: ')
    if len(user_answer) == 1:
        if user_answer.upper() in word.upper():  
            print('Есть такая буква в этом слове!')
            i = 0
            for _ in range(len(word)):
                if(word[i].upper() == user_answer.upper()):
                    zvezdochki[i] = user_answer
                i+=1
        else:
            print('Такой буквы нет')
    else:
        if user_answer.upper() == word.upper():
            break
        else:
            print('Вы не отгадали слово')
print('Вы отгадали слово - ' + word)
