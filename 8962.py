import hashlib
import time

# Класс User
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

    def __repr__(self):
        return f"User(nickname={self.nickname}, age={self.age})"

# Класс Video
class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"

# Класс UrTube
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Вошли как {user.nickname}")
                return
        print("Неверные данные для входа")

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f"Пользователь {nickname} зарегистрирован")
    
    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                self.play_video(video)
                return

        print(f"Видео '{title}' не найдено")

    def play_video(self, video):
        print(f"Начало воспроизведения видео: {video.title}")
        while video.time_now < video.duration:
            print(video.time_now + 1)
            video.time_now += 1
            time.sleep(1)
        print("Конец видео")

# Пример использования

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))    # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  # Войдите в аккаунт, чтобы смотреть видео
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')  # Вам нет 18 лет, пожалуйста покиньте страницу
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')  # Видео воспроизводится

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)  # User(nickname=vasya_pupkin, age=55)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')  # Видео 'Лучший язык программирования 2024 года!' не найдено
