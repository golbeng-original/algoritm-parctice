
partial class Program {

    public static void Merge(int[] arr, int left, int middle, int right) {

        var helper = new int[arr.Length];
        for( var i = left ; i <= right  ; i++ ) {
            helper[i] = arr[i];
        }

        int helperLeft = left;
        int helperRight = middle + 1;
        int current = left;

        while( helperLeft <= middle && helperRight <= right ) {
            if( helper[helperLeft] <= helper[helperRight] ) {
                arr[current] = helper[helperLeft];
                helperLeft++;
            }
            else {
                arr[current] = helper[helperRight];
                helperRight++;
            }

            current++;
        }

        while( helperLeft <= middle ) {
            arr[current++] = helper[helperLeft++];
        }
    }

    public static void MergeSort(int[] arr, int left, int right) {

        if( left < right ) {

            var middle = (left + right) / 2;
            MergeSort(arr, left, middle);
            MergeSort(arr, middle + 1, right);

            Merge(arr, left, middle, right);
        }
    }

    public static void Main(string[] args) {

        var question = new int[] {5, 3, 1, 10, 15, 19, 34, 9, 7, 24, 23};

        MergeSort(question, 0 , question.Length - 1);

        var result = String.Join(", ", question);
        Console.WriteLine(result);
    }
}