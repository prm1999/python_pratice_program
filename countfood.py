class Solution:
    def countPairs(self) :
        #List = [(input().split(','))]
        List=[1,3,5,7,9]
        p = len(List)
        count = 0
        for i in List:
            for j in List:
                if (List[i] + List[j]) % 2 == 0:
                    count = +1
                else : break

        print(count)


if __name__ == '__main__':
    Solution().countPairs()

