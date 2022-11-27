class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}")

    # This will take different param, which is cls
    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method(self):
        print("Called static _method")

test = ClassTest()

# both these will print the same output
test.instance_method()
ClassTest.instance_method(test)

# this will fetch the class method
# by default ClassTest will be the param, if we don't pass anything
ClassTest.class_method()
ClassTest.static_method()