


// 부분 문자열이 포함된 최소 윈도우
public class Program {

    public record Question(string s, string t);

    public static void MySolution(Question question) {
        var targetChCount = question.t.GroupBy(e => e).ToDictionary(e => e.Key, e => e.Count());
        var windowCount = new Dictionary<char, int>();

        var s = question.s;
        (var start, var left, var right) = (0, 0, 0);
        var formed = 0;
        var required = targetChCount.Count;
        var minLength = int.MinValue;

        while( right < s.Length) {
            // 오른쪽 포인트 중가 부분
            var ch = s[right];
            if( windowCount.ContainsKey(ch) == true ) {
                windowCount[ch]++;
            }
            else {
                windowCount[ch] = 1;
            }

            if( targetChCount.ContainsKey(ch) && windowCount[ch] == targetChCount[ch]) {
                formed++;
            }

            // 모든 문자열 충족하기 전까지는 오른쪽 진행

            /// 모든 문자열이 충족 되면, 왼쪽으로 움직인다.
            while( left <= right && formed == required ) {
                var leftCh = s[left];

                //최소 길이 계산
                if( right - left + 1 < minLength) {
                    minLength = right - left + 1;
                    start = left;
                }

                // 왼쪽 문자 제거
                windowCount[leftCh]--;
                if( targetChCount.ContainsKey(leftCh) && windowCount[leftCh] < targetChCount[leftCh]) {
                    formed--;
                }

                left++;
            }

            right++;
        }

        if( minLength == int.MinValue) {
            Console.WriteLine("");
        }
        else {
            Console.WriteLine(s[start..(start+minLength)]);
        }
    }

    public static void MySolutionReview(Question question) {

        (var s, var t) = question;
        var targetCh = t.GroupBy(e => e).ToDictionary(e => e.Key, e => e.Count());
        var windowCh = new Dictionary<char, int>();

        var targetLength = t.Length;
        var findChLength = 0;
        var minLength = int.MaxValue;
        int start = 0, left = 0, right = 0;
        
        while(right < s.Length) {
            // 오른쪽 슬라이드 움직이기
            var ch = s[right];
            if( windowCh.ContainsKey(ch) == false ) {
                windowCh[ch] = 0;
            }
            windowCh[ch]++;

            if( targetCh.ContainsKey(ch) == true && targetCh[ch] == windowCh[ch]) {
                findChLength++;
            }

            while( left <= right && targetLength == findChLength) {
                var leftCh = s[left];

                var length = right - left + 1;
                if( length < minLength ) {
                    minLength = length;
                    start = left;
                }

                windowCh[leftCh]--;
                if(targetCh.ContainsKey(leftCh) && windowCh[leftCh] < targetCh[leftCh]) {
                    findChLength--;
                }

                left++;
            }

            right++;
        }

        Console.WriteLine($"start : {start}, minLength : {minLength}");
    }

    public static void Main(string[] args) {
        
        var question = new Question(
            s: "ADOBECODEBANC",
            t: "ABC"
        );


        //MySolution(question);
        MySolutionReview(question);
    }

}