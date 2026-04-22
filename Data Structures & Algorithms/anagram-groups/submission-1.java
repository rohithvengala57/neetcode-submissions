class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for(String str: strs){
            int[] l = new int[26];
            for(char i: str.toCharArray()){
                l[i - 'a']++;
            }
            String key = Arrays.toString(l);
            map.putIfAbsent(key, new ArrayList<>());
            map.get(key).add(str);
        }
        return new ArrayList(map.values());
    }
}
