import datetime
from abc import ABC
import random


class AbstAddUser(ABC):
    @staticmethod
    def data_user():
        pass

class AddLogin(AbstAddUser):
    def __get__(self, instance, owner):
        return instance.__dict__.get("login", "not found")

    def __set__(self, instance, value):
        if not isinstance(value, str):
            print("Логін має бути строкою!")
        elif len(value) > 10 or len(value) < 2:
            print("Логін має бути від 2 до 10 символів!")
        else:
            instance.__dict__["login"] = value

    def data_user(self):
        pass

class AddPassword(AbstAddUser):
    def __get__(self, instance, owner):
        return instance.__dict__.get("password", "not found")

    def __set__(self, instance, value):
        if not isinstance(value, str):
            print("Пароль має бути строкою!")
        elif len(value) > 10 or len(value) < 2:
            print("Пароль має бути від 2 до 10 символів!")
        else:
            instance.__dict__["password"] = value

    def data_user(self):
        pass

class AddDateHB(AbstAddUser):
    def __get__(self, instance, owner):
        return instance.__dict__.get("date_hb", "not found")

    def __set__(self, instance, value):
        if not isinstance(value, datetime.date):
            print("Вкажіть корректно дату!")
        else:
            instance.__dict__["date_hb"] = value

    def data_user(self):
        pass

class AddStatus(AbstAddUser):
    def __get__(self, instance, owner):
        return instance.__dict__.get("status", "not found")

    def __set__(self, instance, value):
        if value == "user" or value == "admin":
            instance.__dict__["status"] = value
        else:
            print("Вкажіть корректно дату!")

    def data_user(self):
        pass


class AddUser:
    login = AddLogin()
    password = AddPassword()
    date_hn = AddDateHB()
    status = AddStatus()

    def __init__(self, login, password, date_hn, status):
        self.login = login
        self.password = password
        self.date_hn = date_hn
        self.status = status

    def add_users(self, ls):
        ls.append({
            "login":self.login,
            "password":self.password,
            "date_hn":self.date_hn,
            "status":self.status
        })

class User:
    def __init__(self, login=None):
        self.login = login
        self.users = []

    def data_user(self):
        login = str.lower(input("Введіть логін нового користувача: "))
        for user in self.users:
            if user.get('name') == login:
                print("Існуючий логін! Помилка")
                raise NameError
        password = input("Введіть пароль нового користувача(5-10 символів): ")
        data_hb = input("Введіть дату народження в форматі: ")
        status = input("Введіть статус користувача (admin або user): ")
        new_user = AddUser(login, password, data_hb, status)
        new_user.add_users(self.users)


    def edit(self):
        print("Що саме ви хочете відрагувати:"
              "\n1. Пароль, \n2. Дату народження \n")
        choice = ("Введіть ваш вибір: ")
        if choice == '1':
            new_password = input("Введіть новий пароль! ")
            for j in range(len(self.users)):
                if self.users[j]["login"] == self.login:
                    self.users[j]["password"] = new_password
                else:
                    print("Ви не ввійшли в аккаунт. Користувача не знайдено!")
        elif choice == '2':
            new_date = input("Введіть нову дату народження: ")
            if isinstance(new_date, datetime.date):
                for j in range(len(self.users)):
                    if self.users[j]["login"] == self.login:
                        self.users[j]['date_hn'] = new_date
                    else:
                        print("Ви не ввійшли в аккаунт. Користувача не знайдено!")
            else:
                print("Введіть корректну дату!")

    def entrace(self):
        login = input("Введіть ваш логін: ")
        for i in range(len(self.users)):
            if self.users[i]['login'] == login:
                password = input("Введіть пароль: ")
                if self.users[i]["password"] == password:
                    print("Вітаємо вас в системі!")
                    self.login = login
                else:
                    print("Невірний пароль!")
            else:
                print("Користувача не знайдено!")





class AbstQyestion(ABC):
    @staticmethod
    def question():
        pass

    # @staticmethod
    # def answer():
    #     pass


class QuestionHistory(AbstQyestion):
    def __init__(self):
        self.questions_his = []
    def question(self):
        self.questions_his = [ #key:value
            {'ques':'Коли почалася перша світова війна?', 'answer':"1914"},
            {'ques':'Яка найдавніша цивілізація у світі? ', 'answer': "Месопотамія"},
            {'ques':'Хто був із відомих римських поетів?', 'answer': "Вергілій"},
            {'ques':'Під час якої події Корея була розділена на 2 країни?', 'answer': "Друга світова"},
            {'ques':'Як ще називають Велику піраміду в Єгипті? ', 'answer': "Гіза, Хуфу"},
            {'ques':'В якому місті народився Юлій Цезар?', 'answer': "Рим"},
            {'ques':'Яка країна Азії була учасником Осі у Другій світовій війні? ', 'answer': "Японія"},
            {'ques':'Яка перша назва НАТО перед її теперішньою назвою?', 'answer': "Північноатлантичний договір"},
            {'ques':'Хто також відомий як засновник наукового соціалізму?', 'answer': "Карл Маркс"},
            {'ques':'Де востаннє зупинявся Олександр Єрсін перед смертю?', 'answer': "В'єтнам"},
            {'ques':'Коли стався Голокост, одна з найстрашніших подій в історії?', 'answer': "Під час Другої світової війни"},
            {'ques':'Кого назвали на честь убивства Авраама Лінкольна?', 'answer': "Ендрю Джонсон"},
            {'ques':'Яка країна входила до півострова Індокитай під час французької колонізації?', 'answer': "В'єтнам, Лаос, Камбоджа"},
            {'ques':'Кого називають Наполеоном Іранським? ', 'answer': "Надер Шах"},
            {'ques':'Хто є першим президентом США?', 'answer': "Вашингтон "},
            {'ques':'якому році було вбито Джона Ф. Кеннеді?', 'answer': "1963"},
            {'ques':'Чий період був відомий як Золотий вік Риму?', 'answer': "Август Цезар"},
            {'ques':'Хто є найдавнішими предками корінних американців?', 'answer': "палеоіндійці"},
            {'ques':'Хто був першою людиною, яка ступила на Місяць', 'answer': "Ніл Армстронг"},
            {'ques':'Яка технологія вважається першою людською?', 'answer': "Вогонь"},
            {'ques':'Хто є винахідником електричного світла?', 'answer': "Едісон"},
        ]
        return self.questions_his

class QuestionBiolog(AbstQyestion):
    def __init__(self):
        self.questions_bio = []
    def question(self):
        self.questions_bio = [
            {'ques':"Які істоти мають три серця?", 'answer': "восьминоги, каракатиці, кальмари"},
            {'ques':"Що означає поняття “ікебана”?", 'answer': "живі квіти"},
            {'ques':"Яка рослина дає кращий мед?", 'answer': "липа"},
            {'ques':"Яка найбільший літаючий птах?", 'answer': "дрохва, корі"},
            {'ques':"Який найменша птах?", 'answer': "колібрі"},
            {'ques':"Який птах іноді кричить як кішка?", 'answer': "Іволга"},
            {'ques':"Яка найменша м’ясоїдна тварина суші?", 'answer': "горностай"},
            {'ques':"Чи косий заєць?", 'answer': "ні"},
            {'ques':"Яка змія плюється?", 'answer': "кобра"},
            {'ques':"У кого найбільший язик?", 'answer': "мурахоїд"},
            {'ques':"Які ноги жирафа довші?", 'answer': "передні"},
            {'ques':"Яка рослина має назву очі птиці?", 'answer': "вороняче око"},
            {'ques':"Який звір після їжі чистить зуби?", 'answer': "Тигр"},
            {'ques':"Чи зростає дерево взимку?", 'answer': "ні"},
            {'ques':"Яка риба за зовнішнім виглядом нагадує шахову фігуру? ", 'answer': "морський коник"},
            {'ques':"Пташенята, якої птиці в гнізді шиплять, як змії? ", 'answer': "вертишейки"},
            {'ques':"Який птах зовсім не має крил?", 'answer': "ківі"},
            {'ques':"Яка квітка розкривається тільки вночі і ароматно пахне?", 'answer': "тютюн"},
            {'ques':"Найбільший павук у світі? ", 'answer': "Павук-птахоїд"},
            {'ques':"Найбільша змія на землі", 'answer': "анаконда"},
        ]
        return self.questions_bio

class QuestionGeography(AbstQyestion):
    def __init__(self):
        self.questions_geo =[]

    def question(self):
        self.questions_geo = [
            {'ques':"Як називається стародавня цитадель в Афінах", 'answer':"Акрополь"},
            {'ques':"Де знаходиться замок Нойшванштайн?", 'answer': "Німеччина"},
            {'ques':"Який найвищий водоспад у світі?", 'answer': "Анхель "},
            {'ques':"Як називається палац у Великобританії, який вважається постійним будинком королеви?", 'answer': "Букінгемський палац"},
            {'ques':"У якому місті розташований Ангкор-Ват?", 'answer': "Сиемреап"},
            {'ques':" Яка пам'ятка США знаходиться в Нью-Йорку, але не була виготовлена в США?", 'answer': "Статуя Свободи"},
            {'ques':"Яка будівля є найвищою у світі?", 'answer': "Бурдж -Халіфа"},
            {'ques':"Нотр-Дам – це відомий собор Парижа?", 'answer': "так"},
            {'ques':"Яка відома пам’ятка Великобританії? ", 'answer': "Біг Бен"},
            {'ques':"Назви країну-банкіра всієї планети", 'answer': "Швейцарія"},
            {'ques':"Чи знаєш Ти, яка держава найбільша у Південній Америці?", 'answer': "Бразилія"},
            {'ques':"Назви батьківщину Олімпійських ігор та марафонського бігу", 'answer': "Греція"},
            {'ques':"В якій африканській країні найбільша чисельність населення?", 'answer': "Нігерія"},
            {'ques':"Яку корисну функцію виконує Статуя Свободи у США?", 'answer': "маяк"},
            {'ques':"Звідки пішло слово «газета»?", 'answer': "італія"},
            {'ques':"Найвища народжуваність, стверджує Книга рекордів Гіннеса, спостерігалась у Кенії в 1980-х роках. А в якій країні найнижча народжуваність?", 'answer': "Ватикан"},
            {'ques':"У якій країні можна купити слона за найдешевшу ціну?", 'answer': "Зімбабве"},
            {'ques':"Земля оливкової олії?", 'answer': "Ізраїль"},
            {'ques':"У якій країні прийнято подавати на стіл живу рибу, яка плескає хвостом?", 'answer': "Лаос"},
            {'ques':"В якій країні жінки носять сарі?", 'answer': "Індія"},
        ]
        return self.questions_geo


class AbstAddQuestion(ABC):
    @staticmethod
    def status():
        pass

    @staticmethod
    def add_question():
        pass



class AddQuestion(AbstAddQuestion):
    user = User()
    def status(self):
        self.user.entrace()
        if self.user.login:
            for j in range(len(self.user.users)):
                if self.user.users[j]['status'] == 'admin':
                    return True
                else:
                    print("Ваш статус не дозволяє додавання питання!")
        else:
            print("Ви не авторизовані в системі!")
        return False

    def add_question(self):
        if self.status():
            print("Виберіть категорію питаня: \n1. Історія \n2. Біологія \n3. Географія")
            choice = input("Введіть ваш вибір: ")
            if choice == '1':
                x = QuestionHistory()
                x.questions_his.append({
                    'ques': input("Введіть запитання: "),
                    'answer': input("Введіть відповідть: ")
                })
            elif choice == '2':
                x = QuestionBiolog()
                x.questions_bio.append({
                    'ques':input("Введіть запитання: "),
                    'answer':input("Введіть відповідть: ")
                })
            elif choice == '3':
                x = QuestionGeography()
                x.questions_geo.append({
                    'ques': input("Введіть запитання: "),
                    'answer': input("Введіть відповідть: ")
                })
            else:
                print("Введіть корректний вибір!")


class AbstEditQuedtion(ABC):
    @staticmethod
    def status():
        pass

    @staticmethod
    def edit():
        pass


class EditQuestion(AbstEditQuedtion):
    user = User()
    def status(self):
        self.user.entrace()
        if self.user.login:
            for j in range(len(self.user.users)):
                if self.user.users[j]['status'] == 'admin':
                    return True
                else:
                    print("Ваш статус не дозволяє додавання питання!")
        else:
            print("Ви не авторизовані в системі!")
        return False

    def edit(self):
        if self.status():
            print("Виберіть категорію питаня: \n1. Історія \n2. Біологія \n3. Географія")
            choice = input("Введіть ваш вибір: ")
            if choice == '1':
                x = QuestionHistory()
                z = input("Введіть питання яке хочете змінити: ")
                for j in range(len(x.questions_his)):
                    if str.lower(x.questions_his[j]['ques']) == str.lower(z):
                        new_ques = input("Введіть нове питання: ")
                        new_answer = input("Введіть відповіь: ")
                        x.questions_his[j]['ques'] = new_ques
                        x.questions_his[j]['anwer'] = new_answer
                    else:
                        print("Питання не знайдено! ")
            elif choice == '2':
                x = QuestionBiolog()
                z = input("Введіть питання яке хочете змінити: ")
                for j in range(len(x.questions_bio)):
                    if str.lower(x.questions_bio[j]['ques']) == str.lower(z):
                        new_ques = input("Введіть нове питання: ")
                        new_answer = input("Введіть відповіь: ")
                        x.questions_bio[j]['ques'] = new_ques
                        x.questions_bio[j]['anwer'] = new_answer
                    else:
                        print("Питання не знайдено! ")
            elif choice == '3':
                x = QuestionGeography()
                z = input("Введіть питання яке хочете змінити: ")
                for j in range(len(x.questions_geo)):
                    if str.lower(x.questions_geo[j]['ques']) == str.lower(z):
                        new_ques = input("Введіть нове питання: ")
                        new_answer = input("Введіть відповіь: ")
                        x.questions_geo[j]['ques'] = new_ques
                        x.questions_geo[j]['anwer'] = new_answer
                    else:
                        print("Питання не знайдено! ")
            else:
                print("Введіть корректне значення!")


class AbstTop(ABC):
    @staticmethod
    def add_top():
        pass

    @staticmethod
    def top():
        pass

class TopQuizHistory(AbstTop):
    def __init__(self):
        self.top_history = []

    def add_top(self, score, login):
        self.top_history.append({'score':score, 'name':login})
        return

    def top(self):
        for i in range(len(self.top_history)-1):
            for j in range(len(self.top_history)-1):
                if self.top_history[j]['score'] > self.top_history[j+1]['score']:
                    temp = self.top_history[j]
                    self.top_history[j] = self.top_history[j+1]
                    self.top_history[j+1] = temp
        return self.top_history

    def show(self):
        self.top()
        for i in range(len(self.top_history)):
            print(*self.top_history[i])

class TopQuizBiolog(AbstTop):
    def __init__(self):
        self.top_biolog = []

    def add_top(self, score, login):
        self.top_biolog.append({'score':score, 'name':login})
        return

    def top(self):
        for i in range(len(self.top_biolog)-1):
            for j in range(len(self.top_biolog)-1):
                if self.top_biolog[j]['score'] > self.top_biolog[j+1]['score']:
                    temp = self.top_biolog[j]
                    self.top_biolog[j] = self.top_biolog[j+1]
                    self.top_biolog[j+1] = temp
        return self.top_biolog

    def show(self):
        self.top()
        for i in range(len(self.top_biolog)):
            print(*self.top_biolog[i])

class TopQuizGeography(AbstTop):
    def __init__(self):
        self.top_georg = []

    def add_top(self, score, login):
        self.top_georg.append({'score':score, 'name':login})
        return

    def top(self):
        for i in range(len(self.top_georg)-1):
            for j in range(len(self.top_georg)-1):
                if self.top_georg[j]['score'] > self.top_georg[j+1]['score']:
                    temp = self.top_georg[j]
                    self.top_georg[j] = self.top_georg[j+1]
                    self.top_georg[j+1] = temp
        return self.top_georg

    def show(self):
        self.top()
        for i in range(len(self.top_georg)):
            print(*self.top_georg[i])

class TopQuizMixed(AbstTop):
    def __init__(self):
        self.top_mix = []

    def add_top(self, score, login):
        self.top_mix.append({'score':score, 'name':login})
        return

    def top(self):
        for i in range(len(self.top_mix)-1):
            for j in range(len(self.top_mix)-1):
                if self.top_mix[j]['score'] > self.top_mix[j+1]['score']:
                    temp = self.top_mix[j]
                    self.top_mix[j] = self.top_mix[j+1]
                    self.top_mix[j+1] = temp
        return self.top_mix

    def show(self):
        self.top()
        for i in range(len(self.top_mix)):
            print(*self.top_mix[i])



class AbstQuiz(ABC):
    @staticmethod
    def ques():
        pass

    @staticmethod
    def scores():
        pass

class Quiz(AbstQuiz):
    user = User()
    def __init__(self):
        self.score = 0

    def ques(self):
        login = self.user.login
        choice = input("Виберіть категорію: \n1. Історія \n2. Біологія \n3. Георграфія \n4. Змішана\n")
        if choice == '1':
            x = QuestionHistory()
            x.question()
            top = TopQuizHistory()
            for i in range(len(x.questions_his)):
                print(x.questions_his[i]['ques'])
                answer = str.lower(input("Введіть відповідь: "))
                if x.questions_his[i]['answer'] == answer:
                    self.score += 1
                    print("Правильна відповідь! +1 бал")
                else:
                    print("Відповідь неправильна")
                if i == 20:
                    print(f"Кінець вікторини! Ви заробили: {self.score} балів")
                    break
            top.add_top(self.score, login)
            return self.score
        elif choice == '2':
            x = QuestionBiolog()
            x.question()
            top = TopQuizBiolog()
            for i in range(len(x.questions_bio)):
                print(x.questions_bio[i]['ques'])
                answer = str.lower(input("Введіть відповідь: "))
                if x.questions_bio[i]['answer'] == answer:
                    self.score += 1
                    print("Правильна відповідь! +1 бал")
                else:
                    print("Відповідь неправильна")
                if i == 20:
                    print(f"Кінець вікторини! Ви заробили: {self.score} балів")
                    break
            top.add_top(self.score, login)
            return self.score
        elif choice == '3':
            x = QuestionGeography()
            x.question()
            top = TopQuizGeography()
            for i in range(len(x.questions_geo)):
                print(x.questions_geo[i]['ques'])
                answer = str.lower(input("Введіть відповідь: "))
                if x.questions_geo[i]['answer'] == answer:
                    self.score += 1
                    print("Правильна відповідь! +1 бал")
                else:
                    print("Відповідь неправильна")
                if i == 20:
                    print(f"Кінець вікторини! Ви заробили: {self.score} балів")
                    break
            top.add_top(self.score, login)
            return self.score
        elif choice == '4':
            print("""Виберіть варіант: 
            1. Історія і Біологія
            2. Історія і Географія
            3. Географія і Біологія
            4. Історія, Біологія і Географія""")
            y = input("Введіть ваш вибір: ")
            new_ques = []
            if y == '1':
                x1 = QuestionHistory()
                x2 = QuestionBiolog()
                x1.question()
                x2.question()
                top = TopQuizMixed()
                for i in range(100):
                    random_ques = random.randrange(0, 21)
                    if x1.questions_his[random_ques] not in new_ques and x2.questions_bio[random_ques] not in new_ques:
                        new_ques.append(x1.questions_his[random_ques])
                        new_ques.append(x2.questions_bio[random_ques])
                    else:
                        continue
                    if len(new_ques) == 20:
                        break
                for i in range(len(new_ques)):
                    print(new_ques[i]['ques'])
                    answer = str.lower(input("Введіть відповідь: "))
                    if new_ques[i]['answer'] == answer:
                        self.score += 1
                        print("Правильна відповідь! +1 бал")
                    else:
                        print("Відповідь неправильна")
                    if i == 20:
                        print(f"Кінець вікторини! Ви заробили: {self.score} балів")
                        break
                top.add_top(self.score, login)
                return self.score
            elif y == '2':
                x1 = QuestionHistory()
                x1.question()
                x2 = QuestionGeography()
                x2.question()
                top = TopQuizMixed()
                for i in range(100):
                    random_ques = random.randrange(0, 21)
                    if x1.questions_his[random_ques] not in new_ques and x2.questions_geo[random_ques] not in new_ques:
                        new_ques.append(x1.questions_his[random_ques])
                        new_ques.append(x2.questions_geo[random_ques])
                    else:
                        continue
                    if len(new_ques) == 20:
                        break
                for i in range(len(new_ques)):
                    print(new_ques[i]['ques'])
                    answer = str.lower(input("Введіть відповідь: "))
                    if new_ques[i]['answer'] == answer:
                        self.score += 1
                        print("Правильна відповідь! +1 бал")
                    else:
                        print("Відповідь неправильна")
                    if i == 20:
                        print(f"Кінець вікторини! Ви заробили: {self.score} балів")
                        break
                top.add_top(self.score, login)
                return self.score
            elif y == '3':
                x1 = QuestionGeography()
                x1.question()
                x2 = QuestionBiolog()
                x2.question()
                top = TopQuizMixed()
                for i in range(100):
                    random_ques = random.randrange(0, 21)
                    if x1.questions_geo[random_ques] not in new_ques and x2.questions_bio[random_ques] not in new_ques:
                        new_ques.append(x1.questions_geo[random_ques])
                        new_ques.append(x2.questions_bio[random_ques])
                    else:
                        continue
                    if len(new_ques) == 20:
                        break
                for i in range(len(new_ques)):
                    print(new_ques[i]['ques'])
                    answer = str.lower(input("Введіть відповідь: "))
                    if new_ques[i]['answer'] == answer:
                        self.score += 1
                        print("Правильна відповідь! +1 бал")
                    else:
                        print("Відповідь неправильна")
                    if i == 20:
                        print(f"Кінець вікторини! Ви заробили: {self.score} балів")
                        break
                top.add_top(self.score, login)
                return self.score
            elif y == '4':
                x1 = QuestionHistory()
                x2 = QuestionBiolog()
                x3 = QuestionGeography()
                x1.question()
                x2.question()
                x3.question()
                top = TopQuizMixed()
                for i in range(100):
                    random_ques = random.randrange(0, 21)
                    if x1.questions_his[random_ques] not in new_ques and x2.questions_bio[random_ques] not in new_ques and x3.questions_geo[random_ques] not in new_ques:
                        new_ques.append(x1.questions_his[random_ques])
                        new_ques.append(x2.questions_bio[random_ques])
                        if len(new_ques) == 20:
                            break
                        new_ques.append(x3.questions_geo[random_ques])
                    else:
                        continue
                    if len(new_ques) == 20:
                        break
                for i in range(len(new_ques)):
                    print(new_ques[i]['ques'])
                    answer = str.lower(input("Введіть відповідь: "))
                    if new_ques[i]['answer'] == answer:
                        self.score += 1
                        print("Правильна відповідь! +1 бал")
                    else:
                        print("Відповідь неправильна")
                    if i == 20:
                        print(f"Кінець вікторини! Ви заробили: {self.score} балів")
                        break
                top.add_top(self.score, login)
                return self.score


    def scores(self):
        pass



if __name__ == "__main__":
    edit = EditQuestion()
    quiz = Quiz()
    user = User()
    print("""Меню:
    1. Ввійти
    2. Додати нового користувача""")
    choice = input("Введіть ваш вибір: ")
    if choice == '1':
        user.entrace()
        if user.login:
            print("""1. Розпочати вікторину
            2. Переглянути топ
            3. Змінити пароль або дату народження
            4. Для адміністраторів""")
            choice_1 = input("Введіть ваш вибір: ")
            if choice_1 == '1':
                user.entrace()
                quiz.ques()
            elif choice_1 == '2':
                print("Виберіть категорію: \n1. Історія \n2. Біологія \n3. Географія \n4.Мікс")
                x = input("Введіть ваш вибір")
                if x == '1':
                    y = TopQuizHistory()
                    y.top()
                elif x == '2':
                    y = TopQuizBiolog()
                    y.top()
                elif x == '3':
                    y = TopQuizGeography()
                    y.top()
                elif x == '4':
                    y = TopQuizMixed()
                    y.top()
                else:
                    print("Помилка! Введіть корректний вибір!")
            elif choice_1 == '3':
                user.entrace()
                user.edit()
            elif choice_1 == '4':
                edit.status()
                edit.edit()
        else:
            print("Ви не авторизовані в системі! Зареєструйтесь або створіть нового користувача")
    elif choice == '2':
        user.data_user()
        if user.login:
            print("""1. Розпочати вікторину
            2. Переглянути топ
            3. Змінити пароль або дату народження
            4. Для адміністраторів""")
            choice_1 = input("Введіть ваш вибір: ")
            if choice_1 == '1':
                user.entrace()
                quiz.ques()
            elif choice_1 == '2':
                print("Виберіть категорію: \n1. Історія \n2. Біологія \n3. Географія \n4.Мікс")
                x = input("Введіть ваш вибір")
                if x == '1':
                    y = TopQuizHistory()
                    y.top()
                elif x == '2':
                    y = TopQuizBiolog()
                    y.top()
                elif x == '3':
                    y = TopQuizGeography()
                    y.top()
                elif x == '4':
                    y = TopQuizMixed()
                    y.top()
                else:
                    print("Помилка! Введіть корректний вибір!")
            elif choice_1 == '3':
                user.entrace()
                user.edit()
            elif choice_1 == '4':
                edit.status()
                edit.edit()
        else:
            print("Ви не авторизовані в системі! Зареєструйтесь або створіть нового користувача")
    else:
        print("Введіть корректний вибір")
