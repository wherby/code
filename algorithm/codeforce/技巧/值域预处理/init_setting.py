import sys
from pathlib import Path

# 获取项目根目录
current_file = Path(__file__).resolve()
project_root = current_file.parents[2]  # 上两级
sys.path.insert(0, str(project_root))  # 使用insert(0, ...)确保优先搜索

print(f"Added to path: {project_root}")