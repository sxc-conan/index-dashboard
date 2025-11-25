<!-- c6977a9d-1eb0-402b-b477-4b59a0198aca 1c3350db-aa92-4c94-a314-771fcce6c333 -->
# 月度枢轴点样式优化

## 修改内容

将月度枢轴点的样式从虚线改为实线，并加粗线条。

## 具体修改

**文件：** `/Users/shenxuechao_1/指数狂飙/web/index.html`

**位置：** `addMonthlyPivots` 函数中的数据集配置（约第1894-1895行）

**修改项：**

1. 将 `borderDash: [10, 5] `改为 `borderDash: []` 或删除该属性（实线）
2. 将 `borderWidth: 2` 改为 `borderWidth: 3`（加粗）

**修改后的代码片段：**

```javascript
chart.data.datasets.push({
    // ... 其他配置保持不变 ...
    borderColor: color,
    borderWidth: 3,           // 从2改为3，加粗
    // borderDash: [10, 5],   // 删除或改为 []，实现实线效果
    pointRadius: 0,
    // ... 其他配置保持不变 ...
});
```

## 预期效果

- 月度枢轴点显示为实线（不再是虚线）
- 线条更粗（3px，比之前的2px更明显）
- 颜色保持不变（P轴橙色，R轴蓝色，S轴红色）

### To-dos

- [ ] 为枢轴点数据集添加pivotType、pivotLabel、isPivot字段
- [ ] 自定义tooltip显示逻辑，展开完整标签
- [ ] 优化tooltip过滤逻辑，只显示有效范围内的枢轴点
- [ ] 测试tooltip显示效果