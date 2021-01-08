from time import sleep
import emoji
feliz = 'Feliz Ano Novo'
fogos = ':boom::boom::boom::boom::boom::boom:'
for c in range(10, 0, -1):
    print(c)
    sleep(0.4)
print(emoji.emojize(f'{fogos*3:^20}', use_aliases=True))
print(f'{feliz:^30}')
print(emoji.emojize(f'{fogos*3:^20}', use_aliases=True))
