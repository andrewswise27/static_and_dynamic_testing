### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # needs to be '=='.
      return True
    else # else statement is missing a colon
      return False
   


  dif highest_card(self, card1 card2): # dif used instead of 'def', also syntax error between card1 and card2 as there is a missing comma
  if card1.value > card2.value: # if statement is missing indentation
    return card # this should say 'return card1'
  else:
    return card2
    # there needs to be an elif that allows for return when the cards are of equal value
  
# dif/def mistake on the function definition above means the 'return' in the else statment above would cause the below function to be ignored

def cards_total(self, cards): # definition of this function is happening outside the scope of the CardGame class
  total  #total here is not being established as a variable properly
  for card in cards:
    total += card.value
    return "You have a total of" + total # indentation of return means that the for loop stops after one itteration. additionally code will break trying to attatch an integer to a string like this
  
```
