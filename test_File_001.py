import pytest
class Test_Number:

    def test_Add(self):
        A = 10
        B = 10
        Sum = A + B
        print("Sum of A & B :", Sum)
        if Sum == 20:
            print("Addition is Correct")
            assert True
        else:
            print("Addition is Wrong ")
            assert False

    def test_Sub(self):
        P=30
        Q=10
        Sub=P-Q
        print("Substraction is :",Sub)
        if Sub==20:
            print("Substraction is Successfull")
            assert True
        else:
            print("Substraction is Failed")
            assert False

    def test_Mul(self):
        X=10
        Y=10
        Mul=X*Y
        print("Multiplication is :", Mul)
        if Mul==100:
            print("Multiplication is Successfull")
            assert True
        else:
            print("Multiplication is Failed")
            assert False