
/**
 * 18. 4Sum
 * https://leetcode.com/problems/4sum/
 */
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class P18_FourSum {
    public static void main(String[] args) throws Exception {
        var obj = new P18_FourSum();
        int[] input = { 1000000000, 1000000000, 1000000000, 1000000000 };
        System.out.println(obj.fourSum(input, -294967296));
    }

    public List<List<Integer>> fourSum(int[] nums, int target) {
        var list = new ArrayList<List<Integer>>();
        var sorted = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sorted);
        for (var i = 0; i < sorted.length; i++) {
            for (var j = i + 1; j < sorted.length; j++) {
                if (i > 0 && sorted[i] == sorted[i - 1] || j > i + 1 && sorted[j] == sorted[j - 1]) {
                    continue;
                }
                var left = j + 1;
                var right = sorted.length - 1;
                while (left < right) {
                    var sum = Arrays.stream(new int[] { sorted[left], sorted[right], sorted[i], sorted[j] })
                            .mapToObj(BigInteger::valueOf)
                            .reduce(BigInteger.ZERO, BigInteger::add);
                    if (sum.equals(BigInteger.valueOf(target))) {
                        list.add(Arrays.asList(sorted[i], sorted[j], sorted[left], sorted[right]));
                        left++;
                        right--;
                        while (left < right && sorted[left] == sorted[left - 1]) {
                            left++;
                        }
                        while (left < right && sorted[right] == sorted[right + 1]) {
                            right--;
                        }
                    } else if (sum.compareTo(BigInteger.valueOf(target)) < 0) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        return list;
    }
}
