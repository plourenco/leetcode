
/**
 * 88. Merge Sorted Array
 * https://leetcode.com/problems/merge-sorted-array
 */
import java.util.ArrayList;
import java.util.Arrays;

class MergeSortedArray {
    public static void main(String[] args) throws Exception {
        var obj = new MergeSortedArray();
        int[] nums1 = { 4, 5, 6, 0, 0, 0 };
        int m = 3;
        int[] nums2 = { 1, 2, 3 };
        int n = 3;
        obj.merge(nums1, m, nums2, n);
    }

    /**
     * Slower speed but optimal memory
     * 
     * Time complexity: O(m + n) + O(n * (2m + n - 1) / 2) = O(n^2)
     * (similar to the sum of 1 to infinity series)
     * 
     * m = 3, n = 3
     * i = 3 to 6; 3, 4, 5
     * i = 3, j runs 3 times
     * i = 4, j runs 4 times
     * i = 5, j runs 5 times
     * number of terms = n
     * mid term = m + (m + n) / 2
     * S = n * (m + m + n - 1) / 2 (using the arithmetic series formula)
     */
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (var i = m; i < m + n; i++) { // O(m + n)
            nums1[i] = nums2[i - m];
        }
        for (var i = m; i < m + n; i++) { // O(n)
            var j = i;
            while (j > 0 && nums1[j] < nums1[j - 1]) { // best O(m) worst O(m + n)
                // swap them without a third var by using a sum
                nums1[j] = nums1[j - 1] + nums1[j];
                nums1[j - 1] = nums1[j] - nums1[j - 1];
                nums1[j] = nums1[j] - nums1[j - 1];
                j--;
            }
        }
        System.out.println(Arrays.toString(nums1));
    }

    /**
     * Faster but with a higher memory usage
     * Time complexity = O(n + m)
     */
    public void merge2(int[] nums1, int m, int[] nums2, int n) {
        var i = 0;
        var j = 0;
        var list = new ArrayList<Integer>();
        while (i + j < n + m) {
            if (j == n || (i < m && nums1[i] < nums2[j])) {
                list.add(nums1[i++]);
            } else {
                list.add(nums2[j++]);
            }
        }
        for (i = 0; i < n + m; i++) {
            nums1[i] = list.get(i);
        }
        System.out.println(list);
    }
}
