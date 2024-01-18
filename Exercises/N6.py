def bisestile(anno):
    if anno % 100 == 0:
     if anno % 400 == 0:
        return True
     else:
         return False
    else:
        if anno % 4 == 0:
            return True
    return False
    
def main():
    anno = int(input())
    if bisestile(anno):
        print('BISESTILE', end='')
    else:
        print('NON BISESTILE', end='')

main()  