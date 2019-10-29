class Dog:
    def __init__(self, height):
        if height >= 10:
            raise ValueError("\"Dog's can't be that tall, you oaf\"")
        else:
            self.height = height

try:
  clifford = Dog(10)
except Exception as e:
    print(e)
    print("What a shame")