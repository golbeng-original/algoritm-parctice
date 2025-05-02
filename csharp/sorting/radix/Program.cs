
partial class Program {

    private static void RadixSort(int[] array, int exp) {
        var output = new int[array.Length];
        var count = new int[10];

        // 해당 자릿수로 위치 누적
        for(var i = 0 ; i < array.Length ; i++) {
            var digit = (array[i] / exp) % 10;
            count[digit]++;
        }

        // 실제 자리 위치를 위한 누적
        for(var i = 1 ; i < array.Length ; i++) {
            count[i] += count[i - 1];
        }

        // 위치로 배치
        for(var i = array.Length - 1 ; i > 0 ; i--) {
            var digit = (array[i] / exp) % 10;
            output[--count[digit]] = array[i];
        }

        Array.Copy(output, array, array.Length);
    }

    public static void RadixSort(int[] array) {
        var maxCount = array.Max();
        var exp = 1;
        while( maxCount / exp > 0 ) {
            RadixSort(array, exp);
            exp *= 10;
        }


    }

    public static void Main(string[] srgs) {
        var question = new int[] {
            321, 203, 4, 5, 6, 102, 10, 66, 45, 2
        };

        RadixSort(question);

        var result = String.Join(", ", question);
        Console.WriteLine(result);
    }
}