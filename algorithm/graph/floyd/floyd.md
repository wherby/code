# page 369 算法竞赛 进阶指南
https://github.com/lydrainbowcat/tedukuri/blob/master/%E9%85%8D%E5%A5%97%E5%85%89%E7%9B%98/%E6%AD%A3%E6%96%87%E5%8C%85%E5%90%AB%E7%9A%84%E7%A8%8B%E5%BA%8F%E7%89%87%E6%AE%B5/0x61%20shortest_path.cpp
// floyd求任意两点间最短路径
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);