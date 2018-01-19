## [013 Roman to Integer](https://leetcode.com/problems/roman-to-integer/description/)

**difficulity:easy**

**题目：**

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.


**solution：**
1. [Roman numerals](http://en.wikipedia.org/wiki/Roman_numerals)

2. 简单规则（3999以内）：

   I. 基本字符：'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1
   
   II. the numeral I can be placed before V and X to make 4 units (IV) and 9 units (IX) respectively.
   
   III. the numeral X can be placed before L and C to make 40 (XL) and 90 (XC) respectively.
   
   IV. the numeral C can be placed before D and M to make 400 (CD) and 900 (CM) according to the same pattern.
   
3. 遍历一遍累加是必须的，用字典存储基本字符及对应阿拉伯数值

4. 特殊情况主要是4/9/40/90/400/900这种，如会出现XCIX（99）小数字在大数字左侧的情形

5. 两种方案，**可以**循环时遇到当前比右边小，减去当前值，**或者**全部相加，遇到当前值大于左边值，再减去两倍的左边值

6. 注意循环时候起止点，第一种最后一位无法比较，但可直接相加，第二种第一位无法比较，也可直接相加。（特殊情况不会出现在起止点）

7. 实际上，出现特殊位置的，只有1、10、100之类的数，可以将其用作判断标准
