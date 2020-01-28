
public class BubbleSort {

	int ar[]= {11,212,83,74,55,66};
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BubbleSort ob = new BubbleSort();
		for(int i=0;i<ob.ar.length-1;i++) {
			for(int j=0;j<ob.ar.length-i-1;j++) {
				if(ob.ar[j]>ob.ar[j+1]) {
					int swap = ob.ar[j];
					ob.ar[j]=ob.ar[j+1];
					ob.ar[j+1]=swap;
				}
			}
		}
		for(int i=0;i<ob.ar.length;i++) {
			System.out.print(ob.ar[i]+" ");
		}
	}

}
