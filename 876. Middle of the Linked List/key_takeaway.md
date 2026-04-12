It is not necessary to traverse all of the elements
inside List to get to the needed point(in this case middle).
For instance, if we have List [1,2,3,4,5], we don't need to know the length of a List to get the middle value in List (3)
Instead, we can run through two variables: one of them iterates by 1 and the other one by 2 steps.
And when the one which iterates faster reaches the end, other one is located in the middle:

[1,2,3,4,5]
    ^    ^

[1,2,3,4,5]
     ^    ^

Middle: (1 step / 2 steps)

Key: You can get to the target by just incresing the steps you are going by