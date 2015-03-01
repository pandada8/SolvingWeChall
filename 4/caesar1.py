import string

words = "VJG SWKEM DTQYP HQZ LWORU QXGT VJG NCBA FQI QH ECGUCT CPF AQWT WPKSWG UQNWVKQP KU EJTDNPKIUFEH"
for i in range(1,26):
    print(''.join(map(lambda x: chr((ord(x) - ord('A')+i)%26 + ord('A')) if x in string.ascii_uppercase else x, words)))
