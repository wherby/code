#Suppose you are designing a social network. Every member has a list of his/her direct friends. 
#Member's direct friends are level 1 friends. 
#Member's friends' friends are level 2 friends, and so on.
#Given a name and print this member's level 1, level 2, level n friends.



def geneNetwork(relations,levelNum):
    n = len(relations)
    network = []
    relationLevels = []
    for i in range(n):
        network.append({})
        leve = [] 
        relationLevels.append(leve)

    for i in range(n):
        relation = relations[i]
        for t in relation:
            if t not in network[i]:
                network[i][t] =1
                if len(relationLevels[i]) == 0: 
                    relationLevels[i].append([t])
                else:
                    relationLevels[i][-1].append(t)
    for i in range(1,levelNum):
        for j in range(n):
            relation = relationLevels[j][i-1]
            #print relation
            relationLevels[j].append([])
            for t in relation:
                leve0 = relationLevels[t][0]
                #print leve0
                for k in leve0:
                    if k not in network[j]:
                        network[j][k] =1
                        relationLevels[j][-1].append(k)
                    #print k
                    #print relationLevels[i][-1].append(k)
                    #relationLevels[i][-1].append(k)
                

    print network,relationLevels





relations= [[1],[2],[3],[4],[5],[0]]

geneNetwork(relations,1)
geneNetwork(relations,2)
geneNetwork(relations,3)


#[{1: 1}, {2: 1}, {3: 1}, {4: 1}, {5: 1}, {0: 1}] [[[1]], [[2]], [[3]], [[4]], [[5]], [[0]]]
#[{1: 1, 2: 1}, {2: 1, 3: 1}, {3: 1, 4: 1}, {4: 1, 5: 1}, {0: 1, 5: 1}, {0: 1, 1: 1}] [[[1], [2]], [[2], [3]], [[3], [4]], [[4], [5]], [[5], [0]], [[0], [1]]]
#[{1: 1, 2: 1, 3: 1}, {2: 1, 3: 1, 4: 1}, {3: 1, 4: 1, 5: 1}, {0: 1, 4: 1, 5: 1}, {0: 1, 1: 1, 5: 1}, {0: 1, 1: 1, 2: 1}] [[[1], [2], [3]], [[2], [3], [4]], [[3], [4], [5]], [[4], [5], [0]], [[5], [0], [1]], [[0], [1], [2]]]