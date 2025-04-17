import logging

# 其他常用格式化字段
# 字段	说明
# %(name)s	记录器名称
# %(filename)s	文件名
# %(lineno)d	行号（数字）
# %(funcName)s	函数名
# %(process)d	进程ID
# %(thread)d	线程ID

def print_vs_logging():
    logging.debug("debug info")
    logging.info("info")
    logging.error("Ewwor ..")


def main():
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level= level,format=fmt)

main()
print_vs_logging()