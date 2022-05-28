# 跳马问题
a,b,c,d=map(int,input().split())
p=[[1,2],[2,1],[-1,2],[-1,-2],[1,-2],[-2,1],[-2,-1],[2,-1]]#每一步可以走的路径
minstep=float('inf')#初始化最短路径
v=[[0 for i in range(9)]for j in range(9)]#用二维数组记录棋盘上的点是否已经走过
path=[[a,b]]#存放马走到终点的单条路经
res=[]#存放马走到终点的多条路径
def huisu(x,y,step):
    global minstep
    if step>=minstep:#如果走的步数已经大于最小步数，则返回，换一条路径继续搜索
        return
    if x==c and y==d:#到达终点，更新最小步数
        minstep=step
        res.append(path.copy())
        return

    for i in range(8):
        nx=x+p[i][0]
        ny=y+p[i][1]#下一步走到的点
        if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
            if v[nx][ny]==1:#可以走的路径有[-2,-1],有负数，因此有些节点可能会重复走到，会无限循环，要跳过这些重复的点
                continue
            v[nx][ny]=1
            path.append([nx,ny])
            huisu(nx,ny,step+1)
            path.pop()
            v[nx][ny]=0
            x=nx-p[i][0]
            y=ny-p[i][1]#回溯，撤销处理结果
huisu(a,b,0)
print("最短步数为："+str(minstep))
# print(res)
# 输出最短路径
for r in res:
    if len(r)-1==minstep:
        print("最短路径为：")
        print(r)
