class Functions():
    
    def Subfields():
        lists=["Sub-fields in AI are:","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for subfields in lists:
            print(subfields)
    
    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2)==1):
            print(num, "is odd number")
        else:
            print(num,"is even number")
    
    
    def Elegible():
        gender=input("Your Gender:").capitalize()
        age=int(input("Your Age:"))
        if(gender=='Male' and age>=21):
            print("ELIGIBLE")
        elif(gender=='Female' and age>=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        Total=sub1+sub2+sub3+sub4+sub5
        percent=(Total/500)*100
        print ("Total:",Total)
        print ("Percentage:",percent) 
        
    
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        formula=(height*breadth)/2
        print("Area formula: (Height*Breadth)/2 ")
        print("Area of Triangle:", formula)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        triangle=height1+height2+breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", triangle)
