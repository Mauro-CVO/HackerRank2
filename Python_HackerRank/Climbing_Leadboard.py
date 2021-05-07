from collections import Counter

def climbing_leadboard(rank,player):
    player.sort()
    rank = dict(Counter(rank))
    rank = [v for v in rank.keys()]
    rank.sort()
    len_rank1 = len(rank)
    '''
    print('rank: ', rank)
    print("--" * 20)
    print("player: ", player)
    #'''
    
    for i in range(len(player)):
        for j in range(len(rank)):
            if player[i] < rank[j]:
                rank.insert(j, player[i])
                print(len(rank) - j)
                break
            #if  num > max(rank):
            #    rank.insert(len(rank), num)
            #    print(1)
                
    x = len(rank) - len_rank1
    ones = player[x:] 
    for one in ones:
        print(1)



    #print('rank: {}, player {}'.format(rank,player))

def run():

    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    '''
    ranked = [100,100,50,40,40,20,10]
    player = [5 ,25, 50, 120]'''
    climbing_leadboard(ranked, player)
    #'''
if __name__ == "__main__":
    run()