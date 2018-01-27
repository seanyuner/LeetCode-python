## [002 Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

**difficulty: medium**

**题目：**

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**examples：**

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

Output: 7 -> 0 -> 8

Explanation: 342 + 465 = 807.

---
**solution:**

1. 首先是对ListNode类的理解，类似链表，val和next方法

2. 遍历一遍是必须的，由于加法只有对应位相加，就只需O（n）

3. 加法的进位（carry）是比较关键的一点，注意判断循环时候，末位（最高位）相加可能等于10，因此*while l1 or l2 or carry*

4. 对node中不存在的加法元素，**既可**直接取零，**也可**判断跳过

5. 实测，开头增加判断是否有ListNode为空，速度比较快（难道test里面有很多空？？）；另外divmod（）也较手动慢一些。
