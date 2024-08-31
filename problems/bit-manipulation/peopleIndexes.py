from collections import defaultdict

def peopleIndexes1(favoriteCompanies: list[list[str]]) -> list[int]:
    lookup = defaultdict(set)
    for i, companyList in enumerate(favoriteCompanies): 
        lookup[i] = set(companyList)

    res = []
    for i, iCompanyList in enumerate(favoriteCompanies): 
        isSubset = False
        for j, _ in enumerate(favoriteCompanies):
            count = 0
            if i == j: continue
            for iCompany in iCompanyList: 
                if iCompany in lookup[j]: 
                    count += 1
            if count == len(iCompanyList): 
                isSubset = True 
                # print("issubset = true", i, j)
                break
        # print(i, isSubset, count)
        if not isSubset: res.append(i)
    return res

# a binary representation
# how do you convert a list into binary easily? 
def peopleIndexes(favoriteCompanies: list[list[str]]) -> list[int]:
    # build array of all non dupes
    allCompanies = set()
    for x in favoriteCompanies: 
        for y in x: 
            allCompanies.add(y)
    
    allCompanies = list(allCompanies)
    companyToIndex = {}
    for i, company in enumerate(allCompanies):
        companyToIndex[company] = i 
    bFavs = []

    for fav in favoriteCompanies: 
        binFavs = ["0"]*len(allCompanies)
        for company in fav: 
            idx = companyToIndex[company]
            binFavs[idx] = "1"
        binFavs = "".join(binFavs)
        bFavs.append(int(binFavs, 2))
    res = []
    for i, bFav1 in enumerate(bFavs): 
        isSubset = False
        for j, bFav2 in enumerate(bFavs): 
            if i == j: continue

            if bFav1 & bFav2 == bFav1: 
                isSubset = True
                break 
        if not isSubset: res.append(i)

    return res


favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]


print(peopleIndexes(favoriteCompanies))

# print(bin(3))
# print(int("11", 2))

print(3 & 6)