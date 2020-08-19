# lst = ["가", "나", "다"]

# for list_ids, list_val in enumerate(lst):
#     print(list_ids, list_val)

# test = [["가", "나", "다"], ["라","마","사"], ["아","자","차"]]

# # test에 i가 있는 동안, 반복 하시오.
# for i in test:
#     # i에 j가 있는 동안, 반복 하시오.
#     for j in i:
#         print(j)

# lst = {"가":1, "나":2, "다":3}
# gst = lst["가"]
# print(gst)

balls = [1, 2, 3, 4]
weapons = [11, 22, 3, 44]

for ball_idx, ball_val in enumerate(balls):
    print('ball :', ball_val)
    for weapons_idx, weapon_val in enumerate(weapons):
        print("weapons :", weapon_val)
        if ball_val == weapon_val: # 충돌 체크
            print("공과 무기가 충돌")
            break
    else:
        continue
    print("바깥 for 문 break")
    break
    # if 조건:
    #     동작
    # else:
    #     그 외의 동작