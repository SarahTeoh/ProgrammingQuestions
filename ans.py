# Python
def answer1(arr):
    # 与えれられた配列の長さ
    n = len(arr)

    # 配列に”含まれない”最小の自然数の初期値
    min_missing = 1

    # 空配列が与えられた場合
    if n == 0:
        return min_missing

    # 与えられた配列を昇順に並び替える
    arr.sort()

    # 配列に”含まれない”最小の自然数が配列に含まれている場合，min_missing+1
    for i in range(n):
        if arr[i] == min_missing:
            min_missing += 1

    return min_missing    

def answer2(arr):
    # 与えれられた配列の長さ
    n = len(arr)

    # 配列に”含まれない”最小の自然数の初期値
    min_missing = 1

    # 空配列が与えられた場合
    if n == 0:
        return min_missing
    
    # min_missingより大きな整数を格納する配列
    x = []

    for i in range(n):
        # 現在の値がmin_missingより大きければxに格納
        if (arr[i] > min_missing):
            x.append(arr[i])
        
        # min_missingが配列に入っていればを配列に”含まれない”最小の自然数を更新
        elif (min_missing == arr[i]):
            min_missing += 1

            # 更新されたmin_missingがすでにxに入っていれば削除してmin_missingを更新
            while (x.count(min_missing)):
                x.remove(min_missing)
                min_missing += 1

    return min_missing
