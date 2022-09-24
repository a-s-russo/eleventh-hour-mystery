import string


def code_cracker(msg, letter):
    first_letter_num = ord('A')
    last_letter_num = ord('Z')
    shift = ord(letter) - first_letter_num
    decoded_msg = []
    for char in msg:
        if char.upper() in string.ascii_uppercase:
            decoded_char_num = ord(char) - shift
            if decoded_char_num < first_letter_num:
                num = last_letter_num - (first_letter_num - decoded_char_num) + 1
            else:
                num = decoded_char_num
            decoded_msg.append(chr(num))
        else:
            decoded_msg.append(char)
    return ''.join(decoded_msg)


print(code_cracker('''MYXQBKDEVKDSYXC! SD GKC SXNOON USVBYI
DRO WYECO GRY CDYVO DRO POKCD. LED RO
RKN ROVZ: YXO REXNBON KXN OVOFOX YP
USVBYI'C PEBBI BOVKDSFOC RSN DROWCOVFOC
SX DRO RYECO KXN KBYEXN DRO QKBNOX KXN,
KD OVOFOX WSXEDOC DY OVOFOX DROI KVV
CMKWZOBON SXDY DRO LKXAEOD RKVV GSDR USVBYI
KXN KDO EZ KVV YP RYBKMO'C LOKEDSPEV PYYN.
KXN XYG, TECD DY CRYG RYG MVOFOB IYE KBO,
MKX IYE PSXN YXO REXNBON KXN OVOFOX WSMO
RSNNOX SX DRO ZSMDEBOC? RKZZI REXDSXQ!''', 'K'))
