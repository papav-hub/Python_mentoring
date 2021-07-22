import re

new_id = input("new_id를 입력하세요 : ") # new_id 입력받기

new_id = new_id.lower() # 1. new_id의 모든 대문자를 대응되는 소문자로 치환합니다.

new_id = re.sub(r"[^a-z0-9-_.]","",new_id) # 2. new_id에서 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자를 제거합니다.

while ".." in new_id:
    new_id = new_id.replace("..", ".") # 3. new_id에서 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환합니다.


if(new_id[0] == ".") : # 4. new_id에서 마침표가 처음이나 끝에 위치한다면 제거합니다.
    if (len(new_id) > 1 ) :
        new_id = new_id[1:]
    else:
        new_id = " "

if(new_id[-1] == ".") :
    if (len(new_id) > 1 ) :
        new_id = new_id[:-1]
    else:
        new_id = " "
    
new_id = new_id.replace(" ", "a")# 5. new_id가 빈 문자열이라면, new_id에 “a”를 대입합니다.

new_id = new_id[:15] # 6. new_id의 길이가 16자 이상이라면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.

# 만약, 제거 후 마침표가 new_id의 끝에 위치한다면 끝에 위치한 마침표 문자를 제거합니다.
if(new_id[-1] == ".") :
    if (len(new_id) > 1 ) :
        new_id = new_id[:-1]
    else:
        new_id = " "

if(len(new_id)==1): # 7. new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3자가 될 때까지 반복해서 붙입니다.
    new_id = new_id + new_id[0]*2

if(len(new_id)==2):
    new_id = new_id + new_id[1]

print(new_id)