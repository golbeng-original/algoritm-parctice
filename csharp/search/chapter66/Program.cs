
// 회전 정렬된 배열 검색
public class Program {
    
    public record Question(int target, int[] nums);

    public static void MySolution(Question question) {

        var nums = question.nums;

        // 최소값 찾기??
        var left = 0;
        var right = nums.Length - 1;
        while(left < right) {
            var mid = (right + left) / 2;

            if(nums[mid] > nums[right]) {
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }

        var pivot = left;
        (left, right) = (0, nums.Length - 1);
        var midPivot = 0;
        while(left <= right) {

            var mid = (right + left) / 2;
            midPivot = (mid + pivot) % nums.Length;

            if( nums[midPivot] < question.target ) {
                left = mid + 1;
            }
            else if(nums[midPivot] > question.target) {
                right = mid - 1;
            }
            else {
                break;
            }
        }

        Console.WriteLine(midPivot);

    }

    public static void Main(string[] args) {

        var question = new Question(
            target: 1,
            nums: [4,5,6,7,0,1,2]
        );

        MySolution(question);

    }
}