// See https://aka.ms/new-console-template for more information

partial class Program {

    public static int Partition(int[] arr, int left, int right) {
        var pivotValue = arr[(right + left) / 2];

        while(left <= right) {
            
            while(arr[left] < pivotValue ) {
                left++;
            }

            while(arr[right] > pivotValue ) {
                right--;
            }

            if( left <= right ) {
                (arr[right], arr[left]) = (arr[left], arr[right]);

                left++;
                right--;
            }
        }

        return left;
    }

    public static void QuickSort(int[] arr, int left, int right) {

        if( left >= right ) {
            return;
        }

        var middle = Partition(arr, left, right);
        QuickSort(arr, left, middle - 1); 
        QuickSort(arr, middle, right);
    }


    public static void Main(string[] args) {
        Console.WriteLine("Hello, World!");

        var question = new int[10] {10, 6, 8, 3, 0, 4, 9, 1, 2, 20};
        //var question = new int[4] {10, 6, 8, 3 };
        //var question = new int[6] {10, 6, 8, 3, 2, 20 };
    
        QuickSort(question, 0, question.Length - 1);

        var result = String.Join(", ", question);

        Console.WriteLine(result);

        //QuickSort(question, 0, question.Length);
    }
}

