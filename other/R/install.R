# 设置全局镜像站（这里推荐清华大学镜像站，国内下载速度极快）
options(repos = c(CRAN = "https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))

# 1. 列出你需要的包
required_packages <- c("tidyverse", "data.table", "ggplot2", "sf", "caret","ggplot2","glmnet","igraph","lme4","lubridate","RCurl","reshape","RJSONIO","tm","here","XML")
# 2. 找出查漏补缺的包（找出在已安装列表中不存在的包）
missing_packages <- required_packages[!(required_packages %in% installed.packages()[,"Package"])]

# 3. 如果有缺失的包，就执行安装
if(length(missing_packages) > 0) {
  install.packages(missing_packages)
  print(paste("成功安装了以下包：", paste(missing_packages, collapse = ", ")))
} else {
  print("赞！所有需要的包都已安装完毕，无需重复安装。")
}