# LeetCode

 记录LeetCode刷题情况

**2020.02.04**	回溯算法

| 编号 | 难度 |       题目       | 题解思路 | 执行结果      |
| :--: | :--: | :--------------: | :------- | :------------ |
| 401  | 简单 |    二进制手表    | 回溯算法 | 40 ms 13.2 MB |
| 784  | 简单 | 字母大小写全排列 | 回溯算法 | 64 ms 13.5 MB |

**2020.02.05**	数组

| 编号 | 难度 |      题目      | 题解思路                       | 执行结果                                     |
| :--: | :--: | :------------: | :----------------------------- | :------------------------------------------- |
|  1   | 简单 |    两数之和    | [1] 暴力法<br />[2] 两遍哈希表 | [1] 7608 ms 14.2 MB<br />[2] 56 ms   14.9 MB |
|  11  | 中等 | 盛最多水的容器 | [1] 暴力法<br />[2] 双指针     | [1] 超出时间限制<br />[2] 160 ms  27.1 MB    |
|  15  | 中等 |    三数之和    | 排序 遍历+双指针               | 736 ms  16.6 MB                              |
|  18  | 中等 |    四数之和    | 排序 双循环遍历+双指针         | 164 ms  13 MB                                |

**2020.02.06**	数组

| 编号 | 难度 |           题目            | 题解思路                        | 执行结果                                     |
| :--: | :--: | :-----------------------: | :------------------------------ | :------------------------------------------- |
|  4   | 困难 | 寻找两个有序数组的中位数  | 合并 排序                       | 128 ms  13.2 MB                              |
|  16  | 中等 |     最接近的三数之和      | 排序 遍历+双指针                | 100 ms  13.3 MB                              |
|  26  | 简单 |  删除排序数组中的重复项   | [1] 复制+遍历<br />[2] 快慢指针 | [1] 1164 ms 14.8 MB<br />[2] 148 ms  14.9 MB |
|  80  | 中等 | 删除排序数组中的重复项-ii | 快慢指针                        | 72 ms   13.2 MB                              |

**2020.02.07**	动态规划

| 编号 | 难度 |        题目        | 题解思路                                                     | 执行结果                                   |
| :--: | :--: | :----------------: | :----------------------------------------------------------- | :----------------------------------------- |
|  53  | 简单 |     最大子序和     | 动态规划                                                     | 80 ms   13.9 MB                            |
|  70  | 简单 |       爬楼梯       | [1] 动态规划（自顶向下，记忆化）<br />[2] 动态规划（自底向上） | [1] 36 ms   13 MB<br />[2] 24 ms   12.9 MB |
| 121  | 简单 | 买卖股票的最佳时机 | 动态规划（最长子序和思想）                                   | 64 ms   14.5 MB                            |

**2020.02.08**	动态规划

| 编号 | 难度 |         题目          | 题解思路                                                     | 执行结果                                    |
| :--: | :--: | :-------------------: | :----------------------------------------------------------- | :------------------------------------------ |
| 198  | 简单 |       打家劫舍        | [1] 动态规划（自顶向下，记忆化）<br /> [2] 动态规划（自底向上） | 36 ms   13.1 MB<br />32 ms   13.1 MB        |
| 303  | 简单 | 区域和检索-数组不可变 | [1] 动态规划（记忆化）<br />[2] 动态规划（提前计算）         | 404 ms  16.9 MB<br />164 ms  16.6 MB        |
|  5   | 中等 |     最长回文子串      | [1] 动态规划（区间规划）<br />[2] 中心扩散                   | [1] 4124 ms 21.6 MB<br />[2] 1596 ms 13.1MB |

**2020.02.09**	数学

| 编号 | 难度 |         题目          | 题解思路                                                 | 执行结果                                                     |
| :--: | :--: | :-------------------: | :------------------------------------------------------- | :----------------------------------------------------------- |
|  7   | 简单 |       整数反转        | [1] 字符串+列表<br />[2] 弹出和推入数字 & 溢出前进行检查 | [1] 28 ms   12.9 MB<br />[2] 36 ms   13.2 MB                 |
|  2   | 中等 | 两数相加 | 遍历链表                                                 | 76 ms 13.2 MB                                                |
|  9   | 简单 |     最长回文子串      | [1] 整数反转<br />[2] 反转一半整数<br />[3] 中心扩散法   | [1] 92 ms    13.1 MB<br />[2] 84 ms    13 MB<br />[3] 76 ms    13 MB |
| 8 | 中等 | 字符串转换整数-atoi | [1] 从头遍历<br />[2] 正则表达式 | [1] 36 ms    13.1 MB<br />[2] 48 ms    13.1 MB |

**2020.02.10** 	哈希表

| 编号 | 难度 |         题目         | 题解思路                                              | 执行结果                                                     |
| :--: | :--: | :------------------: | :---------------------------------------------------- | :----------------------------------------------------------- |
|  3   | 中等 | 无重复字符的最长子串 | [1] 动态规划<br />[2] 哈希表<br />[3] 滑动窗口+哈希表 | [1] 76 ms   13.4 MB<br />[2] 68 ms   13.2 MB<br />[3] 92 ms   13.2 MB |

**2020.02.11** 	哈希表

| 编号 | 难度 |    题目    | 题解思路                                          | 执行结果                                                     |
| :--: | :--: | :--------: | :------------------------------------------------ | :----------------------------------------------------------- |
|  36  | 中等 | 有效的数独 | [1] 暴力法 <br />[2] 纯哈希表<br />[3] 一次迭代法 | [1] 188 ms    13.1 MB<br />[2] 124 ms    13.2 MB<br />[3] 100 ms    12.8 MB |

**2020.02.12** 	哈希表

| 编号 | 难度 |       题目       | 题解思路                                               | 执行结果                                                     |
| :--: | :--: | :--------------: | :----------------------------------------------------- | :----------------------------------------------------------- |
|  49  | 中等 |  字母异位词分组  | [1] 排序字符串相等<br />[2] 字符计数相等               | [1] 104 ms   16.9 MB<br />[2] 120 ms   18.6 MB               |
|  94  | 中等 | 二叉树的中序遍历 | [1] 递归算法<br />[2] 基于栈的遍历<br />[3] 莫里斯遍历 | [1] 40 ms    13.1 MB<br />[2] 36 ms    13.2 MB<br />[3] 40 ms    13 MB |

**2020.02.13** 字符串

| 编号 | 难度 |    题目    | 题解思路 | 执行结果          |
| :--: | :--: | :--------: | :------- | :---------------- |
|  6   | 中等 | z-字形变换 | 遍历法   | 60 ms     13.2 MB |

**2020.02.14** 字符串

| 编号 | 难度 |      题目      | 题解思路          | 执行结果       |
| :--: | :--: | :------------: | :---------------- | :------------- |
|  12  | 中等 | 整数转罗马数字 | 贪心算法 + 哈希表 | 60 ms  13.2 MB |
|  13  | 简单 | 罗马数字转整数 | 哈希表            | 56 ms  13.2 MB |
|  14  | 简单 |  最长公共前缀  | 暴力法            | 56 ms  13.1 MB |

**2020.02.15** 树

| 编号 | 难度 |        题目         | 题解思路                              | 执行结果                                       |
| :--: | :--: | :-----------------: | :------------------------------------ | :--------------------------------------------- |
|  96  | 中等 |  不同的二叉搜索树   | [1] 递归算法+记忆化<br />[2] 动态规划 | [1] 40 ms    12.9 MB<br />[2] 28 ms    13.2 MB |
|  95  | 简单 | 不同的二叉搜索树-ii | 递归算法                              | 52 ms    14.3 MB                               |
|  62  | 简单 |      不同路径       | 动态规划                              | 40 ms    13.1 MB                               |

**2020.02.16** 树

| 编号 | 难度 |      题目      | 题解思路                                                     | 执行结果                                                     |
| :--: | :--: | :------------: | :----------------------------------------------------------- | :----------------------------------------------------------- |
|  98  | 中等 | 验证二叉搜索树 | [1] 递归算法+中序遍历<br />[2] 栈+中序遍历<br />[3] 递归算法+上下界<br />[4] 栈+上下界 | [1] 52 ms   16.3 MB<br />[2] 52 ms   15.2 MB<br />[3] 48 ms   15.5 MB<br />[4] 72 ms   15.4 MB |
| 100  | 简单 |    相同的树    | [1] 递归算法<br />[2] 迭代算法                               | [1] 32 ms    13 MB<br />[2] 36 ms    13.2 MB                 |
| 101  | 简单 |   对称二叉树   | [1] 递归算法<br />[2] 迭代算法                               | [1] 48 ms    13.3 MB<br />[2] 40 ms    13.3 MB               |

**2020.02.17** 深度优先搜索

| 编号 | 难度 |              题目              | 题解思路                                 | 执行结果                                         |
| :--: | :--: | :----------------------------: | :--------------------------------------- | :----------------------------------------------- |
| 104  | 简单 |        二叉树的最大深度        | [1] 递归算法<br />[2] 迭代算法           | [1] 32 ms    14.5 MB<br />[2] 48 ms    14.2 MB   |
| 105  | 中等 | 从前序与中序遍历序列构造二叉树 | 递归算法                                 | 156 ms   51.6 MB                                 |
| 106  | 中等 | 从中序与后序遍历序列构造二叉树 | 递归算法                                 | 212 ms   51.8 MB                                 |
| 108  | 简单 |   将有序数组转换为二叉搜索树   | 递归算法                                 | 72 ms     15.3 MB                                |
| 109  | 中等 |     有序链表转换二叉搜索树     | [1] 递归+转成数组<br />[2] 递归+快慢指针 | [1] 156 ms    19.3 MB<br />[2] 124 ms    16.6 MB |

**2020.02.18** 深度优先搜索

| 编号 | 难度 |       题目       | 题解思路                                               | 执行结果                                       |
| :--: | :--: | :--------------: | :----------------------------------------------------- | :--------------------------------------------- |
| 110  | 简单 |    平衡二叉树    | [1] 递归算法（自顶向下）<br />[2] 递归算法（自底向上） | [1] 68 ms  16.7 MB<br />[2] 48 ms  17 MB       |
| 111  | 简单 | 二叉树的最小深度 | [1] 递归算法<br />[2] 迭代算法                         | [1] 80 ms    14.9 MB<br />[2] 44 ms    14.1 MB |
| 112  | 简单 |     路径总和     | [1] 递归算法<br />[2] 迭代算法                         | [1] 40 ms    14.8 MB<br />[2] 44 ms    14.9 MB |
| 113  | 中等 |   路径总和-ii    | 迭代算法                                               | 48 ms    14 MB                                 |

**2020.02.19** 二分查找

| 编号 | 难度 |     题目     | 题解思路  | 执行结果         |
| :--: | :--: | :----------: | :-------- | :--------------- |
|  29  | 中等 |   两数相除   | 移位+减法 | 152 ms  29 MB    |
|  35  | 简单 | 搜索插入位置 | 二分查找  | 116 ms   29.9 MB |

**2020.02.21** 二分查找

| 编号 | 难度 |                    题目                    | 题解思路                                           | 执行结果                                       |
| :--: | :--: | :----------------------------------------: | :------------------------------------------------- | :--------------------------------------------- |
|  33  | 中等 |              搜索旋转排序数组              | 二分查找有序部分                                   | 168 ms   29 MB                                 |
|  34  | 中等 | 在排序数组中查找元素的第一个和最后一个位置 | [1] 二分查找<br />[2] 二分查找的变形               | [1] 164 ms   29.9 MB<br />[2] 176 ms   29.5 MB |
|  50  | 中等 |                  pow-x-n                   | [1] 快速幂算法（递归）<br />[2] 快速幂算法（迭代） | [1] 140 ms  29.1 MB<br />[2] 112 ms  29.2 MB   |
|  69  | 简单 |                 x-的平方根                 | 二分查找                                           | 108 ms   29.1 MB                               |

**2020.02.22** 贪心算法

| 编号 | 难度 |         题目          | 题解思路                                       | 执行结果                                                     |
| :--: | :--: | :-------------------: | :--------------------------------------------- | :----------------------------------------------------------- |
| 122  | 简单 | 买卖股票的最佳时机-ii | [1] 动态规划<br />[2] 峰谷法<br />[3] 贪心算法 | [1] 72 ms    14.7 MB<br />[2] 64 ms    14.6 MB<br />[3] 116 ms  14.6 MB |

