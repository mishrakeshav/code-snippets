import java.util.*;
import java.io.*;


class Permute {
    public List<List<Integer>> all;   
    public List<Integer> arr;
    int n;
    Permute(List<Integer> arr){
        all = new ArrayList<>();
        this.arr = arr;
        n = arr.size();
    }

    public boolean nextPermutations(){
        int i = n - 2;
        // StringBuilder sb = new StringBuilder();
        // sb.append("curr = " + arr.toString());

        while(i >= 0 && arr.get(i) > arr.get(i + 1)){
            i--;
        }

        if(i < 0){
            return false;
        }
        int j = n - 1;
        while(arr.get(i) > arr.get(j)){
            j--;
        }
        // sb.append(" i = " + (i + 1 )+ "  j = " + (j + 1) + " ");
        Collections.swap(arr, i, j);
        Collections.reverse(arr.subList(i + 1, n));
        // sb.append(arr.toString());
        // System.out.println(sb);
        return true;
    }

    public void getPermutations(){
        all.add(new ArrayList<>(arr));
        while(nextPermutations()){
            all.add(new ArrayList<>(arr));
        }
    }


    public void getPermutations(int start, List<Integer> next){
        if(start == arr.size()){
            all.add(new ArrayList<>(next));
        }
        for(int i = start; i < arr.size(); i++){
            next.add(arr.get(i));
            Collections.swap(arr, i, start);
            getPermutations(start + 1, next);
            Collections.swap(arr, i, start);
            next.remove(arr.get(i));
        }
    }
}


class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StreamTokenizer st = new StreamTokenizer(br);
    
    public static int nextInt() throws IOException {
        st.nextToken();
        return (int) st.nval;
    }
    public static void main(String[] args) throws IOException {
        
        int n = nextInt();
        List<Integer> arr = new ArrayList<>();
        for(int i = 1; i <= n; i++){
            arr.add(i);
        }
        Permute pe = new Permute(arr);
        pe.getPermutations();
        // for(List<Integer> l : pe.all){
        //     System.out.println(l.toString());
        // }

            
    }
}