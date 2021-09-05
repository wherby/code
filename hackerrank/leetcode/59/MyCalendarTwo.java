import java.util.*;
public class MyCalendarTwo {

    private List<int[]> list = new ArrayList<>();
    
    public boolean book(int start, int end) {
        MyCalendar c = new MyCalendar();
        for (int[] i : list) {
            if (i[0] < start && i[1] > start) {
                if (!c.book(start, i[1])) {
                    return false;
                }
            } else if (i[0] >= start && i[0] < end) {
                if (!c.book(i[0], Math.min(i[1], end))) {
                    return false;
                }
            }
        }
        list.add(new int[] {start, end});
        for(int [] i :list){System.out.println(Arrays.toString(i));}
        
        return true;
    }
    
    private class MyCalendar {

        TreeMap<Integer, Integer> tm = new TreeMap<>();
        
        public boolean book(int start, int end) {
            for (Map.Entry<Integer, Integer> entry : tm.entrySet()) {
                System.out.println("Key: " + entry.getKey() + ". Value: " + entry.getValue());
                }
            Integer i = tm.lowerKey(end);
            if (i != null && i >= start) {
                return false;
            }
            i = tm.lowerKey(start);
            if (i != null && tm.get(i) > start) {
                return false;
            }
            tm.put(start, end);

            return true;
        }
    }

     public static void main(String[] args) {

        MyCalendarTwo my =new  MyCalendarTwo();
        System.out.println(my.book(10, 20)); // returns true
  System.out.println(my.book(50, 60)); // returns true
 System.out.println(my.book(10, 40)); // returns true
 System.out.println(my.book(5, 15)); // returns false
 System.out.println(my.book(5, 10)); // returns true
 System.out.println(my.book(25, 55));    
        System.out.println("list");
           System.out.println("Hello World!");
     }
}