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
# legnagyobb súlyú álat neve
# 4 évesnél fiatalabb állatok nevei
# "B" betűvel kezdődő nevű csincsillák száma
# legfiatalabb neve