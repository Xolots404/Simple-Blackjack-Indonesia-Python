import random

print('''
888     888                888       d8b                888      
888     888                888       Y8P                888      
888     888                888                          888      
88888b. 888 8888b.  .d8888b888  888 8888 8888b.  .d8888b888  888 
888 "88b888    "88bd88P"   888 .88P "888    "88bd88P"   888 .88P 
888  888888.d888888888     888888K   888.d888888888     888888K  
888 d88P888888  888Y88b.   888 "88b  888888  888Y88b.   888 "88b 
88888P" 888"Y888888 "Y8888P888  888  888"Y888888 "Y8888P888  888 
                                     888                         
                                    d88P                         
                                  888P"                          ''')

list_kartu = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dealer():
  random.shuffle(list_kartu)
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
