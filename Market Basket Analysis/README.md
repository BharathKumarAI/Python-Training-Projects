# Market Basket Analysis

## Problem Statement

Consider yourself to be the newly appointed manager of a retail-store ‘ALL-MART’. Your first task as manager of the store is to increase cross-selling

### Objective:

Encourage the customer to buy the items of what they already brought. In order to do this we need to find the association among different items. i.e., If customer buys item `A` how likely he would be buying item `B`. This requires analysis of transactions

**Ex:** Pampers and Beers - During certain period of the day (i.e., during evening) it is identified that people who are buying pampers are also buying beers. So lot of stores separate beers and pampers far away so that people need to walk through the store and can view the products and pick additional products.

#### Understanding of transactions

1. Find the total number of transactions
2. Find the total number of items in the inventory
3. Find the total number of items purchased
4. Find out the 10 most frequently bought items & make a plot

#### Association Rule learning models:

1. Apriori
2. Eclat

Potentially these algorithms can help us to understand the strong association among various products which can help the organization to take decisions like positioning of the items etc.,

##### Apriori

Different packages are available for Apriori algorithm.

```python
# Association Rule Learning (ARL)
from apyori import apriori
```

OR

```python
# Association Rule Learning (ARL)
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
```

Implemetation of Apriori algorithm using these packages are shown in the notebook present in the EDA folder `apriori.ipynb`

**Key terminologies:**

_Support:_
The support of item I is defined as the ratio between the number of transactions containing the item I by the total number of transactions expressed as :

$$support(I) = \frac{\\# \\; transactions \\;  containing \\; I}{\\# \\;  transactions}$$

_Confidence:_

This is measured by the proportion of transactions with item $I_1$, in which item $I_2$ also appears. The confidence between two items $I_1$ and $I_2$, in a transaction is defined as the total number of transactions containing both items $I_1$ and $I_2$ divided by the total number of transactions containing $I_1$.

$$ confidence (I_1 -> I_2) = \frac{\\# \\; transaction \\; containing\\; I_1 \\; and\\; I_2}{\\#\\; transaction\\; containing\\; I_1}$$

_Lift:_

Lift is the ratio between the confidence and support expressed as :

$$ lift (I_1 -> I_2) = \frac{confidence (I_1 -> I_2)}{support(I_2)}$$

### Steps for Apriori Algorithm:

1. Set a minimum support and confidence - `required to save the time to aviod running the model for all the support and confidence values`
2. Take all the subsets in transactions having higher support than minimum support
3. Take all the rules of these subsets having higher confidence than minimum confidence
4. Sort the rules by decreasing lift

#### Parameters for apriori algorithm:

- `min_support` - It is used to select the items with support values greater than the value specified by the parameter.
- `min_confidence` - Filters those rules that have confidence greater than the confidence threshold specified by the parameter.
- `min_lift` - specifies the minimum lift value for the short listed rules.
- `min_length` - specifies the minimum number of items that you want in your rules.

**How to choose parameter values for algorithm:**

If Business defines the minimum support and confidence values then it is recommended to use the same values for the algorithm.else we can use the rule of thumb to choose the values.

_min_support:_

- Suppose we want rules for only those items that are purchased at least 5 times a day, or 7 x 5 = 35 times in one week, since our dataset is for a one-week time period. The support for those items can be calculated as 35/7500 = 0.0045.

_min_confidence:_

- The minimum confidence for the rules is 20% or 0.2.

_min_lift:_

- The value for lift as 3

_min_length:_

- min_length is 2 since we want at least two products in our rules.

**Note:** These values are mostly just arbitrarily chosen, so you can play with these values and see what difference it makes in the rules you get back out.

### Eclat Algorithm:

- only uses support

1. Set a minimum support
2. Take all the subsets in transactions having higher support than minimum support
3. sort those subsets by decreasing support

**Same project is replicated in R**: https://github.com/BharathKumarAI/R-Projects/tree/main/Market-Basket-Analysis

## References:

1. [Apriori Algorithm](https://www.geeksforgeeks.org/apriori-algorithm-in-python/)
2. [Beginner’s Guide To Understanding Apriori Algorithm With Implementation In Python](https://analyticsindiamag.com/beginners-guide-to-understanding-apriori-algorithm-with-implementation-in-python/)
3. [Machine Learning A-Z™: Hands-On Python & R In Data Science](https://www.udemy.com/course/machinelearning/)
4. [Market basket Analysis: Taught by Intellipaat](https://intellipaat.com/)
5. [Association Rules Mining Using Python Generators to Handle Large Datasets - Kaggle notebook](https://www.kaggle.com/code/datatheque/association-rules-mining-market-basket-analysis)
