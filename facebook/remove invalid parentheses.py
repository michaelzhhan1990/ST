import collections
def calc_Mistake(s):
    a=0
    b=0
    # b is the mistake when ) is more
    # a is the mistake when ( is more
    for c in s:
        a+={'(':1,')':-1}.get(c,0)
        b+=a<0
        a=max(a,0)
    return a+b

def dfs_helper(s,visited):
    numMistake=calc_Mistake(s)
    if numMistake ==0:
        return [s]
    ans=[]
    for index in xrange(0,len(s)):
        if s[index] in ('(',')'):
            new_s=s[:index]+s[index+1:]
            if new_s not in visited:
                visited.add(new_s)
                if calc_Mistake(new_s) <=numMistake: # reduce mistake
                    ans.extend(dfs_helper(new_s,visited))
    return ans

def dfs_helper1(s,visited,numMistake):
    ans=[]
    for index in xrange(0,len(s)):
        if s[index] in ('(',')'):
            new_s=s[:index]+s[index+1:]
            if new_s not in visited:
                visited.add(new_s)
                new_mistakes=calc_Mistake(new_s)
                if new_mistakes==0:
                    ans.append(new_s)
                else:
                    if new_mistakes <= numMistake:
                        ans.extend(dfs_helper1(new_s,visited,new_mistakes))
    return ans

def dfs(s):
    num_mistake=calc_Mistake(s)
    if num_mistake==0:
        return [s]
    visited=set([s])
    return dfs_helper1(s,visited,num_mistake)


def bfs(s):
    mi = calc_Mistake(s)
    if mi == 0:
        return [s]
    ans=[]
    visited=set([s])
    queue=collections.deque([s])
    while queue:
        t = queue.popleft()
        for x in range(len(t)):
            if t[x] not in ('(', ')'):
                continue
            ns = t[:x] + t[x + 1:]
            if ns not in visited:
                num_mistake=calc_Mistake(ns)
                if num_mistake <= mi:
                    if num_mistake!=0:
                        queue.append(ns)
                    else:
                        ans.append(ns)
                    mi=num_mistake

                visited.add(ns)
    return ans


s=['()())()','(a)())()',')(','x(']
s1=['x(']
s2=['))(()(','n']
print bfs(s2[1])
print dfs(s2[1])

'''
for i in s:
    print dfs(i)
    print bfs(i)
'''