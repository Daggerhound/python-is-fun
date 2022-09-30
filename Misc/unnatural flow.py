"""
test  gets passed to lambda right above
which then returns  "5"
which then is passed to lambda above it
which returns  "5" + "5"  aka  "55"
then thats passed into  int  becoming  55
which gets passed into lambda above and that returns  [55, "5"]
which gets passed into lambda above and that returns  [55, int("5" + "0")]  which is  [55, int("50")]  which is  [55, 50]
which then gets passed into lambda above and that returns  [chr(55), chr(50)]  which is  ["7", "2"]  cause of ascii table
which then gets passed into  "".join  above and that returns  "72"
which then gets passed into  int  above and that returns  72
which then gets passed into  chr  above and that returns  "H"
"""
@print
@chr
@int
@"".join
@lambda _: map(chr, _)
@lambda _: [_[0], int(_[1] + "0")]
@lambda _: [_, "5"]
@int
@lambda _: "5" + _
@lambda _: "5"
def test():
    pass