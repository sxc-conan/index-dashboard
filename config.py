"""
配置文件 - 指数狂飙项目
"""

# 图表配置
CHART_CONFIG = {
    # 图表尺寸（英寸）
    'figure_width': 31.5,  # 标准宽度
    'figure_height': 47.25,  # 标准高度的1.5倍
    
    # 颜色配置
    'colors': {
        'weekly': 'blue',      # 周度数据颜色
        'monthly': 'black',    # 月度数据颜色
        'pivot': 'red',        # P轴颜色
        'border': 'black',     # 边框颜色
    },
    
    # 线条样式
    'line_styles': {
        'weekly': '--',   # 虚线
        'monthly': '-',   # 实线
    },
    
    # 字体配置
    'font': {
        'size': 12,
        'weight': 'bold',
        'family': 'sans-serif',
    },
    
    # 标签配置
    'label': {
        'min_distance_ratio': 0.15,  # 最小间距比例（数值范围的15%）
    },
}

# 数据目录
DATA_DIR = 'data'
CHARTS_DIR = 'charts'

# 枢轴点标签
PIVOT_LABELS = ['R3', 'R2', 'R1', 'P', 'S1', 'S2', 'S3']


