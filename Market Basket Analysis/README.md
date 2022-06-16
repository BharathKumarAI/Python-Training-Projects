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

**Key terminologies:**

_Support:_

$$support(I) = \frac{\#\; transactions \;containing \;I}{\#\;transactions}$$

_Confidence:_

$$ confidence (I_1 -> I_2) = \frac{\#\; transaction\; containing\; I_1\; and\; I_2}{\#\; transaction\; containing\; I_1}$$

_Lift:_

If we randomly assign a item to a customer from the population - what is likely hood the customer like the item

$$ lift (I_1 -> I_2) = \frac{confidence (I_1 -> I_2)}{support(I_2)}$$

### Steps for Apriori Algorithm:

1. Set a minimum support and confidence - `required to save the time to aviod running the model for all the support and confidence values`
2. Take all the subsets in transactions having higher support than minimum support
3. Take all the rules of these subsets having higher confidence than minimum confidence
4. Sort the rules by decreasing lift
