#Tomas James Fernadez
#24.09.14
#Assignment_Spot_Check: Question 2
user_entered_weight= int(input('Please enter a weight measured in whole grams:'))
weights_required_hundred= user_entered_weight//100
weights_required_fifty= user_entered_weight%100//50
weights_required_ten= user_entered_weight%100%50//10
weights_required_five= user_entered_weight%100%50%10//5
weights_required_two= user_entered_weight%100%50%10%5//2
weights_required_one= user_entered_weight%100%50%10%5%2//1
print('Here are the weights required to balance the user inputed Weight:')
print(weights_required_hundred':is the amount of 100g weights required')
print(weights_required_fifty':is the amount of 50g weights required')
print(weights_required_ten':is the amount of 10g weights required')
print(weights_required_five':is the amount of 5g weights required')
print(weights_required_two':is the amount of 2g weights required')
print(weights_required_one':is the amount of 1g weights required')
      
