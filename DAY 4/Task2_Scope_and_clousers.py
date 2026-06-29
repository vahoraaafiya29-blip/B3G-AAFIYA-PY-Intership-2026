def make_gretting(language):

    def greet(name):
        if language=="Gujrati":
            print("kem cho,",name)
        elif language=="English":
            print("Hello,",name)
        else:
            print("Hii,",name)
    return greet

Gujrati_greet=make_gretting("Gujrati")
English_greet=make_gretting("English")

Gujrati_greet("Aafiya")
English_greet("Aafiya")