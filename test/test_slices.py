raise "This program can't be run"

testme[1]
testme[1] = 1
del testme[1]

testme[:42]
testme[:42] = "The Answer"
del testme[:42]

testme[2:1024:]
testme[:1024:10]
testme[::]
testme[2:1024:10]
testme[2:1024:10] = "A lot"
del testme[2:1024:10]

testme[:42, ..., :24:, 24, 100]
testme[:42, ..., :24:, 24, 100] = "Strange"
del testme[:42, ..., :24:, 24, 100]

testme[:]
testme[:] = 'Take all'
del testme[:]

testme[40:42]
testme[40:42] = 'Three'
del testme[40:42]

testme[40,41,42]
testme[40,41,42] = 'Another Three'
del testme[40,41,42]
