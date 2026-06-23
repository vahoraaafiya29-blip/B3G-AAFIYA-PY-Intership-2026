admin=("add","edit","delete","view")
editor={"add","edit"}

required="add"

if required in editor:
    print("Editor can perform Action")
else:
    print("Editor cannot perform Action")
