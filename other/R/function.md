





# 合并左右数据源 join?
```R
all.sightings<-merge(states.dates,sightings.counts,by.x=c("s","date.strings"),
 by.y=c("USState","YearMonth"),all=TRUE)
```