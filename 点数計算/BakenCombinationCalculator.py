def calculate_umaren_formation_points(line1, line2):
    """
    馬連フォーメーションの買い目点数を計算する
    :param line1: 軸1の馬番号リスト
    :param line2: 軸2の馬番号リスト
    :return: 買い目の点数
    """
    combinations = []
    for horse1 in line1:
        for horse2 in line2:
            if horse1 == horse2:  # 軸1と軸2で同じ馬を避ける
                continue
            combinations.append(sorted([horse1, horse2]))

    # 重複を削除
    distinct_array = list(set(tuple(sublist) for sublist in combinations))
    return len(distinct_array)

def calculate_umatan_formation_points(line1, line2):
    """
    馬単フォーメーションの買い目点数を計算する
    :param line1: 軸1の馬番号リスト
    :param line2: 軸2の馬番号リスト
    :return: 買い目の点数
    """
    permutations = []
    for horse1 in line1:
        for horse2 in line2:
            if horse1 == horse2:  # 軸1と軸2で同じ馬を避ける
                continue
            permutations.append([horse1, horse2])
    return len(permutations)

def calculate_3renpuku_formation_points(line1, line2, line3):
    """
    3連複フォーメーションの買い目点数を計算する
    :param line1: 軸1の馬番号リスト
    :param line2: 軸2の馬番号リスト
    :param line3: 軸3の馬番号リスト
    :return: 買い目の点数
    """
    combinations = []
    for horse1 in line1:
        for horse2 in line2:
            if horse1 == horse2:  # 軸1と軸2で同じ馬を避ける
                continue
            for horse3 in line3:
                if horse3 in (horse1, horse2):  # 同じ馬を避ける
                    continue
                combinations.append(sorted([horse1, horse2, horse3]))

    # 重複を削除
    distinct_array = list(set(tuple(sublist) for sublist in combinations))
    return len(distinct_array)

def calculate_3rentan_formation_points(line1, line2, line3):
    """
    3連単フォーメーションの買い目点数を計算する
    :param line1: 軸1の馬番号リスト
    :param line2: 軸2の馬番号リスト
    :param line3: 軸3の馬番号リスト
    :return: 買い目の点数
    """
    permutations = []
    for horse1 in line1:
        for horse2 in line2:
            if horse1 == horse2:  # 軸1と軸2で同じ馬を避ける
                continue
            for horse3 in line3:
                if horse3 in (horse1, horse2):  # 同じ馬を避ける
                    continue
                permutations.append([horse1, horse2, horse3])
    return len(permutations)