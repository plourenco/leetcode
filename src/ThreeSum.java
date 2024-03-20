import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class ThreeSum {
    public static void main(String[] args) throws Exception {
        var obj = new ThreeSum();
        // int[] input = { 1, -1, -1, 0 };
        // int[] input = { 3, 0, -2, -1, 1, 2 };
        int[] input = { 1, -1, -1, 0 };
        System.out.println(obj.threeSum(input));
    }

    /**
     * Time complexity:
     * - n * log(n) + (n - 2) * (n * (n-1)/2)
     * - O(n^2)
     * 
     * @param nums
     * @return
     */
    public List<List<Integer>> threeSum(int[] nums) {
        var list = new ArrayList<List<Integer>>();
        var sorted = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sorted);
        for (var k = 0; k < sorted.length - 2; k++) {
            if (k > 0 && sorted[k] == sorted[k - 1]) {
                continue;
            }
            var i = k + 1;
            var j = sorted.length - 1;
            while (i < j) {
                var sum = sorted[i] + sorted[j];
                if (sum + sorted[k] == 0) {
                    list.add(Arrays.asList(sorted[k], sorted[i], sorted[j]));
                    i++;
                    j--;
                    while (i < j && sorted[i] == sorted[i - 1]) {
                        i++;
                    }
                    while (i < j && sorted[j] == sorted[j + 1]) {
                        j--;
                    }
                } else if (sum < -sorted[k]) {
                    i++;
                } else {
                    j--;
                }
            }
        }
        return list;
    }
}
