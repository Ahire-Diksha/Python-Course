class PythonProject:
    
    def basic():
        """Method to display basic syntax and input/output concepts in Python."""
        print("Syntax :\n   1. Print message :\n \t  print('printing msg')")
        print("   2. Take Input :  a=input('msg here') #for string \n \t\t a= int(input('msg here ') #for int \n \t \t same for  float ")
        print("\nFor example: Write a program to display your name:\n\tname = input('Enter your name : ')\n\tprint('Your Name:', name)\n\tOutput: Enter your name : Diksha\n\tYour Name: Diksha")
        ac = input("Detail about Comments (y/n) : ")
        if ac== 'y' or ac=='Y':
            print("2 types of Comments : \n\t1. Single Line \n\t2. Multi Line ")
            print("1. Single Line Comment: # is used for creating single line comment in python\n \tExample: #this is single line")
            print("2. Multiline Comment: ''' ... ''' is used for creating multiline comment\n \tExample: '''this is\n \tmultiline comment'''")
        elif ac == 'n' or ac=='N':
            print("Thank You!!! ")
        else:
            print("Invalid Choice ")

    
    def data():
        """Method to display information about Python data types."""
        print("Python Data Types: Numeric, String, List, Tuple, Dictionary, Set")
    
        while True:
            print("1. Numeric\n2. String\n3. List\n4. Tuple\n5. Dictionary\n6. Set\n7. Main menu")
            choice = int(input("Enter Your Choice: "))
        
            if choice == 1:
                print("NUMERIC DATA TYPE:")
                print("\tNumeric data types in Python include integers, floats, and complex numbers.")
                print("\tIntegers are whole numbers, floats are numbers with decimal points, and complex numbers have a real and imaginary part.")
                print("\tExample:")
                print("\t x = 5")
                print("\t y = 2.5")
                print("\t z = 3 + 4j")
        
            elif choice == 2:
                print("STRING DATA TYPE:")
                print("\tStrings are sequences of characters, enclosed in single, double, or triple quotes.")
                print("\tThey support various operations like concatenation, slicing, and formatting.")
                print("\tExample:")
                print("\t message = 'Hello, world!'")
        
            elif choice == 3:
                print("LIST DATA TYPE:")
                print("\tLists are ordered collections of items, which can be of different data types.")
                print("\tThey are mutable and support various methods like append, extend, and remove.")
                print("\tExample:")
                print("\t my_list = [1, 'two', 3.0]")
        
            elif choice == 4:
                print("TUPLE DATA TYPE:")
                print("\tTuples are similar to lists, but they are immutable.")
                print("\tThey are created using parentheses and support indexing and slicing.")
                print("\tExample:")
                print("\t my_tuple = (1, 'two', 3.0)")
        
            elif choice == 5:
                print("DICTIONARY DATA TYPE:")
                print("\tDictionaries are unordered collections of key-value pairs.")
                print("\tThey are mutable and allow access to values based on keys.")
                print("\tExample:")
                print("\t my_dict = {'name': 'John', 'age': 30}")
        
            elif choice == 6:
                print("SET DATA TYPE:")
                print("\tSets are unordered collections of unique elements.")
                print("\tThey support mathematical set operations like union, intersection, and difference.")
                print("\tExample:")
                print("\t my_set = {1, 2, 3}")
        
            elif choice == 7:
                print("Returning to the main menu...")
                break
        
            else:
                print("Invalid choice!")

    
    def operator():
        """Method to display information about operators in Python."""
        print("Operators in Python: Arithmetic operators, Comparison operators, Assignment operators, Logical operators, Bitwise operators, Membership operators, Identity operators")
        
        while  True :
            print("1. Arithmetic operator \n 2. Comparison Operator \n 3.Assignment Operator \n 4.Bitwise Operator \n 5.Logical Operator \n 6. Membership operator \n 7.Identity Operator \n.8 Operator Precedency \n 9 Main Menu      ")
            ch=int(input("Enter Your Choice : "))
            if  ch==1:
                print("ARITHMETIC OPERATORATOR : ") 
                print("\tMathematical operations including addition, subtraction, multiplication, and division are commonly carried out using Python arithmetic operators.\n\tThey are compatible with integers, variables, and expressions.\n\tIn addition to the standard arithmetic operators, there are operators for modulus, exponentiation, and floor division.")
                print("\t Operator \t	Name \t	Example\n\t+	\tAddition	\t10 + 20 = 30\n\t-	\tSubtraction	\t20 – 10 = 10\n\t*	\tMultiplication	\t10 * 20 = 200\n\t/	\tDivision	\t20 / 10 = 2\n\t%	\tModulus	\t22 % 10 = 2\n\t**	\tExponent	\t4**2 = 16\n\t//	\tFloor Division	\t9//2 = 4")
                print("\t CODE : \n\ta = 21\n\tb = 10\n\t# Addition\n\tprint ('a + b : ', a + b)\n\t# Subtraction\n\tprint ('a - b : ', a - b)\n\t# Multiplication\n\tprint ('a * b : ', a * b)\n\t# Division\n\tprint ('a / b : ', a / b)\n\t# Modulus\n\tprint ('a % b : ', a % b)\n\t# Exponent\n\tprint ('a ** b : ', a ** b)\n\t# Floor Division\n\tprint ('a // b : ', a // b)")
                print("\tOUTPUT :\n\ta + b : 31\n\ta - b : 11\n\ta * b : 210\n\ta / b : 2.1\n\ta % b : 1\n\ta ** b : 16679880978201\n\ta // b : 2")



            elif ch==2:
                print("COMPARISON OPERATOR")
                print("\t To compare two values, Python comparison operators are needed.\n \tBased on the comparison, they produce a Boolean value (True or False).")
                print("\t Operator	\t Name	\t Example\n\t ==	\t Equal	\t 4 == 5 is not true.\n\t!=	\t Not Equal	\t4 != 5 is true.\n\t >	\t Greater Than	\t 4 > 5 is not true\n\t<	\t Less Than \t	4 < 5 is true\n\t >=	\t Greater than or Equal to	\t 4 >= 5 is not true.\n\t <=	\t Less than or Equal to	\t 4 <= 5 is true.")
                print("\t CODE : \n\ta = 4\n\tb = 5\n\t# Equal\n\tprint ('a == b : ', a == b)\n\t# Not Equal\n\tprint ('a != b : ', a != b)\n\t# Greater Than\n\tprint ('a > b : ', a > b)\n\t# Less Than\n\tprint ('a < b : ', a < b)\n\t# Greater Than or Equal to\n\tprint ('a >= b : ', a >= b)\n\t# Less Than or Equal to\n\tprint ('a <= b : ', a <= b)")
                print("\t OUTPUT :\n\ta == b : False\n\ta != b : True\n\ta > b : False\n\ta < b : True\n\ta >= b : False\n\ta <= b : True")
            
            elif ch==3:
                print("ASSIGNMENT OPERATOR ")
                print("\tPython assignment operators are used to assign values to variables in Python.\n\tThe single equal symbol (=) is the most fundamental assignment operator.\n\tIt assigns the value on the operator's right side to the variable on the operator's left side.")
                print("\n\t Operator	\t Name  \t Example\n\t=	\tAssignment Operator	\ta = 10\n\t+=	\tAddition Assignment	\ta += 5 (Same as a = a + 5)\n\t-=	\tSubtraction Assignment	\ta -= 5 (Same as a = a - 5)\n\t*=	\tMultiplication Assignment	\ta *= 5 (Same as a = a * 5)\n\t/=	\tDivision Assignment	\ta /= 5 (Same as a = a / 5)\n\t%=	\tRemainder Assignment	\ta %= 5 (Same as a = a % 5)\n\t**=	\tExponent Assignment	\ta **= 2 (Same as a = a ** 2)\n\t//=	\tFloor Division Assignment	\ta //= 3 (Same as a = a // 3)")
                print("\t CODE : \n\t# Assignment Operator\n\ta = 10\n\t# Addition Assignment\n\ta += 5\n\tprint ('a += 5 : '', a)\n\t# Subtraction Assignment\n\ta -= 5\n\tprint ('a -= 5 : ', a)\n\t# Multiplication Assignment\n\ta *= 5\n\tprint ('a *= 5 : ', a)\n\t# Division Assignment\n\ta /= 5\n\tprint ('a /= 5 : ',a)\n\t# Remainder Assignment\n\ta %= 3\n\tprint ('a %= 3 : ', a)\n\t# Exponent Assignment\n\ta **= 2\n\tprint ('a **= 2 : ', a)\n\t# Floor Division Assignment\n\ta //= 3\n\tprint ('a //= 3 : ', a)")
                print("\t OUTPUT : \n\t # Assignment Operator\n\ta = 10\n\t# Addition Assignment\n\ta += 5\n\tprint ('a += 5 : ', a)\n\t# Subtraction Assignment\n\ta -= 5\n\tprint ('a -= 5 : ', a)\n\t# Multiplication Assignment\n\ta *= 5\n\tprint ('a *= 5 : ', a)\n\t# Division Assignment\n\ta /= 5\n\tprint ('a /= 5 : ',a)\n\t# Remainder Assignment\n\ta %= 3\n\tprint ('a %= 3 : ', a)\n\t# Exponent Assignment\n\ta **= 2\n\tprint ('a **= 2 : ', a)\n\t# Floor Division Assignment\n\ta //= 3\n\tprint ('a //= 3 : ', a)")

            elif ch==4:
                print("BITWISE OPERATOR ")
                print("\tPython bitwise operators execute operations on individual bits of binary integers.\n\tThey work with integer binary representations, performing logical operations on each bit location.\n\tPython includes various bitwise operators, such as AND (&), OR (|), NOT (), XOR (), left shift (), and right shift (>>).")
                print("\n\tOperator	\tName	\tExample\n\t&	\tBinary AND	\tSets each bit to 1 if both bits are 1\n\t|	\tBinary OR	\tSets each bit to 1 if one of the two bits is 1\n\t^	\tBinary XOR	\tSets each bit to 1 if only one of two bits is 1\n\t~	\tBinary Ones Complement	\tInverts all the bits\n\t~	\tBinary Ones Complement	\tInverts all the bits\n\t<<	\tBinary Left Shift	 \tShift left by pushing zeros in from the right and let the leftmost bits fall off\n\t>>	\tBinary Right Shift	\tShift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off")
                print("\t code : \n \t a = 60 # 60 = 0011 1100\n\tb = 13 # 13 = 0000 1101\n\t# Binary AND\n\tc = a & b # 12 = 0000 1100\n\tprint ('a & b : ', c)\n\t# Binary OR\n\tc = a | b # 61 = 0011 1101\n\tprint ('a | b : ', c)\n\t# Binary XOR\n\tc = a ^ b # 49 = 0011 0001\n\tprint ('a ^ b : ', c)\n\t# Binary Ones Complement\n\tc = ~a; # -61 = 1100 0011\n\tprint ('~a : ', c)\n\t# Binary Left Shift\n\tc = a << 2; # 240 = 1111 0000\n\tprint ('a << 2 : ', c)\n\t# Binary Right Shift\n\tc = a >> 2; # 15 = 0000 1111\n\tprint ('a >> 2 : , c)")
                print("\t OUTPUT : \n\ta & b : 12\n\ta | b : 61\n\ta ^ b : 49\n\t~a : -61\n\ta >> 2 : 240\n\ta >> 2 : 15")

            elif ch==5:
                print("LOGICAL OPERATOR ")
                print("\tPython logical operators are used to compose Boolean expressions and evaluate their truth values.\n\tThey are required for the creation of conditional statements as well as for managing the flow of execution in programs.\n\tPython has three basic logical operators: AND, OR, and NOT.")
                print("\tOperator	\tDescription	\tExample\n\tand \tLogical AND	\tIf both of the operands are true then the condition becomes true.	(a and b) is true.\n\tor \tLogical OR	\tIf any of the two operands is non-zero then the condition becomes true.	(a or b) is true.\n\tnot \tLogical NOT	\tUsed to reverse the logical state of its operand	Not(a and b) is false.")
                print("\t CODE : \n\tx = 5\n\ty = 10\n\tif x > 3 and y < 15:\n\t print('Both x and y are within the specified range')")
                print("\tOUTPUT : \n \t Both x and y are within the specified range")

            elif ch==6 :
                print("MEMBERSHIP OPERATOR ")
                print("\tPython membership operators are used to determine whether or not a certain value occurs within a sequence.\n\tThey make it simple to determine the membership of elements in various data structures such as lists, tuples, sets, and strings.\n\tPython has two primary membership operators: the in and not in operators.")
                print("\tOperator	\n\tDescription	\n\tExample\n\tin	Evaluates to true if it finds a variable in the specified sequence and false otherwise.	x in y, here in results in a 1 if x is a member of sequence y.\n\tnot in	Evaluates to true if it does not find a variable in the specified sequence and false otherwise.	x not in y, here not in results in a 1 if x is not a member of sequence y.")
                print("\tCODE :\n\tfruits = ['apple', 'banana', 'cherry']\n\tif 'banana' in fruits:\n\t    print('Yes, banana is a fruit!')\n\telse:\n\t   print('No, banana is not a fruit!')")
                print("\tOUTPUT :\n\t Yes, banana is a fruit!")

            elif ch==7:
                print("IDENTITY OPERATOR ")
                print("\tPython identity operators are used to compare two objects' memory addresses rather than their values.\n\tIf the two objects refer to the same memory address, they evaluate to True; otherwise, they evaluate to False.\n\tPython includes two identity operators: the is and is not operators.")
                print("\tOperator	\tDescription	\t\tExample\n\tis	\tEvaluates to true if the variables on either side of the operator point to the same object and false otherwise	\tx is y, here are results in 1 if id(x) equals id(y)\n\tis not	\tEvaluates to false if the variables on either side of the operator point to the same object and true otherwise	\tx is not y, there are no results in 1 if id(x) is not equal to id(y).")
                print("\t CODE : \n\tx = 10\n\ty = 5\n\tif x is y:\n\t   print('x and y are the same object')\n\telse:\n\t   print('x and y are not the same object')")
                print("\tOUTPUT :\n\tx and y are not the same object")
            
            elif ch==8:
                ac = input("Detail about Operator Precedence (y/n) : ")
                if ac== 'y' or ac=='Y':
                    print("\tSr.No.	\t Operator	\t Description\n\t 1.	\t**	\tExponentiation (raise to the power)\n\t2.	\t~ + -	\tComplement, unary plus and minus (method names for the last two are +@ and -@)\n\t3.	\t* / % //	\tMultiply, divide, modulo, and floor division\n\t4.	\t+ -	\tAddition and subtraction\n\t5.	\t>> <<	\tRight and left bitwise shift\n\t6.	\t&	\tBitwise 'AND'\n\t7.	\t^ |	\tBitwise exclusive `OR' and regular `OR'\n\t8.	\t<= < > >=	\tComparison operators\n\t9.	\t<> == !=	\tEquality operators\n\t10.	\t= %= /= //= -= += *= **=	\tAssignment operators\n\t11.	\tis is not	\tIdentity operators\n\t12	\tin not in	\tMembership operators\n\t13.	\tnot or and	\tLogical operators")
                elif ac == 'n' or ac=='N':
                    print("Thank You!!! ")
                else:
                    print("Invalid Choice ")
            
            elif ch==9:
                break

            else :
                print("Invalid choice !!!")

        

        






                


                


                
            



    
    def loops():
        """Method to display information about loops and control statements in Python."""
        print("Loops and Control Statements in Python: for loop, while loop, break, continue, pass")

        while True:
            print("1. For Loop\n2. While Loop\n3. Break Statement\n4. Continue Statement\n5. Pass Statement\n6. Main Menu")
            choice = int(input("Enter Your Choice: "))
        
            if choice == 1:
                print("FOR LOOP:")
                print("\tA for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).")
                print("\tIt is used when you have a piece of code which you want to repeat n number of times.")
                print("\tSyntax:")
                print("\tfor item in sequence:")
                print("\t    # do something with item")
                print("\tExample:")
                print("\tfruits = ['apple', 'banana', 'cherry']")
                print("\tfor fruit in fruits:")
                print("\t    print(fruit)")
        
            elif choice == 2:
                print("WHILE LOOP:")
                print("\tA while loop is used to repeatedly execute a block of code as long as the condition is true.")
                print("\tIt is used when you do not know the number of iterations beforehand.")
                print("\tSyntax:")
                print("\twhile condition:")
                print("\t    # do something")
                print("\tExample:")
                print("\ti = 1")
                print("\twhile i <= 5:")
                print("\t    print(i)")
                print("\t    i += 1")
        
            elif choice == 3:
                print("BREAK STATEMENT:")
                print("\tThe break statement terminates the loop containing it.")
                print("\tIt is used to exit a loop prematurely.")
                print("\tExample:")
                print("\tfor i in range(5):")
                print("\t    if i == 3:")
                print("\t        break")
                print("\t    print(i)")
        
            elif choice == 4:
                print("CONTINUE STATEMENT:")
                print("\tThe continue statement skips the rest of the code inside a loop for the current iteration.")
                print("\tIt is used to continue with the next iteration of the loop.")
                print("\tExample:")
                print("\tfor i in range(5):")
                print("\t    if i == 3:")
                print("\t        continue")
                print("\t    print(i)")
        
            elif choice == 5:
                print("PASS STATEMENT:")
                print("\tThe pass statement is a null operation - when it is executed, nothing happens.")
                print("\tIt is used as a placeholder when a statement is required syntactically but you do not want any command or code to execute.")
                print("\tExample:")
                print("\tfor i in range(5):")
                print("\t    pass")
        
            elif choice == 6:
                print("Returning to Main Menu")
                break
        
            else:
                print("Invalid choice!!!")



    
    def display_oop_concepts():
        """Function to display information about OOP concepts in Python."""

        print("Python OOP Concepts:")
        print("1. Classes and Objects")
        print("2. Inheritance")
        print("3. Encapsulation")
        print("4. Polymorphism")
        print("5. Abstraction")
        print("6. Main Menu")

        while True:
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                print("CLASSES AND OBJECTS:")
                print("\tClasses are blueprints for creating objects. They define properties (attributes) and behaviors (methods).")
                print("\tObjects are instances of classes. They encapsulate data and behavior.")
                # Example
                print("\tExample:")
                print("\t\tclass Dog:")
                print("\t\t    def __init__(self, name, breed):")
                print("\t\t        self.name = name")
                print("\t\t        self.breed = breed")
                print("\t\t    ")
                print("\t\t    def bark(self):")
                print("\t\t        return 'Woof!'")
                print("\t\t    ")
                print("\t\tmy_dog = Dog('Buddy', 'Golden Retriever')")
                print("\t\tprint('My dog\'s name is', my_dog.name, 'and it belongs to the', my_dog.breed, 'breed.')")
                print("\t\tprint(my_dog.name, 'says:', my_dog.bark())")
            elif choice == 2:
                print("INHERITANCE:")
                print("\tInheritance allows a class (subclass) to inherit properties and behavior from another class (superclass).")
                print("\tIt promotes code reusability and establishes a hierarchy among classes.")
                # Example
                print("\tExample:")
                print("\t\tclass Animal:")
                print("\t\t    def speak(self):")
                print("\t\t        pass")
                print("\t\t    ")
                print("\t\tclass Dog(Animal):")
                print("\t\t    def speak(self):")
                print("\t\t        return 'Woof!'")
                print("\t\t    ")
                print("\t\tclass Cat(Animal):")
                print("\t\t    def speak(self):")
                print("\t\t        return 'Meow!'")
                print("\t\t    ")
                print("\t\tdog = Dog()")
                print("\t\tcat = Cat()")
                print("\t\tprint('Dog says:', dog.speak())")
                print("\t\tprint('Cat says:', cat.speak())")
            elif choice == 3:
                print("ENCAPSULATION:")
                print("\tEncapsulation refers to restricting access to certain components of objects.")
                print("\tIt prevents the accidental modification of data by external code and promotes data hiding.")
                # Example
                print("\tExample:")
                print("\t\tclass Car:")
                print("\t\t    def __init__(self):")
                print("\t\t        self.__max_speed = 200  # Encapsulated variable")
                print("\t\t    ")
                print("\t\t    def drive(self):")
                print("\t\t        print('Driving at', self.__max_speed, 'km/h')")
                print("\t\t    ")
                print("\t\tmy_car = Car()")
                print("\t\t# Trying to access encapsulated variable directly will raise an error")
                print("\t\t# print(my_car.__max_speed)")
                print("\t\tmy_car.drive()")
            elif choice == 4:
                print("POLYMORPHISM:")
                print("\tPolymorphism allows objects of different classes to be treated as objects of a common superclass.")
                print("\tIt enables methods to behave differently based on the object they are called upon.")
                # Example
                print("\tExample:")
                print("\t\tclass Animal:")
                print("\t\t    def speak(self):")
                print("\t\t        pass")
                print("\t\t    ")
                print("\t\tclass Dog(Animal):")
                print("\t\t    def speak(self):")
                print("\t\t        return 'Woof!'")
                print("\t\t    ")
                print("\t\tclass Cat(Animal):")
                print("\t\t    def speak(self):")
                print("\t\t        return 'Meow!'")
                print("\t\t    ")
                print("\t\tdef animal_sound(animal):")
                print("\t\t    return animal.speak()")
                print("\t\t    ")
                print("\t\tdog = Dog()")
                print("\t\tcat = Cat()")
                print("\t\tprint('Dog says:', animal_sound(dog))")
                print("\t\tprint('Cat says:', animal_sound(cat))")
            elif choice == 5:
                print("ABSTRACTION:")
                print("\tAbstraction focuses on hiding the implementation details and showing only the necessary features of an object.")
                print("\tIt simplifies complex systems by providing a simplified interface for interacting with objects.")
                # Example
                print("\tExample:")
                print("\t\tfrom abc import ABC, abstractmethod")
                print("\t\tclass Shape(ABC):")
                print("\t\t    @abstractmethod")
                print("\t\t    def area(self):")
                print("\t\t        pass")
                print("\t\t    ")
                print("\t\tclass Rectangle(Shape):")
                print("\t\t    def __init__(self, width, height):")
                print("\t\t        self.width = width")
                print("\t\t        self.height = height")
                print("\t\t    ")
                print("\t\t    def area(self):")
                print("\t\t        return self.width * self.height")
                print("\t\t    ")
                print("\t\tclass Circle(Shape):")
                print("\t\t    def __init__(self, radius):")
                print("\t\t        self.radius = radius")
                print("\t\t    ")
                print("\t\t    def area(self):")
                print("\t\t        import math")
                print("\t\t        return math.pi * self.radius ** 2")
                print("\t\t    ")
                print("\t\tshapes = [Rectangle(5, 4), Circle(3)]")
                print("\t\tfor shape in shapes:")
                print("\t\t    print('Area of shape:', shape.area())")
            elif choice == 6:
                break
            else:
                print("Invalid choice!!!")


        
    
    
        

    def numpy():
        """Function to display information about fundamental concepts in NumPy."""
        print("Fundamental Concepts in NumPy:")

        while True:
            print("1. NumPy Arrays\n2. Indexing and Slicing\n3. Broadcasting\n4. Main menu")
            choice = int(input("Enter Your Choice : "))
        
            if choice == 1:
                print("NUMPY ARRAYS: ") 
                print("\tNumPy arrays are the core data structure in NumPy library.")
                print("\tThey are similar to Python lists but optimized for numerical computations.")
                print("\tArrays can be created from Python lists or using built-in NumPy functions.")
                print("\tEXAMPLE :")
                # Creating NumPy array from Python list
                print("import numpy as np")
                print("\t arr_list = [1, 2, 3, 4, 5]")
                print("\tnp_arr = np.array(arr_list")
                print("\t print('Python list:', arr_list)")
                print("print('NumPy array:,' np_arr)")
        
            elif choice == 2:
                print("INDEXING AND SLICING")
                print("\tNumPy arrays support powerful indexing and slicing operations.")
                print("\tIndexing starts from 0 and negative indexing is also supported.")
                print("\tSlicing allows selecting a subset of elements from an array.")
                print("\tEXAMPLE :")
                # Creating a NumPy array
                print("import numpy as np")
                print("np_arr = np.array([1, 2, 3, 4, 5]")
                # Indexing
                print("print('Element at index 2:', np_arr[2])")
                # Slicing
                print("print('Sliced array:', np_arr[1:4])")
        
            elif choice == 3:
                print("BROADCASTING")
                print("\tNumPy broadcasting is a powerful mechanism that allows arithmetic operations between arrays of different shapes.")
                print("\tSmaller arrays are 'broadcast' across the larger array to perform the operation.")
                print("\tBroadcasting enables efficient element-wise operations without the need for explicit loops.")
                print("\tEXAMPLE :")
                # Creating NumPy arrays
                print("import numpy as np")
                print("np_arr1 = np.array([[1, 2, 3], [4, 5, 6]]")
                print("np_arr2 = np.array([10, 20, 30]")
                # Broadcasting addition
                print("print('result = np_arr1 + np_arr2')")
                print("print('Array 1:', np_arr1)")
                print("print('Array 2:', np_arr2)")
                print("print('Result after broadcasting addition:', result')")
        
            elif choice == 4:
                print("Returning to Main Menu...")
                break
        
            else:
                print("Invalid choice!!!")



    
    
    def matplotlib_concepts_info():
        """Function to display information about fundamental concepts in Matplotlib."""
        print("Fundamental Concepts in Matplotlib:")

        while True:
            print("1. Basic Plotting\n2. Customizing Plots\n3. Saving Plots\n4. Main menu")
            choice = int(input("Enter Your Choice : "))
        
            if choice == 1:
                print("BASIC PLOTTING:") 
                print("\tMatplotlib is a powerful visualization library in Python.")
                print("\tIt provides various functions to create different types of plots such as line plots, scatter plots, histograms, etc.")
                print("\tEXAMPLE :")
                print("import matplotlib.pyplot as plt")
                print("import numpy as np")
                # Example of creating a simple line plot
                print("x = np.linspace(0, 10, 100")
                print("y = np.sin(x)")
                print('print("plt.plot(x, y)")')
                print("print('plt.title('Sine Wave')')")
                print("print('plt.xlabel('X-axis')')")
                print("print('plt.ylabel('Y-axis')')")
                print("print('plt.grid(True)')")
                print("print('plt.show()')")
        
            elif choice == 2:
                print("CUSTOMIZING PLOTS")
                print("\tMatplotlib allows customization of plots by modifying colors, markers, line styles, labels, etc.")
                print("\tCustomizing plots makes them more informative and visually appealing.")
                print("\tEXAMPLE :")
                print("import matplotlib as plt")
                print("import numpy as np")
                # Example of customizing a plot
                print("x = np.linspace(0, 10, 100)")
                print("y1 = np.sin(x)")
                print("y2 = np.cos(x)")
                print("print('plt.plot(x, y1, color='blue', linestyle='--', label='Sine')')")
                print("print('plt.plot(x, y2, color='red', linestyle='-.', label='Cosine')')")
                print("print('plt.title('Sine and Cosine Waves')')")
                print("print('plt.xlabel('X-axis')')")
                print("print('plt.ylabel('Y-axis')')")
                print("print('plt.legend()')")
                print("print('plt.grid(True)')")
                print("print('plt.show()'")
        
            elif choice == 3:
                print("SAVING PLOTS")
                print("\tMatplotlib allows saving plots in various formats such as PNG, PDF, SVG, etc.")
                print("\tSaving plots enables sharing or using them in documents or presentations.")
                print("\tEXAMPLE :")
                # Example of saving a plot
                print("import matplotlib as plt")
                print("import numpy as np")
                print("x = np.linspace(0, 10, 100)")
                print("y = np.sin(x)")
                print("print('plt.plot(x, y)')")
                print("print('plt.title('Sine Wave')')")
                print("print('plt.xlabel('X-axis')')")
                print("print('plt.ylabel('Y-axis')')")
                print("print('plt.grid(True)')")
                print("print('plt.savefig('sine_wave.png')')")
                print("print('Plot saved as 'sine_wave.png')")
        
            elif choice == 4:
                print("Returning to Main Menu...")
                break
        
            else:
                print("Invalid choice!!!")
   
    

    def pandas():
        """Function to display information about fundamental concepts in Pandas."""
        print("Fundamental Concepts in Pandas:")

        while True:
            print("1. Series\n2. DataFrame\n3. Indexing and Selection\n4. Main menu")
            choice = int(input("Enter Your Choice : "))
        
            if choice == 1:
                print("SERIES: ") 
                print("\tSeries is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, etc.).")
                print("\tIt is similar to a one-dimensional NumPy array with axis labels.")
                print("\tSeries can be created from Python lists, NumPy arrays, dictionaries, etc.")
                print("\tEXAMPLE :")
                print("import pandas as pd")
                # Example of creating a Pandas Series from a Python list
                print("data = [1, 2, 3, 4, 5]")
                print("series = pd.Series(data)")
                print("print('\tPython list:', data)")
                print("print('\tPandas Series:')")
                print('series')
        
            elif choice == 2:
                print("DATAFRAME")
                print("\tDataFrame is a 2-dimensional labeled data structure with columns of potentially different types.")
                print("\tIt is similar to a spreadsheet or SQL table, or a dictionary of Series objects.")
                print("\tDataFrame can be created from Python dictionaries, NumPy arrays, lists of dictionaries, etc.")
                print("\tEXAMPLE :")
                print("import pandas as pd")
                # Example of creating a Pandas DataFrame from a dictionary
                print("data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],'Age': [25, 30, 35, 40],'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}")
                print("df = pd.DataFrame(data)")
                print("\tprint('Dictionary:')")
                print("print(data)")
                print("\tprint('Pandas DataFrame:')")
                print("print(df)")
        
            elif choice == 3:
                print("INDEXING AND SELECTION")
                print("\tPandas provides various methods for indexing and selecting data from a DataFrame.")
                print("\tIndexing can be done by label (loc), by integer position (iloc), or by boolean indexing.")
                print("\tEXAMPLE :")
                print("pandas as pd")
                # Example of indexing and selection in Pandas DataFrame
                print("data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],'Age': [25, 30, 35, 40],'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}")
                print("df = pd.DataFrame(data)")
                print("\tprint('Pandas DataFrame:')")
                print("print(df)")
                print("\tprint('Selecting a single column:')")
                print("print(df['Name'])")
                print("\tprint('Selecting multiple columns:')")
                print("print(df[['Name', 'Age']])")
                print("\tprint('Selecting rows by label (loc):')")
                print("print(df.loc[1])")
                print("\tprint('Selecting rows by integer position (iloc):')")
                print("print(df.iloc[1])")
                print("\tprint('Boolean indexing:')")
                print("print(df[df['Age'] > 30])")
        
            elif choice == 4:
                print("Returning to Main Menu...")
                break
        
            else:
                print("Invalid choice!!!")


    
    
    def scipy():
        """Function to display information about fundamental concepts in SciPy."""
        print("Fundamental Concepts in SciPy:")

        while True:
            print("1. Probability Distributions\n2. Statistical Functions\n3. Integration\n4. Main menu")
            choice = int(input("Enter Your Choice : "))
        
            if choice == 1:
                print("PROBABILITY DISTRIBUTIONS: ") 
                print("\tSciPy provides a wide range of probability distributions for statistical modeling.")
                print("\tThese distributions can be used to generate random samples, compute PDF/CDF, and fit data.")
                print("\tEXAMPLE :")
                print("import numpy as np\nfrom scipy import stats")
                # Example of generating random samples from normal distribution
                print("mu, sigma = 0, 0.1")
                print("samples = np.random.normal(mu, sigma, 1000)")
                print("\tprint('Random samples from normal distribution with mean={} and standard deviation={}.format(mu, sigma)')")
                print("\tprint('First 10 samples:, samples[:10]')")
        
            elif choice == 2:
                print("STATISTICAL FUNCTIONS")
                print("\tSciPy provides a wide range of statistical functions for data analysis.")
                print("\tThese functions include descriptive statistics, hypothesis testing, and regression analysis.")
                print("\tEXAMPLE :")
                print("import numpy as np\nfrom scipy import stats")
                # Example of computing descriptive statistics
                print("data = np.random.normal(0, 1, 100)")
                print("mean = np.mean(data)")
                print("median = np.median(data)")
                print("std_dev = np.std(data)")
                print("\tprint('Descriptive statistics of random data:')")
                print("\tprint('Mean:, mean')")
                print("\tprint('Median:, median')")
                print("\tprint('Standard deviation:, std_dev')")
        
            elif choice == 3:
                print("INTEGRATION")
                print("\tSciPy provides functions for numerical integration of functions.")
                print("\tThese functions can be used to compute definite integrals and solve differential equations.")
                print("\tEXAMPLE :")
                print("import numpy as np\nfrom scipy import stats")
                # Example of numerical integration
                print("f = lambda x: np.exp(-x**2)")
                print("integral, error = stats.norm.integrate.quad(f, -np.inf, np.inf)")
                print("\tprint('Numerical integration of exp(-x^2) from -inf to inf:')")
                print("\tprint('Integral value:, integral')")
                print("\tprint('Estimated error:, error')")
        
            elif choice == 4:
                print("Returning to Main Menu...")
                break
        
            else:
                print("Invalid choice!!!")


if __name__ == "__main__":
    print("Welcome To Python Programming Language !!!")
    print("\nWhat is Python? ")
    print("\tPython is a high-level, general-purpose, and very popular programming language. \nPython programming language (latest Python 3) is being used in web development, \nand Machine Learning applications, along with all cutting-edge technology in Software Industry. \nPython language is being used by almost all tech-giant companies like – Google, Amazon, Facebook, Instagram, Dropbox, Uber… etc.")

    while True:
        print("\nMenu:")
        print("1. Basic of Python (Syntax, Basic Input/Output)")
        print("2. Data Types in Python")
        print("3. Operators in Python")
        print("4. Loops in Python")
        print("5. OOP Concepts of Python")
        print("6. NumPy Library")
        print("7. Matplotlib Library")
        print("8. Pandas Library")
        print("9. SciPy Library")
        print("10. Exit")

        choice = input("Enter Your Choice : ")

        if choice == '1':
            print(" Basic Concepts of Python ......")
            PythonProject.basic()
        elif choice == '2':
            print("Data Types In Python ...")
            PythonProject.data()
        elif choice == '3':
            print("Operators in Python ...")
            PythonProject.operator()
        elif choice == '4':
            print("Loops in Python ...")
            PythonProject.loop()
        elif choice == '5':
            print("OOP Concepts of Python ...")
            PythonProject.oop()
        elif choice == '6':
            print("NumPy Library ...")
            PythonProject.numpy()
        elif choice == '7':
            print("Matplotlib Library ...")
            PythonProject.matplotlib()
        elif choice == '8':
            print("Pandas Library ...")
            PythonProject.pandas()
        elif choice == '9':
            print("SciPy Library ...")
            PythonProject.scipy()
        elif choice == '10':
            print("Exiting .......")
            break
        else:
            print("Invalid Choice ???")
