from random import uniform
from time import sleep
import sys
flag=1
temp=""
count=1
decrypted_string=""

def logic1(letter):
    global decrypted_string
    # bs logic lgake decrypt krke append krdo decrypted_string m

    #for lowercase
    if letter==chr(34):
        decrypted_string=decrypted_string+"a"
    elif letter==chr(39):
        decrypted_string=decrypted_string+"b"
    elif letter==chr(42):
        decrypted_string=decrypted_string+"c"
    elif letter==chr(45):
        decrypted_string=decrypted_string+"d"
    elif letter==chr(55):
        decrypted_string=decrypted_string+"e"
    elif letter==chr(58):
        decrypted_string=decrypted_string+"f"
    elif letter==chr(60):
        decrypted_string=decrypted_string+"g"
    elif letter==chr(63):
        decrypted_string=decrypted_string+"h"
    elif letter==chr(64):
        decrypted_string=decrypted_string+"i"
    elif letter==chr(69):
        decrypted_string=decrypted_string+"j"
    elif letter==chr(79):
        decrypted_string=decrypted_string+"k"
    elif letter==chr(87):
        decrypted_string=decrypted_string+"l"
    elif letter==chr(92):
        decrypted_string=decrypted_string+"m"
    elif letter==chr(95):
        decrypted_string=decrypted_string+"n"
    elif letter==chr(96):
        decrypted_string=decrypted_string+"o"
    elif letter==chr(100):
        decrypted_string=decrypted_string+"p"
    elif letter==chr(105):
        decrypted_string=decrypted_string+"q"
    elif letter==chr(123):
        decrypted_string=decrypted_string+"r"
    elif letter==chr(127):
        decrypted_string=decrypted_string+"s"
    elif letter==chr(131):
        decrypted_string=decrypted_string+"t"
    elif letter==chr(155):
        decrypted_string=decrypted_string+"u"
    elif letter==chr(175):
        decrypted_string=decrypted_string+"v"
    elif letter==chr(191):
        decrypted_string=decrypted_string+"w"
    elif letter==chr(168):
        decrypted_string=decrypted_string+"x"
    elif letter==chr(142):
        decrypted_string=decrypted_string+"y"
    elif letter==chr(240):
        decrypted_string=decrypted_string+"z"

    # for uppercase

    if letter==chr(33):
        decrypted_string=decrypted_string+"A"
    elif letter==chr(40):
        decrypted_string=decrypted_string+"B"
    elif letter==chr(49):
        decrypted_string=decrypted_string+"C"
    elif letter==chr(65):
        decrypted_string=decrypted_string+"D"
    elif letter==chr(90):
        decrypted_string=decrypted_string+"E"
    elif letter==chr(94):
        decrypted_string=decrypted_string+"F"
    elif letter==chr(107):
        decrypted_string=decrypted_string+"G"
    elif letter==chr(115):
        decrypted_string=decrypted_string+"H"
    elif letter==chr(124):
        decrypted_string=decrypted_string+"I"
    elif letter==chr(126):
        decrypted_string=decrypted_string+"J"
    elif letter==chr(128):
        decrypted_string=decrypted_string+"K"
    elif letter==chr(140):
        decrypted_string=decrypted_string+"L"
    elif letter==chr(158):
        decrypted_string=decrypted_string+"M"
    elif letter==chr(206):
        decrypted_string=decrypted_string+"N"
    elif letter==chr(217):
        decrypted_string=decrypted_string+"O"
    elif letter==chr(239):
        decrypted_string=decrypted_string+"P"
    elif letter==chr(224):
        decrypted_string=decrypted_string+"Q"
    elif letter==chr(228):
        decrypted_string=decrypted_string+"R"
    elif letter==chr(234):
        decrypted_string=decrypted_string+"S"
    elif letter==chr(236):
        decrypted_string=decrypted_string+"T"
    elif letter==chr(242):
        decrypted_string=decrypted_string+"U"
    elif letter==chr(247):
        decrypted_string=decrypted_string+"V"
    elif letter==chr(252):
        decrypted_string=decrypted_string+"W"
    elif letter==chr(255):
        decrypted_string=decrypted_string+"X"
    elif letter==chr(159):
        decrypted_string=decrypted_string+"Y"
    elif letter==chr(174):
        decrypted_string=decrypted_string+"Z"

    # for numbers

    if letter==chr(71):
        decrypted_string=decrypted_string+"0"
    elif letter==chr(82):
        decrypted_string=decrypted_string+"1"
    elif letter==chr(93):
        decrypted_string=decrypted_string+"2"
    elif letter==chr(100):
        decrypted_string=decrypted_string+"3"
    elif letter==chr(125):
        decrypted_string=decrypted_string+"4"
    elif letter==chr(130):
        decrypted_string=decrypted_string+"5"
    elif letter==chr(161):
        decrypted_string=decrypted_string+"6"
    elif letter==chr(203):
        decrypted_string=decrypted_string+"7"
    elif letter==chr(219):
        decrypted_string=decrypted_string+"8"
    elif letter==chr(254):
        decrypted_string=decrypted_string+"9"

    # for symbols
    # for 33-47
    if letter == chr(47):
        decrypted_string = decrypted_string + chr(33)
    elif letter == chr(56):
        decrypted_string = decrypted_string + chr(34)
    elif letter == chr(73):
        decrypted_string = decrypted_string + chr(35)
    elif letter == chr(85):
        decrypted_string = decrypted_string + chr(36)
    elif letter == chr(104):
        decrypted_string = decrypted_string + chr(37)
    elif letter == chr(91):
        decrypted_string = decrypted_string + chr(38)
    elif letter == chr(135):
        decrypted_string = decrypted_string + chr(39)
    elif letter == chr(205):
        decrypted_string = decrypted_string + chr(40)
    elif letter == chr(207):
        decrypted_string = decrypted_string + chr(41)
    elif letter == chr(221):
        decrypted_string = decrypted_string + chr(42)
    elif letter == chr(243):
        decrypted_string = decrypted_string + chr(43)
    elif letter == chr(233):
        decrypted_string = decrypted_string + chr(44)
    elif letter == chr(227):
        decrypted_string = decrypted_string + chr(45)
    elif letter == chr(143):
        decrypted_string = decrypted_string + chr(46)
    elif letter == chr(238):
        decrypted_string = decrypted_string + chr(47)

    # for 58-64
    if letter == chr(44):
        decrypted_string = decrypted_string + chr(58)
    elif letter == chr(53):
        decrypted_string = decrypted_string + chr(59)
    elif letter == chr(66):
        decrypted_string = decrypted_string + chr(60)
    elif letter == chr(84):
        decrypted_string = decrypted_string + chr(61)
    elif letter == chr(108):
        decrypted_string = decrypted_string + chr(62)
    elif letter == chr(121):
        decrypted_string = decrypted_string + chr(63)
    elif letter == chr(144):
        decrypted_string = decrypted_string + chr(64)

    # for 91-96
    if letter == chr(59):
        decrypted_string = decrypted_string + chr(91)
    elif letter == chr(74):
        decrypted_string = decrypted_string + chr(92)
    elif letter == chr(99):
        decrypted_string = decrypted_string + chr(93)
    elif letter == chr(180):
        decrypted_string = decrypted_string + chr(94)
    elif letter == chr(196):
        decrypted_string = decrypted_string + chr(95)
    elif letter == chr(245):
        decrypted_string = decrypted_string + chr(96)

    # for 123-126
    if letter == chr(48):
        decrypted_string = decrypted_string + chr(123)
    elif letter == chr(57):
        decrypted_string = decrypted_string + chr(124)
    elif letter == chr(171):
        decrypted_string = decrypted_string + chr(125)
    elif letter == chr(172):
        decrypted_string = decrypted_string + chr(126)

    return

def logic2(letter):
    global decrypted_string
    # bs logic lgake decrypt krke append krdo decrypted_string m

    # for lowercase
    if letter == chr(253):
        decrypted_string = decrypted_string + "a"
    elif letter == chr(247):
        decrypted_string = decrypted_string + "b"
    elif letter == chr(245):
        decrypted_string = decrypted_string + "c"
    elif letter == chr(235):
        decrypted_string = decrypted_string + "d"
    elif letter == chr(230):
        decrypted_string = decrypted_string + "e"
    elif letter == chr(229):
        decrypted_string = decrypted_string + "f"
    elif letter == chr(200):
        decrypted_string = decrypted_string + "g"
    elif letter == chr(206):
        decrypted_string = decrypted_string + "h"
    elif letter == chr(185):
        decrypted_string = decrypted_string + "i"
    elif letter == chr(191):
        decrypted_string = decrypted_string + "j"
    elif letter == chr(175):
        decrypted_string = decrypted_string + "k"
    elif letter == chr(171):
        decrypted_string = decrypted_string + "l"
    elif letter == chr(161):
        decrypted_string = decrypted_string + "m"
    elif letter == chr(159):
        decrypted_string = decrypted_string + "n"
    elif letter == chr(154):
        decrypted_string = decrypted_string + "o"
    elif letter == chr(146):
        decrypted_string = decrypted_string + "p"
    elif letter == chr(143):
        decrypted_string = decrypted_string + "q"
    elif letter == chr(128):
        decrypted_string = decrypted_string + "r"
    elif letter == chr(125):
        decrypted_string = decrypted_string + "s"
    elif letter == chr(100):
        decrypted_string = decrypted_string + "t"
    elif letter == chr(97):
        decrypted_string = decrypted_string + "u"
    elif letter == chr(91):
        decrypted_string = decrypted_string + "v"
    elif letter == chr(80):
        decrypted_string = decrypted_string + "w"
    elif letter == chr(66):
        decrypted_string = decrypted_string + "x"
    elif letter == chr(64):
        decrypted_string = decrypted_string + "y"
    elif letter == chr(59):
        decrypted_string = decrypted_string + "z"

    # for uppercase

    if letter == chr(255):
        decrypted_string = decrypted_string + "A"
    elif letter == chr(251):
        decrypted_string = decrypted_string + "B"
    elif letter == chr(244):
        decrypted_string = decrypted_string + "C"
    elif letter == chr(240):
        decrypted_string = decrypted_string + "D"
    elif letter == chr(236):
        decrypted_string = decrypted_string + "E"
    elif letter == chr(224):
        decrypted_string = decrypted_string + "F"
    elif letter == chr(219):
        decrypted_string = decrypted_string + "G"
    elif letter == chr(208):
        decrypted_string = decrypted_string + "H"
    elif letter == chr(201):
        decrypted_string = decrypted_string + "I"
    elif letter == chr(186):
        decrypted_string = decrypted_string + "J"
    elif letter == chr(172):
        decrypted_string = decrypted_string + "K"
    elif letter == chr(174):
        decrypted_string = decrypted_string + "L"
    elif letter == chr(168):
        decrypted_string = decrypted_string + "M"
    elif letter == chr(165):
        decrypted_string = decrypted_string + "N"
    elif letter == chr(158):
        decrypted_string = decrypted_string + "O"
    elif letter == chr(148):
        decrypted_string = decrypted_string + "P"
    elif letter == chr(145):
        decrypted_string = decrypted_string + "Q"
    elif letter == chr(135):
        decrypted_string = decrypted_string + "R"
    elif letter == chr(127):
        decrypted_string = decrypted_string + "S"
    elif letter == chr(119):
        decrypted_string = decrypted_string + "T"
    elif letter == chr(94):
        decrypted_string = decrypted_string + "U"
    elif letter == chr(93):
        decrypted_string = decrypted_string + "V"
    elif letter == chr(84):
        decrypted_string = decrypted_string + "W"
    elif letter == chr(63):
        decrypted_string = decrypted_string + "X"
    elif letter == chr(47):
        decrypted_string = decrypted_string + "Y"
    elif letter == chr(42):
        decrypted_string = decrypted_string + "Z"

    # for numbers

    if letter == chr(252):
        decrypted_string = decrypted_string + "0"
    elif letter == chr(243):
        decrypted_string = decrypted_string + "1"
    elif letter == chr(226):
        decrypted_string = decrypted_string + "2"
    elif letter == chr(190):
        decrypted_string = decrypted_string + "3"
    elif letter == chr(179):
        decrypted_string = decrypted_string + "4"
    elif letter == chr(164):
        decrypted_string = decrypted_string + "5"
    elif letter == chr(153):
        decrypted_string = decrypted_string + "6"
    elif letter == chr(144):
        decrypted_string = decrypted_string + "7"
    elif letter == chr(118):
        decrypted_string = decrypted_string + "8"
    elif letter == chr(53):
        decrypted_string = decrypted_string + "9"

    # for symbols
    # for 33-47
    if letter == chr(246):
        decrypted_string = decrypted_string + chr(33)
    elif letter == chr(227):
        decrypted_string = decrypted_string + chr(34)
    elif letter == chr(197):
        decrypted_string = decrypted_string + chr(35)
    elif letter == chr(156):
        decrypted_string = decrypted_string + chr(36)
    elif letter == chr(131):
        decrypted_string = decrypted_string + chr(37)
    elif letter == chr(126):
        decrypted_string = decrypted_string + chr(38)
    elif letter == chr(122):
        decrypted_string = decrypted_string + chr(39)
    elif letter == chr(107):
        decrypted_string = decrypted_string + chr(40)
    elif letter == chr(102):
        decrypted_string = decrypted_string + chr(41)
    elif letter == chr(90):
        decrypted_string = decrypted_string + chr(42)
    elif letter == chr(79):
        decrypted_string = decrypted_string + chr(43)
    elif letter == chr(76):
        decrypted_string = decrypted_string + chr(44)
    elif letter == chr(71):
        decrypted_string = decrypted_string + chr(45)
    elif letter == chr(65):
        decrypted_string = decrypted_string + chr(46)
    elif letter == chr(55):
        decrypted_string = decrypted_string + chr(47)

    # for 58-64
    if letter == chr(239):
        decrypted_string = decrypted_string + chr(58)
    elif letter == chr(222):
        decrypted_string = decrypted_string + chr(59)
    elif letter == chr(123):
        decrypted_string = decrypted_string + chr(60)
    elif letter == chr(114):
        decrypted_string = decrypted_string + chr(61)
    elif letter == chr(86):
        decrypted_string = decrypted_string + chr(62)
    elif letter == chr(69):
        decrypted_string = decrypted_string + chr(63)
    elif letter == chr(56):
        decrypted_string = decrypted_string + chr(64)

    # for 91-96
    if letter == chr(61):
        decrypted_string = decrypted_string + chr(91)
    elif letter == chr(111):
        decrypted_string = decrypted_string + chr(92)
    elif letter == chr(48):
        decrypted_string = decrypted_string + chr(93)
    elif letter == chr(74):
        decrypted_string = decrypted_string + chr(94)
    elif letter == chr(75):
        decrypted_string = decrypted_string + chr(95)
    elif letter == chr(72):
        decrypted_string = decrypted_string + chr(96)

    # for 123-126
    if letter == chr(43):
        decrypted_string = decrypted_string + chr(123)
    elif letter == chr(61):
        decrypted_string = decrypted_string + chr(124)
    elif letter == chr(109):
        decrypted_string = decrypted_string + chr(125)
    elif letter == chr(62):
        decrypted_string = decrypted_string + chr(126)


    return

def logic3(letter):
    global decrypted_string
    # bs logic lgake decrypt krke append krdo decrypted_string m

    # for lowercase
    if letter == chr(90):
        decrypted_string = decrypted_string + "a"
    elif letter == chr(89):
        decrypted_string = decrypted_string + "b"
    elif letter == chr(88):
        decrypted_string = decrypted_string + "c"
    elif letter == chr(87):
        decrypted_string = decrypted_string + "d"
    elif letter == chr(86):
        decrypted_string = decrypted_string + "e"
    elif letter == chr(85):
        decrypted_string = decrypted_string + "f"
    elif letter == chr(84):
        decrypted_string = decrypted_string + "g"
    elif letter == chr(83):
        decrypted_string = decrypted_string + "h"
    elif letter == chr(82):
        decrypted_string = decrypted_string + "i"
    elif letter == chr(81):
        decrypted_string = decrypted_string + "j"
    elif letter == chr(80):
        decrypted_string = decrypted_string + "k"
    elif letter == chr(79):
        decrypted_string = decrypted_string + "l"
    elif letter == chr(78):
        decrypted_string = decrypted_string + "m"
    elif letter == chr(77):
        decrypted_string = decrypted_string + "n"
    elif letter == chr(76):
        decrypted_string = decrypted_string + "o"
    elif letter == chr(75):
        decrypted_string = decrypted_string + "p"
    elif letter == chr(74):
        decrypted_string = decrypted_string + "q"
    elif letter == chr(73):
        decrypted_string = decrypted_string + "r"
    elif letter == chr(72):
        decrypted_string = decrypted_string + "s"
    elif letter == chr(71):
        decrypted_string = decrypted_string + "t"
    elif letter == chr(70):
        decrypted_string = decrypted_string + "u"
    elif letter == chr(69):
        decrypted_string = decrypted_string + "v"
    elif letter == chr(68):
        decrypted_string = decrypted_string + "w"
    elif letter == chr(67):
        decrypted_string = decrypted_string + "x"
    elif letter == chr(66):
        decrypted_string = decrypted_string + "y"
    elif letter == chr(65):
        decrypted_string = decrypted_string + "z"

    # for uppercase

    if letter == chr(122):
        decrypted_string = decrypted_string + "A"
    elif letter == chr(121):
        decrypted_string = decrypted_string + "B"
    elif letter == chr(120):
        decrypted_string = decrypted_string + "C"
    elif letter == chr(119):
        decrypted_string = decrypted_string + "D"
    elif letter == chr(118):
        decrypted_string = decrypted_string + "E"
    elif letter == chr(117):
        decrypted_string = decrypted_string + "F"
    elif letter == chr(116):
        decrypted_string = decrypted_string + "G"
    elif letter == chr(115):
        decrypted_string = decrypted_string + "H"
    elif letter == chr(114):
        decrypted_string = decrypted_string + "I"
    elif letter == chr(113):
        decrypted_string = decrypted_string + "J"
    elif letter == chr(112):
        decrypted_string = decrypted_string + "K"
    elif letter == chr(111):
        decrypted_string = decrypted_string + "L"
    elif letter == chr(110):
        decrypted_string = decrypted_string + "M"
    elif letter == chr(109):
        decrypted_string = decrypted_string + "N"
    elif letter == chr(108):
        decrypted_string = decrypted_string + "O"
    elif letter == chr(107):
        decrypted_string = decrypted_string + "P"
    elif letter == chr(106):
        decrypted_string = decrypted_string + "Q"
    elif letter == chr(105):
        decrypted_string = decrypted_string + "R"
    elif letter == chr(104):
        decrypted_string = decrypted_string + "S"
    elif letter == chr(103):
        decrypted_string = decrypted_string + "T"
    elif letter == chr(102):
        decrypted_string = decrypted_string + "U"
    elif letter == chr(101):
        decrypted_string = decrypted_string + "V"
    elif letter == chr(100):
        decrypted_string = decrypted_string + "W"
    elif letter == chr(99):
        decrypted_string = decrypted_string + "X"
    elif letter == chr(98):
        decrypted_string = decrypted_string + "Y"
    elif letter == chr(97):
        decrypted_string = decrypted_string + "Z"

    # for numbers

    if letter == chr(255):
        decrypted_string = decrypted_string + "0"
    elif letter == chr(245):
        decrypted_string = decrypted_string + "1"
    elif letter == chr(227):
        decrypted_string = decrypted_string + "2"
    elif letter == chr(211):
        decrypted_string = decrypted_string + "3"
    elif letter == chr(199):
        decrypted_string = decrypted_string + "4"
    elif letter == chr(186):
        decrypted_string = decrypted_string + "5"
    elif letter == chr(172):
        decrypted_string = decrypted_string + "6"
    elif letter == chr(165):
        decrypted_string = decrypted_string + "7"
    elif letter == chr(154):
        decrypted_string = decrypted_string + "8"
    elif letter == chr(143):
        decrypted_string = decrypted_string + "9"

    # for symbols
    # for 33-47
    if letter == chr(48):
        decrypted_string = decrypted_string + chr(33)
    elif letter == chr(57):
        decrypted_string = decrypted_string + chr(34)
    elif letter == chr(49):
        decrypted_string = decrypted_string + chr(35)
    elif letter == chr(142):
        decrypted_string = decrypted_string + chr(36)
    elif letter == chr(50):
        decrypted_string = decrypted_string + chr(37)
    elif letter == chr(159):
        decrypted_string = decrypted_string + chr(38)
    elif letter == chr(224):
        decrypted_string = decrypted_string + chr(39)
    elif letter == chr(51):
        decrypted_string = decrypted_string + chr(40)
    elif letter == chr(206):
        decrypted_string = decrypted_string + chr(41)
    elif letter == chr(52):
        decrypted_string = decrypted_string + chr(42)
    elif letter == chr(237):
        decrypted_string = decrypted_string + chr(43)
    elif letter == chr(53):
        decrypted_string = decrypted_string + chr(44)
    elif letter == chr(54):
        decrypted_string = decrypted_string + chr(45)
    elif letter == chr(55):
        decrypted_string = decrypted_string + chr(46)
    elif letter == chr(56):
        decrypted_string = decrypted_string + chr(47)

    # for 58-64
    if letter == chr(222):
        decrypted_string = decrypted_string + chr(58)
    elif letter == chr(47):
        decrypted_string = decrypted_string + chr(59)
    elif letter == chr(43):
        decrypted_string = decrypted_string + chr(60)
    elif letter == chr(45):
        decrypted_string = decrypted_string + chr(61)
    elif letter == chr(40):
        decrypted_string = decrypted_string + chr(62)
    elif letter == chr(33):
        decrypted_string = decrypted_string + chr(63)
    elif letter == chr(41):
        decrypted_string = decrypted_string + chr(64)

    # for 91-96
    if letter == chr(62):
        decrypted_string = decrypted_string + chr(91)
    elif letter == chr(59):
        decrypted_string = decrypted_string + chr(92)
    elif letter == chr(63):
        decrypted_string = decrypted_string + chr(93)
    elif letter == chr(58):
        decrypted_string = decrypted_string + chr(94)
    elif letter == chr(64):
        decrypted_string = decrypted_string + chr(95)
    elif letter == chr(62):
        decrypted_string = decrypted_string + chr(96)

    # for 123-126
    if letter == chr(94):
        decrypted_string = decrypted_string + chr(123)
    elif letter == chr(92):
        decrypted_string = decrypted_string + chr(124)
    elif letter == chr(95):
        decrypted_string = decrypted_string + chr(125)
    elif letter == chr(91):
        decrypted_string = decrypted_string + chr(126)


    return

def logic4(letter):
    global decrypted_string
    # bs logic lgake decrypt krke append krdo decrypted_string m

    # for lowercase
    if letter == chr(48):
        decrypted_string = decrypted_string + "a"
    elif letter == chr(33):
        decrypted_string = decrypted_string + "b"
    elif letter == chr(58):
        decrypted_string = decrypted_string + "c"
    elif letter == chr(62):
        decrypted_string = decrypted_string + "d"
    elif letter == chr(49):
        decrypted_string = decrypted_string + "e"
    elif letter == chr(34):
        decrypted_string = decrypted_string + "f"
    elif letter == chr(61):
        decrypted_string = decrypted_string + "g"
    elif letter == chr(43):
        decrypted_string = decrypted_string + "h"
    elif letter == chr(50):
        decrypted_string = decrypted_string + "i"
    elif letter == chr(63):
        decrypted_string = decrypted_string + "j"
    elif letter == chr(51):
        decrypted_string = decrypted_string + "k"
    elif letter == chr(128):
        decrypted_string = decrypted_string + "l"
    elif letter == chr(52):
        decrypted_string = decrypted_string + "m"
    elif letter == chr(53):
        decrypted_string = decrypted_string + "n"
    elif letter == chr(54):
        decrypted_string = decrypted_string + "o"
    elif letter == chr(59):
        decrypted_string = decrypted_string + "p"
    elif letter == chr(64):
        decrypted_string = decrypted_string + "q"
    elif letter == chr(41):
        decrypted_string = decrypted_string + "r"
    elif letter == chr(60):
        decrypted_string = decrypted_string + "s"
    elif letter == chr(55):
        decrypted_string = decrypted_string + "t"
    elif letter == chr(47):
        decrypted_string = decrypted_string + "u"
    elif letter == chr(56):
        decrypted_string = decrypted_string + "v"
    elif letter == chr(40):
        decrypted_string = decrypted_string + "w"
    elif letter == chr(42):
        decrypted_string = decrypted_string + "x"
    elif letter == chr(57):
        decrypted_string = decrypted_string + "y"
    elif letter == chr(44):
        decrypted_string = decrypted_string + "z"

    # for uppercase

    if letter == chr(101):
        decrypted_string = decrypted_string + "A"
    elif letter == chr(107):
        decrypted_string = decrypted_string + "B"
    elif letter == chr(91):
        decrypted_string = decrypted_string + "C"
    elif letter == chr(97):
        decrypted_string = decrypted_string + "D"
    elif letter == chr(92):
        decrypted_string = decrypted_string + "E"
    elif letter == chr(93):
        decrypted_string = decrypted_string + "F"
    elif letter == chr(108):
        decrypted_string = decrypted_string + "G"
    elif letter == chr(94):
        decrypted_string = decrypted_string + "H"
    elif letter == chr(95):
        decrypted_string = decrypted_string + "I"
    elif letter == chr(96):
        decrypted_string = decrypted_string + "J"
    elif letter == chr(110):
        decrypted_string = decrypted_string + "K"
    elif letter == chr(98):
        decrypted_string = decrypted_string + "L"
    elif letter == chr(123):
        decrypted_string = decrypted_string + "M"
    elif letter == chr(102):
        decrypted_string = decrypted_string + "N"
    elif letter == chr(124):
        decrypted_string = decrypted_string + "O"
    elif letter == chr(99):
        decrypted_string = decrypted_string + "P"
    elif letter == chr(105):
        decrypted_string = decrypted_string + "Q"
    elif letter == chr(127):
        decrypted_string = decrypted_string + "R"
    elif letter == chr(109):
        decrypted_string = decrypted_string + "S"
    elif letter == chr(104):
        decrypted_string = decrypted_string + "T"
    elif letter == chr(111):
        decrypted_string = decrypted_string + "U"
    elif letter == chr(106):
        decrypted_string = decrypted_string + "V"
    elif letter == chr(100):
        decrypted_string = decrypted_string + "W"
    elif letter == chr(125):
        decrypted_string = decrypted_string + "X"
    elif letter == chr(103):
        decrypted_string = decrypted_string + "Y"
    elif letter == chr(126):
        decrypted_string = decrypted_string + "Z"

    # for numbers

    if letter == chr(113):
        decrypted_string = decrypted_string + "0"
    elif letter == chr(65):
        decrypted_string = decrypted_string + "1"
    elif letter == chr(68):
        decrypted_string = decrypted_string + "2"
    elif letter == chr(112):
        decrypted_string = decrypted_string + "3"
    elif letter == chr(114):
        decrypted_string = decrypted_string + "4"
    elif letter == chr(69):
        decrypted_string = decrypted_string + "5"
    elif letter == chr(116):
        decrypted_string = decrypted_string + "6"
    elif letter == chr(66):
        decrypted_string = decrypted_string + "7"
    elif letter == chr(67):
        decrypted_string = decrypted_string + "8"
    elif letter == chr(115):
        decrypted_string = decrypted_string + "9"

    # for symbols
    # for 33-47
    if letter == chr(79):
        decrypted_string = decrypted_string + chr(33)
    elif letter == chr(71):
        decrypted_string = decrypted_string + chr(34)
    elif letter == chr(117):
        decrypted_string = decrypted_string + chr(35)
    elif letter == chr(75):
        decrypted_string = decrypted_string + chr(36)
    elif letter == chr(76):
        decrypted_string = decrypted_string + chr(37)
    elif letter == chr(118):
        decrypted_string = decrypted_string + chr(38)
    elif letter == chr(72):
        decrypted_string = decrypted_string + chr(39)
    elif letter == chr(77):
        decrypted_string = decrypted_string + chr(40)
    elif letter == chr(119):
        decrypted_string = decrypted_string + chr(41)
    elif letter == chr(78):
        decrypted_string = decrypted_string + chr(42)
    elif letter == chr(73):
        decrypted_string = decrypted_string + chr(43)
    elif letter == chr(120):
        decrypted_string = decrypted_string + chr(44)
    elif letter == chr(74):
        decrypted_string = decrypted_string + chr(45)
    elif letter == chr(70):
        decrypted_string = decrypted_string + chr(46)
    elif letter == chr(121):
        decrypted_string = decrypted_string + chr(47)

    # for 58-64
    if letter == chr(83):
        decrypted_string = decrypted_string + chr(58)
    elif letter == chr(80):
        decrypted_string = decrypted_string + chr(59)
    elif letter == chr(85):
        decrypted_string = decrypted_string + chr(60)
    elif letter == chr(81):
        decrypted_string = decrypted_string + chr(61)
    elif letter == chr(84):
        decrypted_string = decrypted_string + chr(62)
    elif letter == chr(82):
        decrypted_string = decrypted_string + chr(63)
    elif letter == chr(122):
        decrypted_string = decrypted_string + chr(64)

    # for 91-96
    if letter == chr(89):
        decrypted_string = decrypted_string + chr(91)
    elif letter == chr(87):
        decrypted_string = decrypted_string + chr(92)
    elif letter == chr(165):
        decrypted_string = decrypted_string + chr(93)
    elif letter == chr(88):
        decrypted_string = decrypted_string + chr(94)
    elif letter == chr(90):
        decrypted_string = decrypted_string + chr(95)
    elif letter == chr(86):
        decrypted_string = decrypted_string + chr(96)

    # for 123-126
    if letter == chr(236):
        decrypted_string = decrypted_string + chr(123)
    elif letter == chr(239):
        decrypted_string = decrypted_string + chr(124)
    elif letter == chr(244):
        decrypted_string = decrypted_string + chr(125)
    elif letter == chr(247):
        decrypted_string = decrypted_string + chr(126)

    return

def into_letters(raw_string):
   for raw_letter in raw_string:
       global decrypted_string
       global count
       global flag
       global temp

       if raw_letter==chr(10000):
           if flag==1:
               pass
           else:
               decrypted_string=decrypted_string +" "
       elif raw_letter==chr(10001):
           # typewriter effect k liye

           for t in decrypted_string:
               print(t,end="")
               sleep(uniform(0,0.3))
           print()
           decrypted_string=""
       else:
           flag=0
           count+=1

           if count%2==0:
               temp=raw_letter

           elif raw_letter == '#':
               logic1(temp)

           elif raw_letter == "$":
               logic2(temp)

           elif raw_letter == "%":
               logic3(temp)

           elif raw_letter == "&":
               logic4(temp)


   return

def takedata():
    raw_string=""
    raw_string=input()
    print()
    print("YOUR MESSAGE IS :-")
    print()
    into_letters(raw_string)

# takedata() ko call krre with some effects

effect="ACCESS GRANTED..."
password=input("Enter password to access : ")
if(password=="aadharjain2002d"):
    for w in effect:
        print(w,end="")
        sys.stdout.flush()
        sleep(0.1)
    print()
    print()
    print("Enter the Encrypted data :-")
    takedata()
else:
    print("ACCESS DENIED!")