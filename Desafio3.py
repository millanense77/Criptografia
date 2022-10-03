cadena = 'PCQ VMJYPD LBYK LYSO KBXBJXWXV BXV ZCJPO EYPD KBXBJYUXJ LBJOO KCPK. CP LBO LBCMKXPV XPV IYJKL PYDBL, QBOP KBO BXV OPVOV LBO LXRO CI SX’XJMI, KBO JCKO XPV EYKKOV LBO DJCMPV ZOICJO BYS, KXUYPD: “DJOXL EYPD, ICJ X LBCMKXPV XPV CPO PYDBLK Y BXNO ZOOP JOACMPLYPD LC UCM LBO IXZROK CI FXKL XDOK XPV LBO RODOPVK CI XPAYOPL EYPDK. SXU Y SXEO KC ZCRV XK LC AJXNO X IXNCMJ CI UCMJ SXGOKLU?” OFYRCDMO, LXROK IJCS LBO LBCMKXPV XPV CPO PYDBL'

from string import ascii_uppercase as alfabeto

lista = {}
for i in alfabeto:
    lista[i] = cadena.count(i)

L = sorted(lista.items(), key = lambda x : x[1], reverse=True)

cadena1 = cadena.replace('L','t')
cadena1 = cadena1.replace('B','h')
cadena1 = cadena1.replace('O','e')
cadena1 = cadena1.replace('S','m')
cadena1 = cadena1.replace('J','r')
cadena1 = cadena1.replace('Y','i')
cadena1 = cadena1.replace('I','f')
cadena1 = cadena1.replace('K','s')
cadena1 = cadena1.replace('R','l')
cadena1 = cadena1.replace('Z','b')
cadena1 = cadena1.replace('C','o')
cadena1 = cadena1.replace('M','u')
cadena1 = cadena1.replace('X','a')
cadena1 = cadena1.replace('P','n')
cadena1 = cadena1.replace('V','d')
cadena1 = cadena1.replace('Q','w')
cadena1 = cadena1.replace('D','g')
cadena1 = cadena1.replace('U','y')
cadena1 = cadena1.replace('E','k')
cadena1 = cadena1.replace('A','c')
cadena1 = cadena1.replace('N','v')
cadena1 = cadena1.replace('W','z')
cadena1 = cadena1.replace('G','j')
cadena1 = cadena1.replace('F','p')

print("\n"+cadena1+"\n")