import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		List<Integer> arr = new ArrayList<Integer>();

		for (int i = 0; i < n; i++) {
			arr.add(i + 1);
		}
		int counter = 1;
		int current_math = 1;
		int loop_index = 0;
		if(n == 1){
			System.out.println(1);
			return;
		}

		while(true) {
			if(arr.size() == 1) {
				break;
			}

			// System.out.println(counter);

			while(loop_index < arr.size()){
				System.out.println(loop_index);
				current_math ++;
				if(current_math == (int)(Math.pow(m, counter))) {
					arr.remove(loop_index);
					loop_index --;
					counter ++;
				}
				loop_index ++;
			}
			loop_index = arr.size() - 1;
			while(true){
				if(loop_index == -1){
					break;
				}
				current_math ++;
				if(current_math == Math.pow(m, counter)) {

					arr.remove(loop_index);

					counter ++;
				}
				System.out.println(loop_index);
				loop_index --;
			}

		}

		System.out.println(arr.get(0));
	}

}
