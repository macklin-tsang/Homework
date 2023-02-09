eat = "Did you eat? "

study = "Did you study? "

laundry = "Did you do your laundry? "

call = "Did you call grandma? "

pts = 0

questions = [eat, study, laundry, call]

for x in questions:

    answer = input(x)

    if answer == "yes":
        pts += 1
        
responses = ["I'm coming over", "Ok.", "Good!"]

if pts >= 3:
    print(responses[2])
if 3 > pts <= 1:
    print(responses[1])
if pts < 1:
    print(responses[0])
