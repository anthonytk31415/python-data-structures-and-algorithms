from typing import List 

# this is a dfs with cycle 


def findAllRecipes(recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    supplies = set(supplies)
    visited = {recipe: 0 for recipe in recipes} # item: 0 unprocessed, 1 processing, 2: cant make; 3: make
    indexes = {recipe: i for i, recipe in enumerate(recipes)}
            
    def do_failure(recipe):
        visited[recipe] = 2         
        return False
            
    def get_idx(recipe): 
        return indexes[recipe]
    
    def dfs(i):        
        recipe, ingredient_list = recipes[i], ingredients[i]
        visited[recipe] = 1
        
        for ingredient in ingredient_list: 
            if ingredient in supplies: 
                continue
            if ingredient not in visited or visited[ingredient] == 1 or visited[ingredient == 2]: 
                return do_failure(recipe)
            if visited[ingredient] == 3: 
                continue
            if visited[ingredient] == 0:
                j = get_idx(ingredient)
                if not dfs(j): 
                    return do_failure(recipe)
                continue                                

        visited[recipe] = 3
        return True
    
    for i in range(len(recipes)):         
        if visited[recipes[i]]==0: 
            dfs(i)
            
    return [x for x in visited.keys() if visited[x] == 3]