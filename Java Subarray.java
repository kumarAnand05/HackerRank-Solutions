/*
Question:

We define the following:

A subarray of an -element array is an array composed from a contiguous block of the original array's elements. For example, if , then the subarrays are , , , , , and . Something like  would not be a subarray as it's not a contiguous subsection of the original array.
The sum of an array is the total sum of its elements.
An array's sum is negative if the total sum of its elements is negative.
An array's sum is positive if the total sum of its elements is positive.
Given an array of  integers, find and print its number of negative subarrays on a new line.

Input Format

The first line contains a single integer, , denoting the length of array .
The second line contains  space-separated integers describing each respective element, , in array .

Constraints

Output Format

Print the number of subarrays of  having negative sums.

Sample Input

5
1 -2 4 -5 1
Sample Output

9
Explanation

There are nine negative subarrays of :

Thus, we print  on a new line.
*/

// Solution:

import java.util.*;

public class Solution{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n];
        for(int i=0; i<n;i++){
            A[i]= sc.nextInt();
        }
        // Print the number of subarrays hacinf the negative sum
        int res=0;
        
        for(int subSize=1;subSize<=n;subSize++){
            for(int idx=0; idx<=n-subSize;idx++){
                int[] arr = Arrays.copyOfRange(A, idx, idx+subSize);
                int subSum=0;
                for(int x:arr){
                    subSum+=x;
                }
                if(subSum<0){
                    res+=1;
                }
            }
        }        
        System.out.println(res);
    }
}
