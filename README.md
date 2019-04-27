# LeetCode

| #    | Title                                                        | Solution                                                     | Tips | Difficulty |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- | ---------- |
| 1    | [Two Sum](https://leetcode.com/problems/two-sum/)            | [C++](https://github.com/fs302/LeetCode/blob/master/001-twoSum/twoSum.cpp) | 模拟 | Easy       |
| 2    | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers) | [C++](https://github.com/fs302/LeetCode/blob/master/002-addTwoNum/addTwoNum.cpp) | 模拟 | Medium     |
| 3    | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | [C++](https://github.com/fs302/LeetCode/blob/master/003-longestSubStr/solution_2.cpp) | 模拟 | Medium     |
| 4    | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) | [Python](https://github.com/fs302/LeetCode/blob/master/004-MedianArray/median_array.py) | 归并查找 | Hard |
| 5    | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Python](https://github.com/fs302/LeetCode/blob/master/005-longestPalindromicSubStr/lpss.py) | 贪心 | Medium |
| 6    | [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/) | [Python](https://github.com/fs302/LeetCode/blob/master/006-ZigZag/zigzag.py) | 模拟 | Medium |
| 7    | [Reverse Integer](https://leetcode.com/problems/reverse-integer) | [Python](https://github.com/fs302/LeetCode/blob/master/007-ReverseInt/reverse.py) | 模拟 | Easy       |
| 8    | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | [Python](https://github.com/fs302/LeetCode/blob/master/008-String2Int/string2int.py) | 模拟 | Easy       |

# ARTS

每周至少做一个leetcode的算法题、阅读并点评至少一篇英文技术文章、学习至少一个技术技巧、分享一篇有观点和思考的技术文章。（也就是Algorithm、Review、Tip、Share 简称 ARTS）

### 2019/03/18-2019/03/24

* Algorithm: Leetcode-007 [Python](https://github.com/fs302/LeetCode/blob/master/007-ReverseInt/reverse.py)
* Review：
* Tip：[《Python风格规范》](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/) 第一条：不要在行尾加分号, 也不要用分号将两条命令放在同一行.
* Share：[《CIKM 最佳论文是怎样炼成的》](https://dl.ccf.org.cn/institude/institudeDetail?id=4238083940370432&_ack=1) 这篇文章讲述了结合视觉和文本做搜索排序优化的新思路，经历了 CVPR、IJCAI 的拒稿后，最终被 CIKM 接收并且拿到最佳论文奖的历程。得到的启发是：一个新思路在被大家认可的过程中，是不断和外接碰撞，完善表达力的过程。其中重要的一环还是作为提出者要足够相信。

### 2019/03/25-2019/03/31

* Algorithm: LeetCode-004 [Python](https://github.com/fs302/LeetCode/blob/master/004-MedianArray/median_array.py)
* Review:[Finding insights with graph analytics](https://www.analyticbridge.datasciencecentral.com/profiles/blogs/finding-insights-with-graph-analytics) 介绍了如何用图分析的方法来帮助企业做决策，可看的地方主要在第一部分，对图分析方法做了分类。
  + Pattern matching algorithms 模式匹配算法
  + Traversal and pathfinding algorithms 遍历和路径查找算法，比如最短路径
  + Connectivity algorithms 连通性算法，比如强联通分量、查找攻击点
  + Community detection algorithms 社区检测算法，比如 Louvain、LPA
  + Centrality algorithms 中心性计算，比如 PageRank、Degree、Closeness、Betweenness
* Tip:
* Share:

### 2019/04/01-2019/04/07

* Algorithm: LeetCode-005 [Python](https://github.com/fs302/LeetCode/blob/master/005-longestPalindromicSubStr/lpss.py)
* Review: [User Identity Linkage across Online Social Networks](https://dl.acm.org/citation.cfm?doid=3068777.3068781) 文章从特征挖掘和模型选型两个角度概述了如何在两个社交网络上做用户同人映射的学术研究，时间截至2016年。其中特征挖掘主要包括 Profile、Content、Network 三方面，模型包括有监督的分类模型（如 SVM、RF、朴素贝叶斯）、半监督的标签传播和 Embedding，以及无监督的迭代模型。需要重点关注的特征包括：文本特征、位置特征、网络特征甚至是图片特征，其中特征的相似度计算也是研究的热点。常见的评价指标包括：准确率、召回率、精确率、AUC 等。 其中[18][62]是信息推荐，对 OneID/OneRelation 均适用。 [38][46] 可能对系统性架构有借鉴意义。 [47][53] 是利用位置信息做同人识别的例子。 [38][40] 是各种特征的集大成者。
* Tip: 学会在长周期的任务里用好“缓存”思想，能够帮助减少计算量、增加效率。
* Share: [李开复图灵奖推荐信曝光：AI时代里 Hinton是最值得嘉奖的人](https://news.cnblogs.com/n/623079/)

### 2019/04/08-2019/04/14

* Algorithm: LeetCode-006 [Python](https://github.com/fs302/LeetCode/blob/master/006-ZigZag/zigzag.py)
* Review: 
* Tip: 
* Share: 

### 2019/04/15-2019/04/21

* Algorithm: LeetCode-008 [Python](https://github.com/fs302/LeetCode/blob/master/008-String2Int/string2int.py)
* Review: [What's in a name]()
* Tip: 从科技发展史，更容易抽象出技术未来的方向。比如市场营销领域的 Targeting，最初是 household（电话、报纸），然后是 individual（手机、电脑），现在可以做得更多维度 households+individual+device（一个人可能有多台设备），从发展的角度去看会更清楚做什么更有价值。
* Share: [社交网络中的深度知识挖掘 ](http://www.sohu.com/a/122070840_468622) 这个 PPT 是关于社交网络的应用综述，有几个有意思的东西：一是构建社会的 RoadMap（User-Tie-Network），二是用社交网络数据来做性别预测和关系预测，三是网络中可以挖掘出一些关键角色（比如公司 Boss）或者意见领袖。

