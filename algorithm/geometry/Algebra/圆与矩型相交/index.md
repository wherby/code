#


## 

https://leetcode.cn/problems/check-if-the-rectangle-corner-is-reachable/solutions/2981351/python3javacgotypescript-yi-ti-yi-jie-df-l8nu/?envType=daily-question&envId=2024-11-08
这里分了几步求相交情况
1.圆与端点相交
2.圆与两部分边界相交，并且需要圆心在矩形的延展区域内/ 圆心在矩形延展区域外在端点相交已经计算 （并且圆心坐标大于0）
3.圆与圆相交，并且圆与圆的重叠区域在矩形内



## 如果圆心坐标没有限制，求圆是否在矩阵内？
分两种情况：
1.圆心到4条边的距离小于r,并且圆心在矩形的投影下
2.四角端点在园内（这里包含了圆心在矩形投影外的情况）


https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line


https://stackoverflow.com/questions/849211/shortest-distance-between-a-point-and-a-line-segment/53176074
```javascript
function pDistance(x, y, x1, y1, x2, y2) {

  var A = x - x1;
  var B = y - y1;
  var C = x2 - x1;
  var D = y2 - y1;

  var dot = A * C + B * D;
  var len_sq = C * C + D * D;
  var param = -1;
  if (len_sq != 0) //in case of 0 length line
      param = dot / len_sq;

  var xx, yy;

  if (param < 0) {
    xx = x1;
    yy = y1;
  }
  else if (param > 1) {
    xx = x2;
    yy = y2;
  }
  else {
    xx = x1 + param * C;
    yy = y1 + param * D;
  }

  var dx = x - xx;
  var dy = y - yy;
  return Math.sqrt(dx * dx + dy * dy);
}

```