#Существует множество веб-сайтов, на которых вы можете послушать музыку.
# Как правило, там представлены альбомы, содержащие треки. Каждый трек имеет название,
# продолжительность, имя исполнителя, год выпуска альбома и другие данные.
# Разработайте классы для альбомов и треков. Подумайте и реализуйте методы,
# которые могут воспроизводить трек, "ставить трек на паузу",
# останавливать воспроизведение треков и выполнять другие действия.

import classes
def main():
    '''Основная функция для запуска программы'''
    while True:
        fon = ('''✻✻✻✻✻✻✻✻✻✻✻✻✻✻✻Hello!✻✻✻✻✻✻✻✻✻✻✻✻✻✻✻✻✻
        .ιllιlι.Музыкальная программа.ιllιlι.
Вы можете выбрать плейлист, а затем музыкальный трек
    
▼▼▼▼▼▼▼▼▼▼Представленные альбомы▼▼▼▼▼▼▼▼▼▼▼▼▼
1.OLD BLOOD
2.VOODOO CHILD
3.PAUSA
4.Tell Me a Fairytale
5.Правило
▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲''')
        print(fon)
        ans = 0
        while ans != 100:
            sel_al = int(input("Введи номер альбома:"))
            albom = ['OLD BLOOD', 'VOODOO CHILD', 'PAUSA', 'Tell Me a Fairytale', 'Правило']
            info_al = classes.Album(albom[sel_al - 1])
            print('------Информация об альбоме-------', '\n',
                  '.ιl Исполнитель', classes.Album(albom[sel_al - 1]).find_author(), 'lι.',
                  '2020г','\n ',
                  info_al)
            print('Номер трека или Вернутся назад(9)')
            ans = int(input('Ввод: '))
            if ans == 9:
                break
            info_track = classes.Album(albom[sel_al - 1]).track()[ans-1]
            chose = 5
            classes.Track.strat_t = 0
            classes.Track.time_end = 0
            classes.Track.time_t = 0
            while chose != 9:
                print('-------------------------------------')
                print('1. Воcпроизвести - ', info_track + '\n9. Назад ')
                chose = int(input('Введите цифру: '))
                if chose == 1:
                    classes.Track().play(info_track)
                    classes.Track().pause(info_track)

main()
