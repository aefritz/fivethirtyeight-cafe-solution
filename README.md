Solution to:

[https://fivethirtyeight.com/features/does-your-gift-card-still-have-free-drinks-on-it/]

The least number of card uses that could lead to this situation is 50. However unlikely, you've used the same card 50 times in a row. This would happen with probability:

(.5 ^ 50)(.5 ^ 0)(50 C 0)

where 50 C 0 represents the binonmial coefficient '50 choose 0'. In this situation there would be 50 coffees left on the remaining card.

The 2nd least number of card uses is 51. You've used one card 50 times and exhausted its credits, and you've used the other card only once. This would happen with probability:

(.5 ^ 50)(.5 ^ 1)(51 C 1)

and leave 49 coffees remaining on the second card.

Following this same pattern, the expected value for the number of remaining drinks is:

(.5 ^ 50)(.5 ^ 0)(50 C 0)(50) + (.5 ^ 50)(.5 ^ 1)(51 C 1)(49) ... + (.5 ^ 50)(.5 ^ 50)(100 C 50)(0)
