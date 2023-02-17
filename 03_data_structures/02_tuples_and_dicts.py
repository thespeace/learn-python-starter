#list와 비슷하지만 더 간단하게 사용할 수 있다.
#list와 tuple의 차이점은? tuple은 불변성을 가진다. 즉 변경 불가!
days = ("Mon","Tue","Wed")
print(days[0])
print(days[-1]) #아이템의 뒤에서부터 접근.

print("==================Dictionary==================")
#백과사전을 예로 들자면, 단어와 정의가 있다 그걸 key value pair이라고 한다.(키-값 쌍) : 키는 단어, 값은 정의
player = {
    'name' : 'seo',
    'age' : 32,
    'alive' : True,
    'fav_food' : ["🍕","🍔"]
}
print(player)
print(player.get('name')) #key를 가져와서 value를 return한다.
print(player['fav_food'])

player.pop('age') #특정 key를 지우기.
print("pop :",player)

player['fav_sport'] = "🥽" #key : value 추가.
print("add :",player)

player['fav_food'].append("🥠")
print("list key append :",player)

player.clear()
print("clear :",player) #list처럼 변경가능하다. 불변하는 것은 오직 tuple뿐!
