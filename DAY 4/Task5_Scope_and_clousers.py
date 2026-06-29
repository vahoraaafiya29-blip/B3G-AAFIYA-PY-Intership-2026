mode="Global /mode"

def outer_function():
    mode="Outer Mode"

    def inner_function():
        mode="Inner Mode"

        print("Local Scope(Inner Function):",mode)
    inner_function()
    print("Enclosing Scope(Outer Function:",mode)
outer_function()
print("Global Scope:",mode) 