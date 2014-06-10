#coding=gbk
import random

data = []

ecount = 16 # ����λ������
score = 0

running = False

# ��ʼ�����ݣ��������������2
def init():
    global data
    global ecount
    data = [[None for i in range(4)] for j in range(4)]

    generate()
    generate()

# ����һ��2��4�����ŵ�����λ��
# mode 0 ֻ����2 ������Ϸ��ʼ��
# mode 1 ����2��4 ������Ϸ����ʱ
def generate(mode = 1):
    global ecount
    if( ecount <= 0 ):
        return
    d = 2 if mode == 0 else random.randint(1,2)*2

    pos = random.randint(0, ecount-1)

    s = 0
    for i in range(4):
        for j in range(4):
            if data[i][j]:
                continue
            if s == pos :
                data[i][j] = d
                ecount -= 1
                return
            s += 1

def draw():
    print(' score : %i'%score)
    print('�����������Щ��������Щ��������Щ���������')
    for i,row in enumerate(data):
        line = '��'
        for d in row:
            if not d:
                line = line + '        ��'
            else :
                line = line + '%6i  ��'%d
        print('��        ��        ��        ��        ��')
        print(line)
        print('��        ��        ��        ��        ��')
        if i < 3 :
            print('�����������੤�������੤�������੤��������')
    print('�����������ة��������ة��������ة���������')

#direct �ƶ�����  0�� 1�� 2�� 3��
def onMove(direct):
    global ecount
    global score
    global running
    #����
    if( direct == 0 or direct == 1 ) :
        # �ϲ�
        for i in range(4):
            idx = 0
            d = 0
            for j in range(4):
                d0 = data[j][i]
                if d and d == d0 :
                    data[j][i] = None
                    data[idx][i] = d+d
                    score += d+d
                    d = 0
                    idx = 0
                    ecount += 1
                elif d0:
                    idx = j
                    d = d0
        # �ƶ�
        start = 0 if direct == 0 else 3
        end = 4 if direct == 0 else -1
        step = 1 if direct == 0 else -1

        for i in range(4):
            idx = start
            for j in range(start, end, step):
                d = data[j][i]
                if d :
                    if j != idx:
                        data[idx][i] = d
                        data[j][i] = None
                    idx += step
    # ����
    if( direct == 2 or direct == 3 ) :
        #�ϲ�
        for i in range(4):
            idx = 0
            d = 0
            for j in range(4):
                d0 = data[i][j]
                if d and d == d0 :
                    data[i][j] = None
                    data[i][idx] = d+d
                    score += d+d
                    d = 0
                    idx = 0
                    ecount += 1
                elif d0:
                    idx = j
                    d = d0
        #�ƶ�
        start = 0 if direct == 2 else 3
        end = 4 if direct == 2 else -1
        step = 1 if direct == 2 else -1

        for i in range(4):
            idx = start
            for j in range(start, end, step):
                d = data[i][j]
                if d :
                    if j != idx:
                        data[i][idx] = d
                        data[i][j] = None
                    idx += step
    generate()
    draw()

    if ecount == 0 and checkOver():
        print(' Game Over')
        running = False


def checkOver():
    for i in range(4):
        d = 0
        for j in range(4):
            d0 = data[j][i]
            if d and d == d0 :
                return False
            elif d0:
                idx = j
                d = d0
    for i in range(4):
        d = 0
        for j in range(4):
            d0 = data[i][j]
            if d and d == d0 :
                return False
            elif d0:
                d = d0
    return True

def circle():
    import msvcrt

    global running
    running = True

    while ( running ) :
        key = msvcrt.getch()
        if( key == '\x1b' ):
            print('88')
            break
        elif ( key == 'w' ) : # ��
            onMove(0)
        elif ( key == 's' ) : # ��
            onMove(1)
        elif ( key == 'a' ) : # ��
            onMove(2)
        elif ( key == 'd' ) : # ��
            onMove(3)


if __name__ == '__main__':
    init()
    draw()
    circle()



