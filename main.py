from module import *
csincsillak:list[Csincsilla] = []
file = open(file='chi.txt', mode='r', encoding='utf-8')
for sor in file:
    csincsillak.append(Csincsilla(sor))

print('2. feladat:')
print(f'összesen {len(csincsillak)} csincsilla van')

szhsdb:int = 0
for cs in csincsillak:
    if cs.szereti: szhsdb += 1
szazalek:float = round(szhsdb / len(csincsillak) * 100, 2)
print('3. feladat:')
print(f'a csincsillák {szazalek}%-a szereti, ha simizik')

print('4. feladat:')
for cs in csincsillak:
    if cs.kor >= 8 and cs.suly < 360:
        print(f'{cs.nev} {cs.kor} éves és {cs.suly} gramm')
        break
else: print('nincs öreg és sovány csincsilla a listában')


# átlagéletkor
es:int = 0
for cs in csincsillak:
    es += cs.kor
print(f'atlageletokor: {round(es/len(csincsillak), 2)}')

# legnagyobb súlyú álat neve
mxi:int = 0
for i in range(1, len(csincsillak)):
    if csincsillak[i].suly > csincsillak[mxi].suly:
        mxi = i
print(f'a legnagyobb sulyu neve: {csincsillak[mxi].nev}')

# 4 évesnél fiatalabb állatok nevei
fnevk:list[str] = []
for cs in csincsillak:
    if cs.kor < 4:
        fnevk.append(cs.nev)
print('4 evesnel fiatalabb allatok:')
for n in fnevk:
    print(f'  - {n}')

# "B" betűvel kezdődő nevű csincsillák száma
bc:int = 0
for cs in csincsillak:
    if cs.nev[0] == 'B':
        bc += 1
print(f'b-vel kezdodo nevu allatok szama: {bc}')

# legfiatalabb neve
mni:int = 0
for i in range(1, len(csincsillak)):
    if csincsillak[i].kor < csincsillak[mni].kor:
        mni = i
print(f'legfiatalabb allat neve: {csincsillak[mni].nev}')