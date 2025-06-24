#Printing runner-up score -- HackerRank question no. 8
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores= list(set(arr))
    unique_scores.sort(reverse=True) # sorting into descending order
    print(unique_scores[1]) #priting 2nd largest number for the runnerup