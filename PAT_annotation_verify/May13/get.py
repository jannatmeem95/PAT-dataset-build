import json

# with open("/home/jmeem001/Desktop/PAT-extension/special_attention_1424.json", "r") as f:
#     data = json.load(f)

# p54_data = dict()
# for k, v in data.items():
#     if v["relations"][0] == "P54":
#         p54_data[k] = v


# with open(
#     "/home/jmeem001/Desktop/PAT-extension/May13/p54_special_"
#     + str(len(p54_data))
#     + ".json",
#     "w",
# ) as f:
#     json.dump(p54_data, f, indent=6)


# with open(
#     "/home/jmeem001/Desktop/PAT-extension/May13/p54_special_231.json",
#     "r",
# ) as f:
#     special_p54 = json.load(f)

# with open(
#     "/home/jmeem001/Desktop/PAT-extension/verified_data/verified_PAT2_267_verfied.json",
#     "r",
# ) as f:
#     ver_data = json.load(f)

# ids = [v["uniq_id"] for k, v in ver_data.items()]

# c = 0
# p54_need_check = dict()
# for k, v in special_p54.items():
#     if v["uniq_id"] not in ids:
#         p54_need_check[k] = v
#     else:
#         c += 1
#         print(v["uniq_id"])

# print(c)
# print(f"need checking: {len(p54_need_check)}")

# with open(
#     "/home/jmeem001/Desktop/PAT-extension/May13/p54_need_check.json",
#     "w",
# ) as f:
#     json.dump(p54_need_check, f, indent=6)


with open(
    "/home/jmeem001/Desktop/PAT-extension/May13/p54_need_check.json",
    "r",
) as f:
    d = json.load(f)

print(len(d))
# c = 0
# for k, v in d.items():
#     if v["uniq_id"] == 2561:
#         break
#     c += 1
# print(c)
