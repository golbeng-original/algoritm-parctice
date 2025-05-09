
// 최대 슬라이등 윈도우
using System.Xml.XPath;

public class Program {

    public record Question(int[] nums, int k);

    public static void BookSolution(Question question) {

        (var nums, var k) = question;

        var result = new List<int>();

        var window = new Queue<int>();
        var currentMax = int.MinValue;
        for(var idx = 0 ; idx < nums.Length ; idx++) {
            var value = nums[idx];
            window.Enqueue(value);
            if( idx < k - 1 ) {
                continue;
            }

            // k만큼 Queue에 값이 차 있어야 한다.
            if(currentMax == int.MinValue) {
                currentMax = window.Max();
            }
            else if(value > currentMax) {
                currentMax = value;
            }

            result.Add(currentMax);

            // 최대 값이 queue에서 빠져 나왔으면, 현재 최대값 초기화
            if( currentMax == window.Dequeue()) {
                currentMax = int.MinValue;
            }
        }

        Console.WriteLine($"[{string.Join(", ", result)}]");
    }

    public static void MySolution(Question question) {

        var result = new List<int>();

        var nums = question.nums;
        for(var idx = 0 ; idx < nums.Length - question.k + 1 ; idx++) {
            var subNums = nums[idx..(idx + question.k)];

            result.Add(subNums.Max());
        }

        Console.WriteLine($"[{string.Join(", ", result)}]");
    }

    public static void Main(string[] args) {
        var questions = new List<Question>() {
            new Question(
                nums: [1,3,-1,-3,5,4,6,7],
                k: 3
            )
        };

        foreach(var question in questions) {
            //MySolution(question);
            BookSolution(question);
        }
    }
}