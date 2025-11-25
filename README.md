# 指数狂飙 📈

一个强大的金融指数分析工具，专注于枢轴点（Pivot Points）分析和可视化。

## 功能特性

- 📊 **枢轴点图表生成**：自动生成专业的枢轴点位图表
- 📈 **多时间周期分析**：支持周度和月度数据对比
- 🎨 **精美可视化**：高质量的图表输出，支持多指数纵向排列
- 🔧 **灵活配置**：可自定义图表样式和数据源

## 项目结构

```
指数狂飙/
├── data/           # 数据文件目录
├── charts/         # 图表输出目录
├── web/            # Web界面文件
│   ├── index.html  # 实时指数看板（含枢轴点）
│   └── dashboard-simple.html  # 简单仪表板
├── utils/          # 工具函数
│   └── pivot_chart.py  # 枢轴点图表生成器
├── main.py         # 主程序入口
├── start_server.py # Web服务器启动脚本
├── config.py       # 配置文件
├── requirements.txt # 项目依赖
└── README.md       # 项目说明
```

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 启动Web指数看板

```bash
python start_server.py
```

服务器启动后会自动打开浏览器，显示实时指数看板。

**功能特点：**
- 📊 实时展示全球主要指数（纳斯达克、标普500、恒生指数等）
- 📈 支持多个月度和周度枢轴点位显示
- 🎨 交互式图表，支持缩放和平移
- 🔄 智能数据更新（开盘时间5分钟，盘后1小时）
- 🌐 多数据源支持（Yahoo Finance、新浪财经等）
- 🔍 市场分类筛选（港股、美股、A股）
- ⏱️ 灵活的时间范围调整
- 💾 自动数据缓存

**访问地址：**
- 完整看板：http://localhost:8888/index.html
- 简单版：http://localhost:8888/dashboard-simple.html

**可选CORS代理：** 如遇数据加载问题，可运行：
```bash
python web/cors_proxy.py
```

### 运行Python程序

```bash
python main.py
```

## 枢轴点图表说明

### 图表特点
- 纵向排列所有指数图表，每行一个
- 图表高度为标准的1.5倍
- 顶部显示总标题（如M11W1）
- 每个指数包含周度（蓝色虚线）和月度（黑色实线）数据
- P轴使用红色特殊标注
- 智能标签布局，避免重叠

### 数据格式

枢轴点数据数组顺序：`[R3, R2, R1, P, S1, S2, S3]`

- R3, R2, R1: 阻力位
- P: 枢轴点
- S1, S2, S3: 支撑位

## 📘 使用文档

### 新手入门

如果你是第一次使用，请查看 [快速开始指南](QUICKSTART.md)，只需三步即可启动！

### 详细文档

- **Web看板使用手册**: [web/README.md](web/README.md)
- **配置文件说明**: [config.py](config.py)
- **快速启动**: [QUICKSTART.md](QUICKSTART.md)

## 使用示例

### Web界面方式（推荐）

最简单的使用方式，只需运行：

```bash
python start_server.py
```

浏览器会自动打开，你可以：
- 查看实时指数数据
- 分析枢轴点位
- 切换不同市场
- 调整时间范围

### Python API方式

```python
from utils.pivot_chart import generate_pivot_chart

# 示例数据
data = {
    'title': 'M11W1',
    'indices': [
        {
            'name': '上证指数',
            'weekly': [3500, 3450, 3400, 3350, 3300, 3250, 3200],
            'monthly': [3550, 3480, 3420, 3370, 3280, 3220, 3150]
        },
        # 更多指数...
    ]
}

# 生成图表
generate_pivot_chart(data, output_path='charts/pivot_chart.png')
```

## 开发计划

- [x] 基础项目结构
- [x] Web界面（实时指数看板）
- [x] 枢轴点实时展示
- [x] 多数据源支持
- [ ] 数据导入功能
- [ ] 枢轴点计算算法
- [ ] 图表生成优化
- [ ] 批量处理功能

## 许可证

MIT License

## 作者

创建于 2025年11月


