# 1233. Remove Sub-Folders from the Filesystem
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/?envType=daily-question&envId=2024-10-25

# def getSubStringUpNotInclusive(x, i): 
#     res = ""
#     for j in range(i): 
#         res += x[j]
#     return res


# Put all strings in the folder in set for O(1) lookups. 
# then for each string in the folder, call a subroutine 
# called isSubFolderInFolders that checks whether that 
# current folder string has a subfolder in the set. If
# it does not, append that string to the result. 

# isSubFolderInFolders works by checking the string from 
# back to front. If you see a slash, check if the string
# up to that slash is in the folders. If so return True. 
# If not, keep checking smaller-length folders. 
# This subroutine takes O(n) time for n length of string

# Time: O(mn) for m strings in folder with max length n
# Space: O(mn) for m strings in folder with max length n


# def isSubFolderInFolders(folderPath, folders): 
#     for i in range(len(folderPath) - 1, -1, -1): 
#         if folderPath[i] == "/" and folderPath[:i] in folders: return True
#     return False

# class Solution:
#     def removeSubfolders(self, folder: list[str]) -> list[str]:
#         folders = set(folder)
#         res = []
#         for folderPath in folder: 
#             if not isSubFolderInFolders(folderPath, folders): 
#                 res.append(folderPath)
#         return res
    


def getSubStringUpNotInclusive(string, i): 
    res = ""
    for j in range(i): 
        res += string[j]
    return res

def isSubFolderInFolders(folderPath, folders): 
    for i in range(len(folderPath) - 1, -1, -1): 
        if folderPath[i] == "/" and getSubStringUpNotInclusive(folderPath, i) in folders: return True
    return False

class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folders = set(folder)
        res = []
        for folderPath in folder: 
            if not isSubFolderInFolders(folderPath, folders): 
                res.append(folderPath)
        return res
    

s = Solution()

folder = ["/1/2/3", "/1", "/1/2"]
# # ["/1"]


# folder = ["1/2/3", "/2/3", "/3/4"]
# # ["1/2/3", "/2/3", "/3/4"]

# folder = ["/1/2/3", "/1/2/3/4", "/2/3/4", "/2/3"]
# # ["/1/2/3", "/2/3"]


print(s.removeSubfolders(folder))