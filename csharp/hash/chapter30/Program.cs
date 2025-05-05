
// 중복 문자 없는 가장 긴 부분 문자열
public partial class Program {

    public static void MySolution(string question) {

        var used = new Dictionary<char, int>();
        var maxLength = 0;
        var start = 0;

        for(var idx = 0 ; idx < question.Length ; idx++ ) {
            var ch = question[idx];

            if( used.ContainsKey(ch) && start <= used[ch]) {
                start = used[ch] + 1;
            }
            else {
                maxLength = Math.Max(maxLength, idx - start + 1);
            }

            used[ch] = idx;
        }

        Console.WriteLine(maxLength);
    }

    public static void WindowSlide(string question) {

        var used = new Dictionary<char, int>();
        var start = 0;
        var maxLength = 0;

        for(var idx = 0 ; idx < question.Length ; idx++) {
            var ch = question[idx];

            if( used.ContainsKey(ch) && start <= used[ch] ) {
                start = used[ch] + 1;
            }
            else {
                maxLength = Math.Max(maxLength, idx - start + 1 );
            }

            used[ch] = idx;
        }

        Console.WriteLine(maxLength);

    }

    public static void Main(string[] args) {

        var questions = new string[] {
            "abcabcbb", // abc, 3
            "bbbbb", // b, 1
            "pwwkew", // wke, 3
        };

        foreach(var question in questions) {
            Console.WriteLine($"{question}");
            MySolution(question);
            //WindowSlide(question);
        }
    }
}