# This program is to create a application generated student exam report
# Team Name = White Shadow
# Team Members = Sajana Gunaratne (Developer), Thiman De Silva (Developer), Rangana Gunathilaka (Mentor)
# Date = 18th Novermber, 2021
# Location = Sri Lanka

print("++++++++++++++++++++++++++++++++++++++++++++")
print("           Student Report System            ")
print("      Programmed by White Shadow Team       ")
print("++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("")

studentFirstname = str(input("Your First Name: "))
studentLastname = str(input("Your Last Name: "))
studentAge = int(input("Your Age: "))
studentParentMob = str(input("Your Contact No: "))

studentRecMat = int(input("Maths Marks on your Exam results : "))
studentRecSci = int(input("Science Marks on your Exam results : "))
studentRecEng = int(input("English Marks on your Exam results : "))
studentRecArt = int(input("Art Marks on your Exam results : "))
studentRecRel = int(input("Religon Marks on your Exam results : "))
studentRecSoc = int(input("Social Studies Marks on your Exam results : "))
studentRecSin = int(input("Science Marks on your Exam results : "))
studentRecAgr = int(input("Agriculture Marks on your Exam results : "))

studentTotalMarks=studentRecMat+studentRecSci+studentRecEng+studentRecArt+studentRecRel+studentRecSoc+studentRecSin+studentRecAgr


studentRecMatGrade = "Not Graded Yet" # str(input())
studentRecSciGrade = "Not Graded Yet" # str(input())
studentRecEngGrade = "Not Graded Yet" # str(input())
studentRecArtGrade = "Not Graded Yet" # str(input())
studentRecRelGrade = "Not Graded Yet" # str(input())
studentRecSocGrade = "Not Graded Yet" # str(input())
studentRecSinGrade = "Not Graded Yet" # str(input())
studentRecAgrGrade = "Not Graded Yet" # str(input())

# For Maths Marks Grading
if studentRecMat>=91 and studentRecMat<=100:
    studentRecMatGrade="A+" #print("Your Maths Marks Grading is A1")
elif studentRecMat>=81 and studentRecMat<91:
    studentRecMatGrade="A" #print("Your Maths Marks Grading is A2")
elif studentRecMat>=71 and studentRecMat<81:
    studentRecMatGrade="B+" #print("Your Maths Marks Grading is B1")
elif studentRecMat>=61 and studentRecMat<71:
    studentRecMatGrade="B" #print("Your Maths Marks Grading is B2")
elif studentRecMat>=51 and studentRecMat<61:
    studentRecMatGrade="C+" #print("Your Maths Marks Grading is C1")
elif studentRecMat>=41 and studentRecMat<51:
    studentRecMatGrade="C" #print("Your Maths Marks Grading is C2")
elif studentRecMat>=33 and studentRecMat<41:
    studentRecMatGrade="D" #print("Your Maths Marks Grading is D")
elif studentRecMat>=21 and studentRecMat<33:
    studentRecMatGrade="E" #print("Your Maths Marks Grading is E1")
elif studentRecMat>=0 and studentRecMat<21:
    studentRecMatGrade="F" #print("Your Maths Marks Grading is E2")
else:
    print("Invalid Input!")

# For Science Marks Grading
if studentRecSci>=91 and studentRecSci<=100:
    studentRecSciGrade="A+" #print("Your Science Marks Grading is A1")
elif studentRecSci>=81 and studentRecSci<91:
    studentRecsciGrade="A" #print("Your Science Marks Grading is A2")
elif studentRecSci>=71 and studentRecSci<81:
    studentRecSciGrade="B+" #print("Your Science Marks Grading is B1")
elif studentRecSci>=61 and studentRecSci<71:
    studentRecSciGrade="B" #print("Your Science Marks Grading is B2")
elif studentRecSci>=51 and studentRecSci<61:
    studentRecSciGrade="C+" #print("Your Science Marks Grading is C1")
elif studentRecSci>=41 and studentRecSci<51:
    studentRecSciGrade="C" #print("Your Science Marks Grading is C2")
elif studentRecSci>=33 and studentRecSci<41:
    studentRecSciGrade="D" #print("Your Science Marks Grading is D")
elif studentRecSci>=21 and studentRecSci<33:
    studentRecSciGrade="E" #print("Your Science Marks Grading is E1")
elif studentRecSci>=0 and studentRecSci<21:
    studentRecMatGrade="F" #print("Your Science Marks Grading is E2")
else:
    print("Invalid Input!")
    
# For English Marks Grading
if studentRecEng>=91 and studentRecEng<=100:
    studentRecEngGrade="A+" #print("Your English Marks Grading is A1")
elif studentRecEng>=81 and studentRecEng<91:
    studentRecEngGrade="A" #print("Your English Marks Grading is A2")
elif studentRecEng>=71 and studentRecEng<81:
    studentRecEngGrade="B+" #print("Your English Marks Grading is B1")
elif studentRecEng>=61 and studentRecEng<71:
    studentRecEngGrade="B" #print("Your English Marks Grading is B2")
elif studentRecEng>=51 and studentRecEng<61:
    studentRecEngGrade="C+" #print("Your English Marks Grading is C1")
elif studentRecEng>=41 and studentRecEng<51:
    studentRecEngGrade="C" #print("Your English Marks Grading is C2")
elif studentRecEng>=33 and studentRecEng<41:
    studentRecEngGrade="D" #print("Your English Marks Grading is D")
elif studentRecEng>=21 and studentRecEng<33:
    studentRecEngGrade="E" #print("Your English Marks Grading is E1")
elif studentRecEng>=0 and studentRecEng<21:
    studentRecEngGrade="F" #print("Your English Marks Grading is E2")
else:
    print("Invalid Input!")

# For Art Marks Grading
if studentRecArt>=91 and studentRecArt<=100:
    studentRecArtGrade="A+" #print("Your Art Marks Grading is A1")
elif studentRecArt>=81 and studentRecArt<91:
    studentRecArtGrade="A" #print("Your Art Marks Grading is A2")
elif studentRecArt>=71 and studentRecArt<81:
    studentRecArtGrade="B+" #print("Your Art Marks Grading is B1")
elif studentRecArt>=61 and studentRecArt<71:
    studentRecArtGrade="B" #print("Your Art Marks Grading is B2")
elif studentRecArt>=51 and studentRecArt<61:
    studentRecArtGrade="C+" #print("Your Art Marks Grading is C1")
elif studentRecArt>=41 and studentRecArt<51:
    studentRecArtGrade="C" #print("Your Art Marks Grading is C2")
elif studentRecArt>=33 and studentRecArt<41:
    studentRecArtGrade="D" #print("Your Art Marks Grading is D")
elif studentRecArt>=21 and studentRecArt<33:
    studentRecArtGrade="E" #print("Your Art Marks Grading is E1")
elif studentRecArt>=0 and studentRecArt<21:
    studentRecMatGrade="F" #print("Your Art Marks Grading is E2")
else:
    print("Invalid Input!")
    
# For Religon
if studentRecRel>=91 and studentRecRel<=100:
    studentRecRelGrade="A+" #print("Your Religon Marks Grading is A1")
elif studentRecRel>=81 and studentRecRel<91:
    studentRecRelGrade="A" #print("Your Religon Marks Grading is A2")
elif studentRecRel>=71 and studentRecRel<81:
    studentRecRelGrade="B+" #print("Your Religon Marks Grading is B1")
elif studentRecRel>=61 and studentRecRel<71:
    studentRecRelGrade="B" #print("Your Religon Marks Grading is B2")
elif studentRecRel>=51 and studentRecRel<61:
    studentRecRelGrade="C+" #print("Your Religon Marks Grading is C1")
elif studentRecRel>=41 and studentRecRel<51:
    studentRecRelGrade="C" #print("Your Religon Marks Grading is C2")
elif studentRecRel>=33 and studentRecRel<41:
    studentRecRelGrade="D+" #print("Your Religon Marks Grading is D")
elif studentRecRel>=21 and studentRecRel<33:
    studentRecRelGrade="E" #print("Your Religon Marks Grading is E1")
elif studentRecRel>=0 and studentRecRel<21:
    studentRecRelGrade="F" #print("Your Religon Marks Grading is E2")
else:
    print("Invalid Input!")

# For Social Studies
if studentRecSoc>=91 and studentRecSoc<=100:
    studentRecSocGrade="A+" #print("Your Social Studies Marks Grading is A1")
elif studentRecSoc>=81 and studentRecSoc<91:
    studentRecSocGrade="A" #print("Your Social Studies Marks Grading is A2")
elif studentRecSoc>=71 and studentRecSoc<81:
    studentRecSocGrade="B+" #print("Your Social Studies Marks Grading is B1")
elif studentRecSoc>=61 and studentRecSoc<71:
    studentRecSocGrade="B" #print("Your Social Studies Marks Grading is B2")
elif studentRecSoc>=51 and studentRecSoc<61:
    studentRecSocGrade="C+" #print("Your Social Studies Marks Grading is C1")
elif studentRecSoc>=41 and studentRecSoc<51:
    studentRecSocGrade="C" #print("Your Social Studies Marks Grading is C2")
elif studentRecSoc>=33 and studentRecSoc<41:
    studentRecSocGrade="D" #print("Your Social Studies Marks Grading is D")
elif studentRecSoc>=21 and studentRecSoc<33:
    studentRecSocGrade="E" #print("Your Social Studies Marks Grading is E1")
elif studentRecSoc>=0 and studentRecSoc<21:
    studentRecSocGrade="F" #print("Your Social Studies Marks Grading is E2")
else:
    print("Invalid Input!")

# For Sinhala Language
if studentRecSin>=91 and studentRecSin<=100:
    studentRecSinGrade="A+" #print("Your Sinhala Language Marks Grading is A1")
elif studentRecSin>=81 and studentRecSin<91:
    studentRecSinGrade="A" #print("Your Sinhala Language Marks Grading is A2")
elif studentRecSin>=71 and studentRecSin<81:
    studentRecSinGrade="B+" #print("Your Sinhala Language Marks Grading is B1")
elif studentRecSin>=61 and studentRecSin<71:
    studentRecSinGrade="B" #print("Your Sinhala Language Marks Grading is B2")
elif studentRecSin>=51 and studentRecSin<61:
    studentRecSinGrade="C+" #print("Your Sinhala Language Marks Grading is C1")
elif studentRecSin>=41 and studentRecSin<51:
    studentRecSinGrade="C" #print("Your Sinhala Language Marks Grading is C2")
elif studentRecSin>=33 and studentRecSin<41:
    studentRecSinGrade="D" #print("Your Sinhala Language Marks Grading is D")
elif studentRecSin>=21 and studentRecSin<33:
    studentRecSinGrade="E" #print("Your Sinhala Language Marks Grading is E1")
elif studentRecSin>=0 and studentRecSin<21:
    studentRecSinGrade="F" #print("Your Sinhala Language Marks Grading is E2")
else:
    print("Invalid Input!")


# For Agriculture
if studentRecAgr>=91 and studentRecAgr<=100:
    studentRecAgrGrade="A+" #print("Your Agriculture Marks Grading is A1")
elif studentRecAgr>=81 and studentRecAgr<91:
    studentRecAgrGrade="A" #print("Your Agriculture Marks Grading is A2")
elif studentRecAgr>=71 and studentRecAgr<81:
    studentRecAgrGrade="B+" #print("Your Agriculture Marks Grading is B1")
elif studentRecAgr>=61 and studentRecAgr<71:
    studentRecAgrGrade="B" #print("Your Agriculture Marks Grading is B2")
elif studentRecAgr>=51 and studentRecAgr<61:
    studentRecAgrGrade="C+" #print("Your Agriculture Marks Grading is C1")
elif studentRecAgr>=41 and studentRecAgr<51:
    studentRecAgrGrade="C" #print("Your Agriculture Marks Grading is C2")
elif studentRecAgr>=33 and studentRecAgr<41:
    studentRecAgrGrade="D+" #print("Your Agriculture Marks Grading is D")
elif studentRecAgr>=21 and studentRecAgr<33:
    studentRecAgrGrade="E" #print("Your Agriculture Marks Grading is E1")
elif studentRecAgr>=0 and studentRecAgr<21:
    studentRecAgrGrade="F" #print("Your Agriculture Marks Grading is E2")
else:
    print("Invalid Input!")


# Printing the Header
print("********************************************************************")
print(" Name of the Student : ",studentFirstname," ",studentLastname)
print(" Age of the Student: ", studentAge, " Years")
print(" Contact Number of the Parent :", studentParentMob)
print("********************************************************************")
print(" ")
print(" ")
print("Subject              Marks        Grade")
print("=======              =====        =====")
print("Mathematics       :  ", studentRecMat, "  ----->  ",studentRecMatGrade)
print("Science           :  ", studentRecSci, "  ----->  ",studentRecSciGrade)
print("English           :  ", studentRecEng, "  ----->  ",studentRecEngGrade)
print("Art               :  ", studentRecArt, "  ----->  ",studentRecArtGrade)
print("Religon           :  ", studentRecRel, "  ----->  ",studentRecRelGrade)
print("Social Studies    :  ", studentRecSoc, "  ----->  ",studentRecSocGrade)
print("Sinhala           :  ", studentRecSin, "  ----->  ",studentRecSinGrade)
print("Agriculture       :  ", studentRecAgr, "  ----->  ",studentRecAgrGrade)
print(" ")
print(" ")
print("Your Total Marks of All Subjects : ", studentTotalMarks)
print("Your Average Marks for the results :", studentTotalMarks/8)

