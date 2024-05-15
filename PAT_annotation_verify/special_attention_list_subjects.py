import json

# with open("/home/jmeem001/Desktop/PAT-extension/special_attention_1424.json", "r") as f:
#     specia_att = json.load(f)

# subjects = set()
# for k, v in specia_att.items():
#     subjects.add(v["subject"]["subject"])


# subs = list(subjects)
# with open(
#     "/home/jmeem001/Desktop/PAT_annotation_verify/filter/subjects_special_attention.json",
#     "w",
# ) as f:
#     json.dump(subs, f, indent=6)

# with open(
#     "/home/jmeem001/Desktop/PAT_annotation_verify/filter/subjects_special_attention.json",
#     "r",
# ) as f:
#     subjects = json.load(f)

with open(
    "/Users/jannatarameem/Downloads/PAT_annotation_verify/finaldata/filtered_singlehop_final_2687.json",
    "r",
) as f:
    data = json.load(f)

print(len(data))
currently_subjects = set()
for k, v in data.items():
    # if "previous" in k or "before" in k or " last " in k:
    #     continue
    currently_subjects.add(v["subject"]["subject"])

with open('/Users/jannatarameem/Downloads/PAT_annotation_verify/test/subjects_singlehop.json','w') as f:
    json.dump(list(currently_subjects),f,indent =2)
# with open("/home/jmeem001/Desktop/PAT_annotation_verify/test/test.json", "r") as f:
#     extra_p54 = json.load(f)

# for k, v in extra_p54.items():
#     if "previous" in k or "before" in k or " last " in k:
#         continue
#     currently_subjects.add(v["subject"]["subject"])

c = 0
"""
with open(
    "finaldata/unchecked_singlehop_1149.json",
    "r",
) as f:
    unchecked = json.load(f)
unchecked_subjects = set()
for k, v in unchecked.items():
    unchecked_subjects.add(v["subject"]["subject"])


why_prev_but_no_cur = dict()
updated_data = dict()
for k, v in data.items():
    if "previous" in k or "before" in k or " last " in k:
        if (
            v["subject"]["subject"] not in currently_subjects
            and v["subject"]["subject"] not in unchecked_subjects
        ):
            c += 1
            continue
            # if v['relations'][0] != 'P54':
            #     why_prev_but_no_cur[v["subject"]["subject"]] = ((v["subject"]['subLabel'], v['relations'][0]))
            # if c < 5:
            #     print(v["subject"]["subject"])
        else:
            updated_data[k] = v
    else:
        updated_data[k] = v

print(c)
print(len(updated_data))


# with open('troubleshooting/why_prev_but_no_cur2.json','w') as f:
#     json.dump(why_prev_but_no_cur, f, indent =2)

with open('/Users/jannatarameem/Downloads/PAT_annotation_verify/finaldata/filtered.json','w') as f:
    json.dump(updated_data,f,indent = 6)

"""


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

# with open(
#     "/home/jmeem001/Desktop/PAT_annotation_verify/verified_PAT2_267_verfied.json",
#     "r",
# ) as f:
#     verified = json.load(f)


# verified_subjects = set()
# for k, v in a2.items():
#     verified_subjects.add(v["subject"]["subject"])

# for k, v in a3.items():
#     verified_subjects.add(v["subject"]["subject"])

# for k, v in verified.items():
#     verified_subjects.add(v["subject"]["subject"])


# c = 0
# for k, v in data.items():
#     if (
#         v["subject"]["subject"] in subjects
#         and v["subject"]["subject"] not in verified_subjects
#     ):
#         if "previous" in k or "before" in k or " last " in k:
#             c += 1
#             if c > 80 and c < 90:
#                 print(v["subject"]["subject"])

# print(c)
