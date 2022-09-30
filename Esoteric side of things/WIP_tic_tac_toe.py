# Turn 9
@lambda _: [_[0], print(_[0]), _[-1]] if _[0] != None else [None,]
@lambda _: [_[0], print(" %s | %s | %s\n───+───+──\n %s | %s | %s\n───+───+──\n %s | %s | %s" % (*_[0],)), _[-1]] if _[0] != None else [None,]
@lambda _: [_[0][:_[1]-1] + "xo"[_[-1]] + _[0][_[1]:], (_[-1] + 1) % 2] if _[0] != None else [None,]
@lambda _: [print({'xxx': 'Game ended X wins', 'ooo': 'Game ended O wins'}[next(filter(lambda __ : __ in ['xxx','ooo'], [_[0][2:7:2], _[0][0:9:4], _[0][0:7:3], _[0][1:8:3], _[0][2:9:3], _[0][0:3], _[0][3:6], _[0][6:9]]))])] if len(list(filter(lambda __ : __ in ['xxx','ooo'], [_[0][2:7:2], _[0][0:9:4], _[0][0:7:3], _[0][1:8:3], _[0][2:9:3], _[0][0:3], _[0][3:6], _[0][6:9]]))) == 1 else [_[0], int(input("Which cell ? (1-9): ")), _[-1]]
# Turn 8
@lambda _: [_[0], print(_[0]), _[-1]] if _[0] != None else [None,]
@lambda _: [_[0], print(" %s | %s | %s\n───+───+──\n %s | %s | %s\n───+───+──\n %s | %s | %s" % (*_[0],)), _[-1]] if _[0] != None else [None,]
@lambda _: [_[0][:_[1]-1] + "xo"[_[-1]] + _[0][_[1]:], (_[-1] + 1) % 2] if _[0] != None else [None,]
@lambda _: [print({'xxx': 'Game ended X wins', 'ooo': 'Game ended O wins'}[next(filter(lambda __ : __ in ['xxx','ooo'], [_[0][2:7:2], _[0][0:9:4], _[0][0:7:3], _[0][1:8:3], _[0][2:9:3], _[0][0:3], _[0][3:6], _[0][6:9]]))])] if len(list(filter(lambda __ : __ in ['xxx','ooo'], [_[0][2:7:2], _[0][0:9:4], _[0][0:7:3], _[0][1:8:3], _[0][2:9:3], _[0][0:3], _[0][3:6], _[0][6:9]]))) == 1 else [_[0], int(input("Which cell ? (1-9): ")), _[-1]]
# Turn 7
@lambda _: [_[0], print(_[0]), _[-1]] if _[0] != None else [None,]
@lambda _: [_[0], print(" %s | %s | %s\n───+───+──\n %s | %s | %s\n───+───+──\n %s | %s | %s" % (*_[0],)), _[-1]] if _[0] != None else [None,]
@lambda _: [_[0][:_[1]-1] + "xo"[_[-1]] + _[0][_[1]:], (_[-1] + 1) % 2] if _[0] != None else [None,]
@lambda _: [print({'xxx': 'Game ended X wins', 'ooo': 'Game ended O wins'}[next(filter(lambda __ : __ in ['xxx','ooo'], [_[0][2:7:2], _[0][0:9:4], _[0][0:7:3], _[0][1:8:3], _[0][2:9:3], _[0][0:3], _[0][3:6], _[0][6:9]]))])] if len(list(filter(lambda __ : __ in ['xxx','ooo'], [_[0][2:7:2], _[0][0:9:4], _[0][0:7:3], _[0][1:8:3], _[0][2:9:3], _[0][0:3], _[0][3:6], _[0][6:9]]))) == 1 else [_[0], int(input("Which cell ? (1-9): ")), _[-1]]
# Turn 6
@lambda _: [_[0], print(_[0]), _[-1]] if _[0] != None else [None,]
@lambda _: [_[0], print(" %s | %s | %s\n───+───+──\n %s | %s | %s\n───+───+──\n %s | %s | %s" % (*_[0],)), _[-1]] if _[0] != None else [None,]
@lambda _: [_[0][:_[1]-1] + "xo"[_[-1]] + _[0][_[1]:], (_[-1] + 1) % 2] if _[0] != None else [None,]
@lambda _: [print({'xxx': 'Game ended X wins', 'ooo': 'Game ended O wins'}[next(filter(lambda __ : __ in ['xxx','ooo'], [_[0][2:7:2], _[0][0:9:4], _[0][0:7:3], _[0][1:8:3], _[0][2:9:3], _[0][0:3], _[0][3:6], _[0][6:9]]))])] if len(list(filter(lambda __ : __ in ['xxx','ooo'], [_[0][2:7:2], _[0][0:9:4], _[0][0:7:3], _[0][1:8:3], _[0][2:9:3], _[0][0:3], _[0][3:6], _[0][6:9]]))) == 1 else [_[0], int(input("Which cell ? (1-9): ")), _[-1]]
# Turn 5
@lambda _: [_[0], print(_[0]), _[-1]] if _[0] != None else [None,]
@lambda _: [_[0], print(" %s | %s | %s\n───+───+──\n %s | %s | %s\n───+───+──\n %s | %s | %s" % (*_[0],)), _[-1]] if _[0] != None else [None,]
@lambda _: [_[0][:_[1]-1] + "xo"[_[-1]] + _[0][_[1]:], (_[-1] + 1) % 2] if _[0] != None else [None,]
@lambda _: [print(_)]
@lambda _: [print({'xxx': 'Game ended X wins', 'ooo': 'Game ended O wins'}[next(filter(lambda __ : __ in ['xxx','ooo'], [_[0][2:7:2], _[0][0:9:4], _[0][0:7:3], _[0][1:8:3], _[0][2:9:3], _[0][0:3], _[0][3:6], _[0][6:9]]))])] if len(list(filter(lambda __ : __ in ['xxx','ooo'], [_[0][2:7:2], _[0][0:9:4], _[0][0:7:3], _[0][1:8:3], _[0][2:9:3], _[0][0:3], _[0][3:6], _[0][6:9]]))) == 1 else [_[0], int(input("Which cell ? (1-9): ")), _[-1]]
# Turn 4
@lambda _: [_[0], print(_[0]), _[-1]]
@lambda _: [_[0], print(" %s | %s | %s\n───+───+──\n %s | %s | %s\n───+───+──\n %s | %s | %s" % (*_[0],)), _[-1]]
@lambda _: [_[0][:_[1]-1] + "xo"[_[-1]] + _[0][_[1]:], (_[-1] + 1) % 2]
@lambda _: [_[0], int(input("Which cell ? (1-9): ")), _[-1]]
# Turn 3
@lambda _: [_[0], print(_[0]), _[-1]]
@lambda _: [_[0], print(" %s | %s | %s\n───+───+──\n %s | %s | %s\n───+───+──\n %s | %s | %s" % (*_[0],)), _[-1]]
@lambda _: [_[0][:_[1]-1] + "xo"[_[-1]] + _[0][_[1]:], (_[-1] + 1) % 2]
@lambda _: [_[0], int(input("Which cell ? (1-9): ")), _[-1]] 
# Turn 2
@lambda _: [_[0], print(_[0]), _[-1]]
@lambda _: [_[0], print(" %s | %s | %s\n───+───+──\n %s | %s | %s\n───+───+──\n %s | %s | %s" % (*_[0],)), _[-1]]
@lambda _: [_[0][:_[1]-1] + "xo"[_[-1]] + _[0][_[1]:], (_[-1] + 1) % 2]
@lambda _: [_[0], int(input("Which cell ? (1-9): ")), _[-1]]
# Turn 1
@lambda _: [_[0], print(_[0]), _[-1]] 
@lambda _: [_[0], print(" %s | %s | %s\n───+───+──\n %s | %s | %s\n───+───+──\n %s | %s | %s" % (*_[0],)) , _[-1]]
@lambda _: [_[0][:_[1]-1] + "xo"[_[-1]] + _[0][_[1]:], (_[-1] + 1) % 2]
@lambda _: ["         ", int(input("Which cell ? (1-9): ")), 0]
def tic_tac_toe():
    pass