 
def poisoned(badbottle):
    p_cnt = 0
    for p in range(10):
        if badbottle & (1 << p):
             # strategia spozycia = i-ty zawodnik spozywa napoj jesli i-ty bit w zapisie jego indexie jest zapalony
             # n pomocnikow potrafii z dokladnoscia 100% rozpoznac 2**n butelek.
            p_cnt = p_cnt + 1
    return p_cnt


if __name__ == "__main__":

    cnt = [0] * 11

    for bb in range(1, 1001):
        cnt[poisoned(bb)] += 1

    print(cnt)

    for i in range(len(cnt)):
        cnt[i] *= i

    print(sum(cnt) / 1000)




