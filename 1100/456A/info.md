# A. Laptops 
**Difficulty**: 1100 
**Link**: https://codeforces.com/problemset/problem/456/A

# A. Laptops
One day Dima and Alex had an argument about the price and quality of laptops.
Dima thinks that the more expensive a laptop is, the better it is. Alex
disagrees. Alex thinks that there are two laptops, such that the price of the
first laptop is less (strictly smaller) than the price of the second laptop
but the quality of the first laptop is higher (strictly greater) than the
quality of the second laptop.

Please, check the guess of Alex. You are given descriptions of _n_ laptops.
Determine whether two described above laptops exist.

Input

The first line contains an integer _n_ (1 ≤  _n_ ≤ 105) — the number of
laptops.

Next _n_ lines contain two integers each, _a_ _i_ and _b_ _i_ (1 ≤  _a_ _i_ ,
_b_ _i_ ≤  _n_), where _a_ _i_ is the price of the _i_ -th laptop, and _b_ _i_
is the number that represents the quality of the _i_ -th laptop (the larger
the number is, the higher is the quality).

All _a_ _i_ are distinct. All _b_ _i_ are distinct.

Output

If Alex is correct, print "Happy Alex", otherwise print "Poor Alex" (without
the quotes).

Examples

Input

    
    
    2  
    1 2  
    2 1  
    

Output

    
    
    Happy Alex  
    

