import random

print('''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           ''')

list_kartu = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dealer():
  list_kartu_bot = list_kartu[:2]
  total_kartu_bot = sum(list_kartu_bot)
  print(f'kartu bot adalah {list_kartu_bot} dengan total {total_kartu_bot}')
  if total_kartu_bot > total_kartu_player:
    print('anda kalah dan bot menang')
  elif total_kartu_bot < total_kartu_player:
    print('anda menang')
  elif total_kartu_bot == total_kartu_player:
    print('Draw')



random.shuffle(list_kartu)
list_kartu_player = list_kartu[:2]
total_kartu_player = sum(list_kartu_player)

print(f'kartu anda adalah {list_kartu_player} dengan total {total_kartu_player}')
kondisi = True
while kondisi:
  lanjut = input('pengen nambah kartu lagi ? ')
  if lanjut == 'y':
    angka_tambahan = random.choice(list_kartu)
    total_kartu_player += angka_tambahan
    print(total_kartu_player)
    if total_kartu_player > 21:
      print('upss anda burst')
      kondisi = False
  elif lanjut == 'n':
    dealer()
    kondisi = False
