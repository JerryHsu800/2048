#coding=gbk
import random

data = []

ecount = 16 # 空余位置数量
score = 0

running = False

# 初始化数据，并随意放置两个2
def init():
    global data
    global ecount
    data = [[None for i in range(4)] for j in range(4)]

    generate()
    generate()

# 生成一个2或4，并放到空余位置
# mode 0 只生成2 用于游戏初始化
# mode 1 生成2或4 用于游戏运行时
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
    print('┌────┬────┬────┬────┐')
    for i,row in enumerate(data):
        line = '│'
        for d in row:
            if not d:
                line = line + '        │'
            else :
                line = line + '%6i  │'%d
        print('│        │        │        │        │')
        print(line)
        print('│        │        │        │        │')
        if i < 3 :
            print('├────┼────┼────┼────┤')
    print('└────┴────┴────┴────┘')

#direct 移动方向  0上 1下 2左 3右
def onMove(direct):
    global ecount
    global score
    global running
    #纵向
    if( direct == 0 or direct == 1 ) :
        # 合并
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
        # 移动
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
    # 横向
    if( direct == 2 or direct == 3 ) :
        #合并
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
        #移动
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
        elif ( key == 'w' ) : # 上
            onMove(0)
        elif ( key == 's' ) : # 下
            onMove(1)
        elif ( key == 'a' ) : # 左
            onMove(2)
        elif ( key == 'd' ) : # 右
            onMove(3)


if __name__ == '__main__':
    init()
    draw()
    circle()



