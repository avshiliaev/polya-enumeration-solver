### 1. The Approach.

The overall solution is based on the:
* Code: https://github.com/rosenbrockc/polya
* Article: https://www.ias.ac.in/article/fulltext/reso/019/04/0338-0346
* Article: https://www.geeksforgeeks.org/orbit-counting-theorem-or-burnsides-lemma/
* Paper: https://github.com/rosenbrockc/polya/blob/master/docs/polyaenum.pdf
* Paper: https://www.sciencedirect.com/science/article/pii/0012365X9390015L
* Paper: https://arxiv.org/abs/1412.4167
* Paper: https://math.mit.edu/~apost/courses/18.204_2018/Jenny_Jin_paper.pdf

1.1. Burnside’s Lemma is also sometimes known as orbit counting theorem. It is one of the results of group theory. 
It is used to count distinct objects with respect to symmetry. It basically gives us the formula to count the total 
number of combinations, where two objects that are symmetrical to each other with respect to rotation or reflection are 
counted as a single representative. Burnside's lemma is a result in group theory that can help when counting objects 
with symmetry taken into account. It gives a formula to count objects, where two objects that are related by a symmetry 
(rotation or reflection, for example) are not to be counted as distinct.

>Let G be a finite group that acts on the set X. Let X/G be the set of orbits of X (that is, each element of X/G is 
an orbit of X). For any element g∈G, let X^g be the set of points of X which are fixed by g: X^g = {x∈X:g⋅x=x}. Then 
>
>∣X/G∣ = 1/∣G∣ ∑g∈G |X^g|
>
>In other words, the number of orbits is the average number of fixed points of G.

1.2. The Polya enumeration theorem is a theorem in combinatorics that both follows from and ultimately generalizes 
Burnside's lemma on the number of orbits of a group action on a set. We can represent it as a group G = Sw x Sh, where 
Sw and Sh are the symmetric groups of their underlying sets W and H. The group G acts on the set X = W x H, which we can 
imagine as the set of indexes of the entries of the matrices. Each matrix is a function f: X->S, and the f∈S^x. In the 
end, according to the theorem, we need to figure out the cardinality of |S^x/G|, or to compute the orbits of G in S^X.

### 2. What kind of running time we should expect here. 

While the factorials and the gcd matrices can be computed in O(Nlog(N)), the bottle neck is where we iterate over 
partitions of both sides of the matrix. So the runtime, at least the pseudo-polynomial one, eliminating all constants, 
would be O(n^2).

### 3. The first viable solution and some optimizations.

So in order to solve the problem, we are to compute:

3.1. All partitions of a number. One can use a recursive algorithm for this purpose.
**Optimization**: The solution is fast enough. However an iterative algorithm, as described here 
https://arxiv.org/abs/0909.2331, would be even more performant for large numbers of w and h.

3.2. Greatest common divisors (gcd) of multiple numbers. An efficient way to compute gcd is the Euclidean algorithm. 
**Optimization**: However, since we are going to compute the gcd of all pairs of numbers in a set, and each one can possible 
be computed many times, it would be logical to compute the entire matrix in advance using dynamic programming. 

3.3. We can take the same approach with the factorials. The solution requires the factorials of all numbers in a 
set where each one can possible be computed many times. So again we are to compute the entire matrix in advance 
bottom-up based on n! = n(n-1)! and 0!=1!=1.
  
### 4. A possible real-life implications.

Probably the most prominent though not strictly computer science application is the Chemical Isomer Enumeration.
In chemistry, a chemical formula can represent more than one molecule due to varying arrangements of the molecules in 
space. The molecules that have the same chemical formula but different chemical structures are called isomers, and we 
can use Polya Enumeration Theorem to enumerate these types of isomers.
