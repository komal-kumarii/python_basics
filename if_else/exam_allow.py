classes_held=int(input("numbers of classes held"))
classes_attended=int(input("number of classes attended"))
percentage= classes_attended/classes_held*100
if percentage>75:
    print("allowed")
else:
    print("not allowed")