assert 7**4 == 2401
assert "Hi there Sam!".split() == ["Hi", "there", "Sam!"]
planet = "Earth"
diameter = 12742
assert "The diameter of {} is {} kilometers.".format(planet, diameter) == "The diameter of Earth is 12742 kilometers."
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
assert lst[3][1][2][0] == "hello"
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
assert d["k1"][3]["tricky"][3]["target"][3] == "hello"
def domainGet(email):
    return email.split("@")[1]
assert domainGet('user@domain.com') == "domain.com"
def findDog(text):
    return "dog" in text
assert findDog('Is there a dog here?') == True
def countDog(text):
    return text.count("dog")
assert countDog("This dog runs faster than the other dog dude!") == 2
seq = ['soup','dog','salad','cat','great']
assert list(filter(lambda word: word[0] == "s", seq)) == ['soup', 'salad']
def caught_speeding(speed, is_birthday):
    if speed <= 60 or (61 >= speed <= 80 and is_birthday):
        return "No Ticket"
    if 61 >= speed <= 80 or (speed >= 81 and is_birthday):
        return "Small Ticket"
    return "Big Ticket"
assert caught_speeding(81,True) == "Small Ticket"
assert caught_speeding(81,False) == "Big Ticket"

