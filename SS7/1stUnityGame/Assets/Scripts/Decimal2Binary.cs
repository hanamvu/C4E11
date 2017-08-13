using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Decimal2Binary : MonoBehaviour {

	// Use this for initialization
	void Start () {
        int N = 20;
        List<int> DecimalList = new List<int>();
        List<int> BinaryList = new List<int>();
        for (int i = 0; i < N; i++)
        {
            DecimalList.Add(Random.Range(10, 50));
        }
        for (int i = 0; i < DecimalList.Count; i++)
            {
                print(DecimalList[i]);
            }
        for (int i = 0; i < DecimalList.Count; i++)
        {
            BinaryList.Add(deciToBinary(DecimalList[i]));
        }
        for(int i = 0; i < BinaryList.Count; i++)
            {
            print(BinaryList[i]);
        }
        int UCLN = 0;
        UCLN = findUCLN(DecimalList[0], DecimalList[1]);
        for (int i=2; i < DecimalList.Count; i++)
        {
            int j = UCLN;
            UCLN = findUCLN(j, DecimalList[i]);
//            print("Uoc chung lon nhat hien tai cua list la: " + UCLN);
        }
        print("Uoc chung lon nhat cua list la: "+ UCLN);
    }
   

        public int deciToBinary(int num)
        {
            int bin;
            if (num != 0)
            {
                bin = (num % 2) + 10 * deciToBinary(num / 2);
                return bin;
            }
            else
            {
                return 0;
            }

        }

        public int findUCLN(int a,int b)
         {
        if (a == 0 || b == 0)
            return a + b;
        while (a != b)
            {
            if (a > b)
                a = a - b;
            else
                b = b - a;
            }
        return a;
        }
        // Update is called once per frame
        void Update () {
		
	}
}
