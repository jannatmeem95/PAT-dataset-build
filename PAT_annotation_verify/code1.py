import pandas as pd
import json
"""
data = pd.read_csv("Annotate1 - Sheet1.csv", sep=",")
data = data.rename(columns={"Correct? Y/N/ NF": "Annotation"})


# for col in data.columns:
#     print(col)

print(data[data.Annotation == "Y"].shape[0])
print(data[data.Annotation == "N"].shape[0])
print(data[data.Annotation == "NF"].shape[0])

with open("ANNOTATORS/annotate1_cor.json", "r") as f:
    actual_data = json.load(f)

questions = list(actual_data.keys())

data["question_keys"] = questions

print(data.head())
data = data[data["Annotation"] != "N"]
print(data.shape[0])

data.to_csv("annotator1_found_Y.csv", sep=",", encoding="utf-8")

correct_answers = list(data["question_keys"])


filtered_data = dict()

for k, v in actual_data.items():
    if k in correct_answers:
        filtered_data[k] = v

print(len(filtered_data))
with open(
    "accumulate_checked_Y_data/annotator1_" + str(len(filtered_data)) + ".json",
    "w",
) as f:
    json.dump(filtered_data, f, indent=6)
"""

# with open(
#     "ANNOTATORS/annotate1_cor.json", "r"
# ) as f:
#     actual_data1 = json.load(f)

# with open(
#     "/home/jmeem001/Desktop/PAT-extension/ANNOTATORS/annotate2_cor.json", "r"
# ) as f:
#     actual_data2 = json.load(f)


# with open(
#     "/home/jmeem001/Desktop/PAT-extension/ANNOTATORS/annotate3_cor.json", "r"
# ) as f:
#     actual_data3 = json.load(f)


# with open(
#     "/home/jmeem001/Desktop/PAT-extension/PAT-Questions/PAT-data/March2024/PAT-singlehop.json",
#     "r",
# ) as f:
#     pat = json.load(f)


# with open("/home/jmeem001/Desktop/PAT-extension/special_attention_1424.json", "r") as f:
#     specia_att = json.load(f)

# print(
#     f"pat: {len(pat)}, a1: {len(actual_data1)}, a2: {len(actual_data2)}, a3: {len(actual_data3)}, sa: {len(specia_att)}"
# )


# specia_att.update(actual_data1)
# specia_att.update(actual_data2)
# specia_att.update(actual_data3)

# print(f"act: {len(specia_att)}")

# keys = list(specia_att.keys())


# unchecked_data = dict()
# for k, v in pat.items():
#     if k not in keys:
#         unchecked_data[k] = v

# print(len(unchecked_data))

# with open(
#     "/home/jmeem001/Desktop/PAT_annotation_verify/accumulate_checked_Y_data/annotator2_415.json",
#     "r",
# ) as f:
#     a2 = json.load(f)

# with open(
#     "/home/jmeem001/Desktop/PAT_annotation_verify/accumulate_checked_Y_data/annotator3_351.json",
#     "r",
# ) as f:
#     a3 = json.load(f)

# unchecked_data.update(a2)
# unchecked_data.update(a3)


# with open(
#     "/home/jmeem001/Desktop/PAT_annotation_verify/verified_PAT2_267_verfied.json",
#     "r",
# ) as f:
#     verified = json.load(f)

# unchecked_data.update(verified)


# with open(
#     "/home/jmeem001/Desktop/PAT_annotation_verify/finaldata/unchecked_1149_plus_verified_267_plus_a2_a3.json",
#     "w",
# ) as f:
#     json.dump(unchecked_data, f, indent=6)

# print(len(unchecked_data))

with open(
    "finaldata/unchecked_1149_plus_verified_267_plus_a2_a3.json",
    "r",
) as f:
    data = json.load(f)

with open(
    "accumulate_checked_Y_data/annotator1_328.json",
    "r",
) as f:
    a1 = json.load(f)

with open('/Users/jannatarameem/Downloads/PAT_annotation_verify/test/added_new_qs_ans_p54.json','r') as f:
    p54 = json.load(f)

print(f'data: {len(data)}')
print(f'a1: {len(a1)}')
print(f'p54: {len(p54)}')

data.update(a1)
print(f'data: {len(data)}')

data.update(p54)
print(f'data: {len(data)}')

with open('/Users/jannatarameem/Downloads/PAT_annotation_verify/finaldata/all_inclusive.json','w') as f:
    json.dump(data, f, indent =6)