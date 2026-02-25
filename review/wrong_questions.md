---
title: 错题本
last_updated: 2026-02-25
---

# 错题本

记录做错的题目和易错点，定期复习。

## 使用说明

每次做错题目时，记录以下信息：

- **题目**：题目名称和链接
- **日期**：做错的日期
- **错误原因**：为什么做错
- **知识点**：涉及的知识点
- **复习次数**：复习了几次
- **掌握状态**：是否已掌握

## 错题记录

### 示例

#### [15. 三数之和](../problems/lc/0015_three_sum.md)

- **日期**：2026-02-25
- **错误原因**：
  - 没有处理去重逻辑
  - 忘记跳过重复元素
- **知识点**：双指针、去重
- **易错点**：
  - 需要在三个地方去重：外层循环、左指针、右指针
  - 跳过重复元素的条件是 `i > 0 && nums[i] == nums[i-1]`
- **复习次数**：0
- **掌握状态**：❌ 未掌握

**正确做法：**

```python
def threeSum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # 去重：跳过重复元素
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # 去重
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result
```

---

## 错题分类

### 数组

- TBD

### 树

- TBD

### 图

- TBD

### 动态规划

- TBD

## 复习计划

### 本周复习（Week 9, 2026）

- [ ] 三数之和
- [ ] 二叉树的层序遍历

### 下周复习

- [ ] TBD

## 易错点总结

### 1. 去重问题

- 排序后使用 `i > 0 && arr[i] == arr[i-1]` 跳过重复
- 注意条件是 `i > 0`，不是 `i > start`

### 2. 边界条件

- 空数组、单元素数组
- 索引越界检查

### 3. 时间复杂度

- 注意嵌套循环的复杂度
- 优化到最优解

## 复习记录

| 日期 | 题目 | 结果 | 备注 |
|------|------|------|------|
| 2026-02-25 | 三数之和 | ❌ | 去重问题 |
| | | | |

## 统计

- **总错题数**：1
- **已掌握**：0
- **未掌握**：1
- **掌握率**：0%
