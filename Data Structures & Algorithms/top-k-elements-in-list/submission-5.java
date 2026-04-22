class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int num: nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        List<Integer>[] bucket = new List[nums.length + 1];
        for(int num: map.keySet()){
            int count = map.get(num);
            if(bucket[count] == null){
                bucket[count] = new ArrayList<>();
            } 
            bucket[count].add(num);
        }
            int[] res = new int[k];
            int idx  = 0;
            for(int i = bucket.length - 1;i>=0 && idx<k; i--){
                if(bucket[i] != null){
                    for(int n: bucket[i]){
                        res[idx++] = n;
                        if(idx == k){
                            break;
                        }
                    }
                }
            }
        return res;
    }
}
