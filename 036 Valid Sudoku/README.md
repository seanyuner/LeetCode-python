## [036 Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)

**difficulty: medium**

**题目：**

Determine if a Sudoku is valid, according to: [Sudoku Puzzles - The Rules](http://sudoku.com.au/TheRules.aspx).

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

![sudoku.png](https://github.com/seanyuner/LeetCode-python/blob/master/036%20Valid%20Sudoku/sudoku.png)
A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

---
**solution:**
1. 判断数独有效（不等于有解！），主要三个原则：行、列、块均满足1到9不重复，对于空白处可直接跳过
2. Solution1，最直观的思考，分别判断三种，将每类9个组成数组，判断转换set后长度是否变化
3. Solution2，将数组换成字典结构，可以直接判断数字是否存在字典中，相比上述有较大提高
4. Solution3，对三类均构造哈希表，遍历一次整个数独，注意对块的转换这一技巧
5. 针对Solution2的改进，将三种情况均统一用一个函数来判断(但是效果并没有提升，尴尬。有意思的是，把相同结果扔到python3运行，则直接超过100%，这种满屏黄色的感觉真的是爽的不行啊！由此可见，leetcode里面还是2是主流吧。)
