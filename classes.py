import time
import math
from threading import Timer
class Album:
    '''Класс альбом '''
    playlist = { 'OLD BLOOD' : ['Angry toy$', 'Vozrast', 'Umi', 'ART HOES', 'X2', '4 shaga'],
    'VOODOO CHILD' : ['ЗЕРКАЛА', 'I CAN KICK IT', 'ВКУС ЯДА', 'ВУДУ', 'ВУССАП!', 'ЗЕЛЕНЬ', 'ПАЦАНЫ'],
    'PAUSA' : ['Simple', 'Recuerdo', 'Cae de Una', 'Quiéreme', 'Tiburones', 'Cántalo'],
    'Tell Me a Fairytale' : ['Призрак войны','На линии огня', 'Encore', 'Пожар'],
    'Правило' : ['Призрак', 'Из-за тебя', 'Чувствую', 'AMG', 'Не хочу', 'Без ключа', 'Ночь пятницы']}

    def __init__(self, name):
        '''Инициализация'''
        self.name = name
        self.author = ''

    def __str__(self):
        '''Метод строкового представления'''
        musics = []
        for k in Album.playlist:
            if k == self.name:
                musics = Album.playlist.get(k)
        info = '♫♫♫ АЛЬБОМ - ' + self.name + ' ♫♫♫\n'
        info += '------------ТРЕКИ------------' + '\n'
        num = 1
        for k in musics:
            info += str(num)+ '. '+k + '\n'
            num += 1
        return info
    def __repr__(self):
        return self.author

    def find_author(self):
        '''Метод поиска исполнителя'''
        al_au = {'OLD BLOOD' : 'Boulevard Depo', 'VOODOO CHILD' : 'GONE.Fludd',
                 'PAUSA': 'Ricky Martin', 'Tell Me a Fairytale' : 'Tell Me a Fairytale',
                 'Правило' : 'PHARAOH', }
        for k in al_au:
            if self.name == k:
                self.author = al_au.get(k)
        return self.author

    def track(self):
        '''Треки в альбоме'''
        musics = []
        for k in Album.playlist:
            if k == self.name:
                musics = Album.playlist.get(k)
        return musics





class Track:
    '''Класс музыкального трека'''
    info_track = {'Angry toy$': 2.06, 'Возраст': 2.17, 'Умы': 2.04, 'ART HOES': 3.02, 'X2': 2.56, '4 шага': 2.14,
    'ЗЕРКАЛА': 1.59, 'I CAN KICK IT': 2.59, 'ВКУС ЯДА': 3.15, 'ВУДУ': 1.42, 'ВУССАП!': 2.04, 'ЗЕЛЕНЬ': 3.30,
    'ПАЦАНЫ': 2.11, 'Simple': 3.35, 'Recuerdo': 3.52, 'Cae de Una': 3.38, 'Quiéreme': 3.05, 'Tiburones': 3.13,
    'Cántalo': 3.39, 'Призрак войны': 3.37, 'На линии огня': 4.14, 'Encore': 4.15, 'Пожар': 3.54,
    'Призрак': 2.49, 'Из-за тебя': 3.18, 'Чувствую': 2.48, 'AMG': 2.51, 'Не хочу': 3.08,
    'Без ключа': 2.39, 'Ночь пятницы': 3.14}
    strat_t = 0
    time_t = 0
    time_end = 0



    def __init__(self, name= ''):
        '''Инициализация'''
        self.name = name

    def __str__(self):
        '''Метод строкового представления'''
        return self.name

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def __end():
        '''Статический метод для окончания трека'''
        Track.strat_t = 0
        Track.time_t = 0
        Track.time_end = 0
        print('Трек закончился')
        print('Введите ''2'' чтобы продолжить')

    def play(self, trackk):
        '''Метод запуска трека, также можно прервать таймер музыки любым вводом'''
        timeout = 0
        timeout += Track.time_end
        for k in Track.info_track:
            if trackk == k:
                timeout += Track.info_track.get(k)

        m = math.floor(timeout)
        s = 100 * (timeout - m)
        timeout = (m * 60) + s
        Track.strat_t = time.time()
        t = Timer(timeout, Track.__end)
        t.start()
        print('♬ ♬ ♬ Трек играет ♬ ♬ ♬')
        try:
            pause = "1. Пауза - абсолютно любой ввод с клавиатуры\n"
            answer = input(pause)

        finally:
            t.cancel()
    def pause(self, trackk):
        '''Метод паузы для трека'''
        timeout = 0
        for k in Track.info_track:
            if  trackk == k:
                timeout = Track.info_track.get(k)
        m = math.floor(timeout)
        s = 100 * (timeout - m)
        timeout = (m * 60) + s
        Track.time_t += (time.time() - Track.strat_t)
        h = str(round(Track.time_t) // 3600)
        m = str((round(Track.time_t) // 60) % 60)
        s = str(round(Track.time_t) % 60)
        if Track.time_t > timeout:
            h = str(round(timeout) // 3600)
            m = str((round(timeout) // 60) % 60)
            s = str(round(timeout) % 60)
            print(h + ':' + m + ':' + s + ' прошло')
        else:
            print('⏸ ' + h + ':' + m + ':' + s + ' прошло')









