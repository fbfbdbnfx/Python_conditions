import math

god=int(input('какой год? '))
animals=['крысы', 'коровы', 'тигра', 'зайца', 'дракона', 'змеи', 'лошади', 'овцы', 'обезьяны', 'петуха', 'собаки', 'свиньи']
nomer_v_zikle=(god-4)%12
zhivotnoe_goda=''
match nomer_v_zikle:
	case 0: zhivotnoe_goda=animals[0]
	case 1: zhivotnoe_goda=animals[1]
	case 2: zhivotnoe_goda=animals[2]
	case 3: zhivotnoe_goda=animals[3]
	case 4: zhivotnoe_goda=animals[4]
	case 5: zhivotnoe_goda=animals[5]
	case 6: zhivotnoe_goda=animals[6]
	case 7: zhivotnoe_goda=animals[7]
	case 8: zhivotnoe_goda=animals[8]
	case 9: zhivotnoe_goda=animals[9]
	case 10: zhivotnoe_goda=animals[10]
	case 11: zhivotnoe_goda=animals[11]

print('Это год',zhivotnoe_goda)
