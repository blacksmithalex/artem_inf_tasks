one_photo_memory = 7680 * 4320 * 16 # размер одного фото в битах
one_card_memory = 9 * 1024 * 1024 * 1024 * 8 # размер одной карты в битах

number_of_photo = one_card_memory // one_photo_memory # количество фотографий на одной карте
print(f'Количество фотографий на последней карте = {4010 % number_of_photo}')