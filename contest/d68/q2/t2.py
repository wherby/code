class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        n = len(recipes)
        res = set()
        dic = {}
        for s in supplies:
            dic[s] = 1
        for x in range(n):
            for j in range(n):
                r,i = recipes[j],ingredients[j]
                if r in res:
                    continue
                isG = True
                for a in i:
                    if a not in dic:
                        isG =False
                if isG:
                    dic[r] =1
                    res.add(r)
        return list(res)

re=Solution().findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast"])
print(re)