import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> mp = new HashMap<String, List<String>>();
        for (String str : strs) {
            char[] ch = str.toCharArray();
            Arrays.sort(ch);
            String key = new String(ch);
            if (!mp.containsKey(key)) {
                mp.put(key, new ArrayList<String>());
            }
            mp.get(key).add(str);
        }
        List<List<String>> list = new ArrayList<>();
        for (List<String> ls : mp.values()) {
            list.add(ls);
        }
        return list;
    }

    public static void main(String arg[]) {
        String[] matrix = new String[] { "eat", "tea", "tan", "ate", "nat", "bat" };
        List<List<String>> res = (new Solution()).groupAnagrams(matrix);
        System.out.println(res);
    }
}
