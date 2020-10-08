def fibonSeq(max_num):
    seq = [0, 1]

    while seq[-1] < max_num:
        print(f"{seq[-1]} < {max_num}")
        seq.append(seq[-2] + seq[-1])
    return seq

print(fibonSeq(66))