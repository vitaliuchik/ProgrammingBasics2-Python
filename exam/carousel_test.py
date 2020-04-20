from carousel import Carousel, Attraction
# a carousel has a type and a capacity
c1 = Carousel("DE501", 3)
assert(str(c1) == "DE501 house 3: []")
# children can be added
assert(c1.add_child("Ostap") == True)
assert(c1.add_child("Orislava") == True)
assert(c1.add_child("Olga") == True)
# can't add children past the max capacity
assert(c1.add_child("Orest") == False)
assert(str(c1) == "DE501 house 3: ['Ostap', 'Orislava', 'Olga']")
# can remove the most recent child
assert(c1.remove_child() == True)
assert(str(c1) == "DE501 house 3: ['Ostap', 'Orislava']")
# mom can call her baby
assert(c1.remove_child(mom_call = 'Ostap') == 'Ostap')
assert(c1.remove_child(mom_call = 'Os') == False)
assert(str(c1) == "DE501 house 3: ['Orislava']")
assert(c1.add_child("Oksana") == True) # that frees up space!
c2 = Carousel("DE505", 4)
# can't remove a child from an empty carousel
assert(c2.remove_child() == False)
assert(c2 == Carousel("DE505", 4))
assert(c2 != c1)
assert(c2 != "DE505") # should not crash!
# an Attraction is a Carousel with a name and a capacity
# an Attraction has a supervisor of the attraction
a1 = Attraction("Children Train", 10, 'Den')
assert(str(a1) == "Children Train house 10: ['Den']")
assert(a1.add_child("Denny") == True)
assert(str(a1) == "Children Train house 10: ['Den', 'Denny']")
# an attraction knows whether it's currently being run
a1.start_attraction()
# while it's being runned, you can't remove children
assert(a1.remove_child() == False)
a1.stop_attraction()
# when the attraction is stopped, normal rules apply
assert(a1.remove_child() == True)
assert(a1.remove_child() == False)
