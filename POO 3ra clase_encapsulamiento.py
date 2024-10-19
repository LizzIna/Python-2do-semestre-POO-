class Test:
    def __uno(self):
        print("Este metodo es privado, ya que su nombre comienza por __")

    def dos(self):
        print("Este metodo es publico")

    def __tres__(self):
        print("Este metodo tambien es publico, porque su nombre empieza y acaba por __")

p = Test()
#p.__uno() #No funcina porque es privado
p.dos()
p.__tres__()