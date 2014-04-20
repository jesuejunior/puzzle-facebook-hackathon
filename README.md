
# Repository of Puzzle to Facebook Hackathon Passport

## References :

https://docs.python.org/2/library/collections.html
https://docs.python.org/2/tutorial/datastructures.html

and my mind.

## Challenge :

### K Difference

Given N numbers , [N<=10^5] we need to count the total pairs of numbers which have a difference of K. [K>0 and K<10^9]. The solution should have as low of a computational time complexity as possible.


Input Format:

1st line contains N & K (integers).
2nd line contains N numbers of the set. All the N numbers are assured to be distinct.


Output Format:

One integer saying the no of pairs of numbers that have a diff K.

Sample Input #00:
5 2
1 5 3 4 2

Sample Output #00:
3

Explanation:
The possible pairs are (5,3), (4,2) and (3,1).


## Execute

```shell
 $ python main.py < inputs\inputXXX.txt
```

    ### Execute tests
    ```shell
    $ py.test
    ```