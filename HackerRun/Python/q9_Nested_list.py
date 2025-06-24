# Prepare Python Basic Data Types Nested Lists
if __name__ == '__main__':
    names=[]
    scores=[]
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        names.append(name)
        scores.append(score)
    #Remove duplication 
    score_list=list(set(scores))
    #Sorting in ascending order
    score_list.sort()
    #Geting the seconding lowest score
    second_lowest = score_list[1]
    #list comprehension
    out = [i[0] for i in records if i[1] == second_lowest]
    
    #sorting alphabatecally
    out.sort()
    #printing the output
    for i in out:
        print(i)
    
    
    
    
        