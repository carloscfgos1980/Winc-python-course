Exercise: Conditions

wincpy start 25596924dffe436da9034d43d0af6791

A local farm has asked you to write a program to help them decide what to do next based on some conditions. You're going to write a function that takes factors and returns a string with one or more actions in it. The value of the factors determine what action(s) the farmer should take.

Here are the factors your function needs to be able to handle:

Factors

Weather
rainy
sunny
windy
neutral
Time of day
day
night
Cow milking status
Need milking: True
Don't need milking: False
Location of the cows
pasture
cowshed
Season
winter
spring
summer
fall
Slurry tank
Full: True
Not full: False
Grass status
Long: True
Short: False
Based on these factors, some actions may be needed:

Actions

take cows to cowshed

This needs to be done when one or more of the following statements are true:

The cows are on the pasture at night
The cows are standing in the rain
milk cows

This needs to be done when the cows require milking, but is only possible when:

The cows are in the cowshed
fertilize pasture

This needs to be done when the slurry tank is full, but is only possible when:

The cows are in the cowshed
The weather is not sunny or windy
mow grass

This needs to be done when all of the following are true:

The grass is long
It's spring
The weather is sunny
But is only possible when:

The cows are not on the pasture
wait

This is done when no other action applies.

Write a function farm_action that takes the seven factors as arguments in the order they are listed above, and returns a single string containing the action(s) the farmer should take. Some extra notes:

You can assume the given arguments are of the correct type, but you should not assume their values are one of the known possible values. It's possible your function will receive a weather argument with value ping-pong ball.

However, your implementation of farm_action should return the actions exactly as listed.

By default the function should only return one action per function call. To decide which action to return look at the order they were listed on this page. For example: if the conditions for both "milk cows" and "mow grass" are met you should only take the action(s) necessary for "milk cows" because it has higher priority.

Under some combination of conditions the function needs to return multiple actions. This happens when (1) cows can be milked, (2) the land can be fertilized or

(3) the grass can be mown. If we need to do one of those things AND the cows are in the pasture we need to add an action before and after our "main" action. The action before is take cows to cowshed, the action after is take cows back to pasture. But be careful: if the cows were already in the cowshed, they should not be taken back to the pasture.

The format for returning multiple actions is to return a string with each action on its own line, in order. The last line should not end on a newline.

Here are some examples:

>>> farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)
'fertilize pasture'

>>> farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)
'wait'

>>> farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)
'milk cows'

>>> farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)
"""take cows to cowshed
milk cows
take cows back to pasture"""
Wincpy Check

Use wincpy check conditions to see if you met all of the requirements for this exercise. Did you pass the test?