#Tomas James Fernadez
#24.09.14
#Assignment_Spot_Check: Question 1
pool_width= int(input('Please input the width of the pool:'))
pool_length= int(input('Please input the length of the pool:'))
pool_depth= int(input('Please input the depth of the pool:'))
main_section_volume= pool_width *pool_length *pool_depth
circle_radius= pool_width/2
circle_area= 3.14*(circle_radius*circle_radius)
half_circle_volume= (circle_area/2)*pool_depth
pool_volume= main_section_volume+ half_circle_volume
print('the total volume of the pool is {0}'.format (pool_volume))
