#las "v" y las "V" son diferente letra
texto_original="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCEAX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
#este no es el orden que nos han dado. Hay que probar con el que nos han dado e ir camiando letras hasta que coincida
mas_com_castellano = ["E","A","R","O","I","N","L","D","C","U","T","S","M","P","B","F","Q","J","Y","V","G","H","X","Z","Ñ","Y","W"]

def bilatuPosHizkia(hizkia,elem):
    for i in range(len(elem)):
        if elem[i][0]==hizkia:
            return i

counter = {}

for letra in texto_original:
    if letra.isalpha(): #".", ",", " " eta zenbakiak ez dira kontatuko 
        if letra not in counter:	
            counter[letra] = 0
        counter[letra] += 1

print(len(counter)," hizki desberdin aurkitu dira.")

elementuak = list(counter.items())

elementuak.sort(key = lambda x:x[1], reverse = True)

print(elementuak)

#String-a array bihurtuko dugu:
texto_lista = list(texto_original)

for i in range(len(texto_lista)):
    if texto_lista[i].isalpha():
        pos = bilatuPosHizkia(texto_lista[i],elementuak)
        texto_lista[i] = mas_com_castellano[pos]

texto_descif = "".join(texto_lista)
print(texto_descif)