from collections import defaultdict
class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        n = len(messages)
        dic =defaultdict(int)
        mx = 0
        users=[]
        for i in range(n):
            k = len(messages[i].split(" "))
            dic[senders[i]] +=k
            if dic[senders[i]]> mx:
                users=[senders[i]]
                mx = dic[senders[i]]
            elif dic[senders[i]] ==mx:
                users.append(senders[i])
        users.sort()
        return users[-1]

re =Solution().largestWordCount(messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"])
print(re)