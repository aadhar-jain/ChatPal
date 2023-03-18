import random
from time import sleep
import sys
encrypted_string=""
def logic_one(raw_letter):
    #yha phela logic lgake ie compare krke hatho hath un do letters ko append kr dege in b

    global encrypted_string
    # for lowercase
    if raw_letter==chr(97):
        encrypted_string=encrypted_string+chr(34)+"#"
    elif raw_letter==chr(98):
        encrypted_string=encrypted_string+chr(39)+"#"
    elif raw_letter==chr(99):
        encrypted_string=encrypted_string+chr(42)+"#"
    elif raw_letter==chr(100):
        encrypted_string=encrypted_string+chr(45)+"#"
    elif raw_letter==chr(101):
        encrypted_string=encrypted_string+chr(55)+"#"
    elif raw_letter==chr(102):
        encrypted_string=encrypted_string+chr(58)+"#"
    elif raw_letter==chr(103):
        encrypted_string=encrypted_string+chr(60)+"#"
    elif raw_letter==chr(104):
        encrypted_string=encrypted_string+chr(63)+"#"
    elif raw_letter==chr(105):
        encrypted_string=encrypted_string+chr(64)+"#"
    elif raw_letter==chr(106):
        encrypted_string=encrypted_string+chr(69)+"#"
    elif raw_letter==chr(107):
        encrypted_string=encrypted_string+chr(79)+"#"
    elif raw_letter==chr(108):
        encrypted_string=encrypted_string+chr(87)+"#"
    elif raw_letter==chr(109):
        encrypted_string=encrypted_string+chr(92)+"#"
    elif raw_letter==chr(110):
        encrypted_string=encrypted_string+chr(95)+"#"
    elif raw_letter==chr(111):
        encrypted_string=encrypted_string+chr(96)+"#"
    elif raw_letter==chr(112):
        encrypted_string=encrypted_string+chr(100)+"#"
    elif raw_letter==chr(113):
        encrypted_string=encrypted_string+chr(105)+"#"
    elif raw_letter==chr(114):
        encrypted_string=encrypted_string+chr(123)+"#"
    elif raw_letter==chr(115):
        encrypted_string=encrypted_string+chr(127)+"#"
    elif raw_letter==chr(116):
        encrypted_string=encrypted_string+chr(131)+"#"
    elif raw_letter==chr(117):
        encrypted_string=encrypted_string+chr(155)+"#"
    elif raw_letter==chr(118):
        encrypted_string=encrypted_string+chr(175)+"#"
    elif raw_letter==chr(119):
        encrypted_string=encrypted_string+chr(191)+"#"
    elif raw_letter==chr(120):
        encrypted_string=encrypted_string+chr(168)+"#"
    elif raw_letter==chr(121):
        encrypted_string=encrypted_string+chr(142)+"#"
    elif raw_letter==chr(122):
        encrypted_string=encrypted_string+chr(240)+"#"
    # for uppercase
    elif raw_letter==chr(65):
        encrypted_string=encrypted_string+chr(33)+"#"
    elif raw_letter==chr(66):
        encrypted_string=encrypted_string+chr(40)+"#"
    elif raw_letter==chr(67):
        encrypted_string=encrypted_string+chr(49)+"#"
    elif raw_letter==chr(68):
        encrypted_string=encrypted_string+chr(65)+"#"
    elif raw_letter==chr(69):
        encrypted_string=encrypted_string+chr(90)+"#"
    elif raw_letter==chr(70):
        encrypted_string=encrypted_string+chr(94)+"#"
    elif raw_letter==chr(71):
        encrypted_string=encrypted_string+chr(107)+"#"
    elif raw_letter==chr(72):
        encrypted_string=encrypted_string+chr(115)+"#"
    elif raw_letter==chr(73):
        encrypted_string=encrypted_string+chr(124)+"#"
    elif raw_letter==chr(74):
        encrypted_string=encrypted_string+chr(126)+"#"
    elif raw_letter==chr(75):
        encrypted_string=encrypted_string+chr(128)+"#"
    elif raw_letter==chr(76):
        encrypted_string=encrypted_string+chr(140)+"#"
    elif raw_letter==chr(77):
        encrypted_string=encrypted_string+chr(158)+"#"
    elif raw_letter==chr(78):
        encrypted_string=encrypted_string+chr(206)+"#"
    elif raw_letter==chr(79):
        encrypted_string=encrypted_string+chr(217)+"#"
    elif raw_letter==chr(80):
        encrypted_string=encrypted_string+chr(239)+"#"
    elif raw_letter==chr(81):
        encrypted_string=encrypted_string+chr(224)+"#"
    elif raw_letter==chr(82):
        encrypted_string=encrypted_string+chr(228)+"#"
    elif raw_letter==chr(83):
        encrypted_string=encrypted_string+chr(234)+"#"
    elif raw_letter==chr(84):
        encrypted_string=encrypted_string+chr(236)+"#"
    elif raw_letter==chr(85):
        encrypted_string=encrypted_string+chr(242)+"#"
    elif raw_letter==chr(86):
        encrypted_string=encrypted_string+chr(247)+"#"
    elif raw_letter==chr(87):
        encrypted_string=encrypted_string+chr(252)+"#"
    elif raw_letter==chr(88):
        encrypted_string=encrypted_string+chr(255)+"#"
    elif raw_letter==chr(89):
        encrypted_string=encrypted_string+chr(159)+"#"
    elif raw_letter==chr(90):
        encrypted_string=encrypted_string+chr(174)+"#"
    # for numbers
    elif raw_letter == chr(48):
        encrypted_string = encrypted_string + chr(71) + "#"
    elif raw_letter == chr(49):
        encrypted_string = encrypted_string + chr(82) + "#"
    elif raw_letter == chr(50):
        encrypted_string = encrypted_string + chr(93) + "#"
    elif raw_letter == chr(51):
        encrypted_string = encrypted_string + chr(100) + "#"
    elif raw_letter == chr(52):
        encrypted_string = encrypted_string + chr(125) + "#"
    elif raw_letter == chr(53):
        encrypted_string = encrypted_string + chr(130) + "#"
    elif raw_letter == chr(54):
        encrypted_string = encrypted_string + chr(161) + "#"
    elif raw_letter == chr(55):
        encrypted_string = encrypted_string + chr(203) + "#"
    elif raw_letter == chr(56):
        encrypted_string = encrypted_string + chr(219) + "#"
    elif raw_letter == chr(57):
        encrypted_string = encrypted_string + chr(254) + "#"
    # for remaining symbols intervals
    # 33-47
    elif raw_letter == chr(33):
        encrypted_string = encrypted_string + chr(47) + "#"
    elif raw_letter == chr(34):
        encrypted_string = encrypted_string + chr(56) + "#"
    elif raw_letter == chr(35):
        encrypted_string = encrypted_string + chr(73) + "#"
    elif raw_letter == chr(36):
        encrypted_string = encrypted_string + chr(85) + "#"
    elif raw_letter == chr(37):
        encrypted_string = encrypted_string + chr(104) + "#"
    elif raw_letter == chr(38):
        encrypted_string = encrypted_string + chr(91) + "#"
    elif raw_letter == chr(39):
        encrypted_string = encrypted_string + chr(135) + "#"
    elif raw_letter == chr(40):
        encrypted_string = encrypted_string + chr(205) + "#"
    elif raw_letter == chr(41):
        encrypted_string = encrypted_string + chr(207) + "#"
    elif raw_letter == chr(42):
        encrypted_string = encrypted_string + chr(221) + "#"
    elif raw_letter == chr(43):
        encrypted_string = encrypted_string + chr(243) + "#"
    elif raw_letter == chr(44):
        encrypted_string = encrypted_string + chr(233) + "#"
    elif raw_letter == chr(45):
        encrypted_string = encrypted_string + chr(227) + "#"
    elif raw_letter == chr(46):
        encrypted_string = encrypted_string + chr(143) + "#"
    elif raw_letter == chr(47):
        encrypted_string = encrypted_string + chr(238) + "#"
   # 58-64
    elif raw_letter == chr(58):
        encrypted_string = encrypted_string + chr(44) + "#"
    elif raw_letter == chr(59):
        encrypted_string = encrypted_string + chr(53) + "#"
    elif raw_letter == chr(60):
        encrypted_string = encrypted_string + chr(66) + "#"
    elif raw_letter == chr(61):
        encrypted_string = encrypted_string + chr(84) + "#"
    elif raw_letter == chr(62):
        encrypted_string = encrypted_string + chr(108) + "#"
    elif raw_letter == chr(63):
        encrypted_string = encrypted_string + chr(121) + "#"
    elif raw_letter == chr(64):
        encrypted_string = encrypted_string + chr(144) + "#"

   # 91-96
    elif raw_letter == chr(91):
        encrypted_string = encrypted_string + chr(59) + "#"
    elif raw_letter == chr(92):
        encrypted_string = encrypted_string + chr(74) + "#"
    elif raw_letter == chr(93):
        encrypted_string = encrypted_string + chr(99) + "#"
    elif raw_letter == chr(94):
        encrypted_string = encrypted_string + chr(180) + "#"
    elif raw_letter == chr(95):
        encrypted_string = encrypted_string + chr(196) + "#"
    elif raw_letter == chr(96):
        encrypted_string = encrypted_string + chr(245) + "#"

    # 123-126
    elif raw_letter == chr(123):
        encrypted_string = encrypted_string + chr(48) + "#"
    elif raw_letter == chr(124):
        encrypted_string = encrypted_string + chr(57) + "#"
    elif raw_letter == chr(125):
        encrypted_string = encrypted_string + chr(171) + "#"
    elif raw_letter == chr(126):
        encrypted_string = encrypted_string + chr(172) + "#"

   # end of logic 1
    return

def logic_two(raw_letter):
    # yha dusra logic lgake aur un do letters ko append kr dege in encrypted_string
    global encrypted_string
    # for lowercase
    if raw_letter == chr(97):
        encrypted_string = encrypted_string + chr(253) + "$"
    elif raw_letter == chr(98):
        encrypted_string = encrypted_string + chr(247) + "$"
    elif raw_letter == chr(99):
        encrypted_string = encrypted_string + chr(245) + "$"
    elif raw_letter == chr(100):
        encrypted_string = encrypted_string + chr(235) + "$"
    elif raw_letter == chr(101):
        encrypted_string = encrypted_string + chr(230) + "$"
    elif raw_letter == chr(102):
        encrypted_string = encrypted_string + chr(229) + "$"
    elif raw_letter == chr(103):
        encrypted_string = encrypted_string + chr(200) + "$"
    elif raw_letter == chr(104):
        encrypted_string = encrypted_string + chr(206) + "$"
    elif raw_letter == chr(105):
        encrypted_string = encrypted_string + chr(185) + "$"
    elif raw_letter == chr(106):
        encrypted_string = encrypted_string + chr(191) + "$"
    elif raw_letter == chr(107):
        encrypted_string = encrypted_string + chr(175) + "$"
    elif raw_letter == chr(108):
        encrypted_string = encrypted_string + chr(171) + "$"
    elif raw_letter == chr(109):
        encrypted_string = encrypted_string + chr(161) + "$"
    elif raw_letter == chr(110):
        encrypted_string = encrypted_string + chr(159) + "$"
    elif raw_letter == chr(111):
        encrypted_string = encrypted_string + chr(154) + "$"
    elif raw_letter == chr(112):
        encrypted_string = encrypted_string + chr(146) + "$"
    elif raw_letter == chr(113):
        encrypted_string = encrypted_string + chr(143) + "$"
    elif raw_letter == chr(114):
        encrypted_string = encrypted_string + chr(128) + "$"
    elif raw_letter == chr(115):
        encrypted_string = encrypted_string + chr(125) + "$"
    elif raw_letter == chr(116):
        encrypted_string = encrypted_string + chr(100) + "$"
    elif raw_letter == chr(117):
        encrypted_string = encrypted_string + chr(97) + "$"
    elif raw_letter == chr(118):
        encrypted_string = encrypted_string + chr(91) + "$"
    elif raw_letter == chr(119):
        encrypted_string = encrypted_string + chr(80) + "$"
    elif raw_letter == chr(120):
        encrypted_string = encrypted_string + chr(66) + "$"
    elif raw_letter == chr(121):
        encrypted_string = encrypted_string + chr(64) + "$"
    elif raw_letter == chr(122):
        encrypted_string = encrypted_string + chr(59) + "$"
    # for uppercase
    elif raw_letter == chr(65):
        encrypted_string = encrypted_string + chr(255) + "$"
    elif raw_letter == chr(66):
        encrypted_string = encrypted_string + chr(251) + "$"
    elif raw_letter == chr(67):
        encrypted_string = encrypted_string + chr(244) + "$"
    elif raw_letter == chr(68):
        encrypted_string = encrypted_string + chr(240) + "$"
    elif raw_letter == chr(69):
        encrypted_string = encrypted_string + chr(236) + "$"
    elif raw_letter == chr(70):
        encrypted_string = encrypted_string + chr(224) + "$"
    elif raw_letter == chr(71):
        encrypted_string = encrypted_string + chr(219) + "$"
    elif raw_letter == chr(72):
        encrypted_string = encrypted_string + chr(208) + "$"
    elif raw_letter == chr(73):
        encrypted_string = encrypted_string + chr(201) + "$"
    elif raw_letter == chr(74):
        encrypted_string = encrypted_string + chr(186) + "$"
    elif raw_letter == chr(75):
        encrypted_string = encrypted_string + chr(172) + "$"
    elif raw_letter == chr(76):
        encrypted_string = encrypted_string + chr(174) + "$"
    elif raw_letter == chr(77):
        encrypted_string = encrypted_string + chr(168) + "$"
    elif raw_letter == chr(78):
        encrypted_string = encrypted_string + chr(165) + "$"
    elif raw_letter == chr(79):
        encrypted_string = encrypted_string + chr(158) + "$"
    elif raw_letter == chr(80):
        encrypted_string = encrypted_string + chr(148) + "$"
    elif raw_letter == chr(81):
        encrypted_string = encrypted_string + chr(145) + "$"
    elif raw_letter == chr(82):
        encrypted_string = encrypted_string + chr(135) + "$"
    elif raw_letter == chr(83):
        encrypted_string = encrypted_string + chr(127) + "$"
    elif raw_letter == chr(84):
        encrypted_string = encrypted_string + chr(119) + "$"
    elif raw_letter == chr(85):
        encrypted_string = encrypted_string + chr(94) + "$"
    elif raw_letter == chr(86):
        encrypted_string = encrypted_string + chr(93) + "$"
    elif raw_letter == chr(87):
        encrypted_string = encrypted_string + chr(84) + "$"
    elif raw_letter == chr(88):
        encrypted_string = encrypted_string + chr(63) + "$"
    elif raw_letter == chr(89):
        encrypted_string = encrypted_string + chr(47) + "$"
    elif raw_letter == chr(90):
        encrypted_string = encrypted_string + chr(42) + "$"
    # for numbers
    elif raw_letter == chr(48):
        encrypted_string = encrypted_string + chr(252) + "$"
    elif raw_letter == chr(49):
        encrypted_string = encrypted_string + chr(243) + "$"
    elif raw_letter == chr(50):
        encrypted_string = encrypted_string + chr(226) + "$"
    elif raw_letter == chr(51):
        encrypted_string = encrypted_string + chr(190) + "$"
    elif raw_letter == chr(52):
        encrypted_string = encrypted_string + chr(179) + "$"
    elif raw_letter == chr(53):
        encrypted_string = encrypted_string + chr(164) + "$"
    elif raw_letter == chr(54):
        encrypted_string = encrypted_string + chr(153) + "$"
    elif raw_letter == chr(55):
        encrypted_string = encrypted_string + chr(144) + "$"
    elif raw_letter == chr(56):
        encrypted_string = encrypted_string + chr(118) + "$"
    elif raw_letter == chr(57):
        encrypted_string = encrypted_string + chr(53) + "$"
    # for remaining symbols intervals
    # 33-47
    elif raw_letter == chr(33):
        encrypted_string = encrypted_string + chr(246) + "$"
    elif raw_letter == chr(34):
        encrypted_string = encrypted_string + chr(227) + "$"
    elif raw_letter == chr(35):
        encrypted_string = encrypted_string + chr(197) + "$"
    elif raw_letter == chr(36):
        encrypted_string = encrypted_string + chr(156) + "$"
    elif raw_letter == chr(37):
        encrypted_string = encrypted_string + chr(131) + "$"
    elif raw_letter == chr(38):
        encrypted_string = encrypted_string + chr(126) + "$"
    elif raw_letter == chr(39):
        encrypted_string = encrypted_string + chr(122) + "$"
    elif raw_letter == chr(40):
        encrypted_string = encrypted_string + chr(107) + "$"
    elif raw_letter == chr(41):
        encrypted_string = encrypted_string + chr(102) + "$"
    elif raw_letter == chr(42):
        encrypted_string = encrypted_string + chr(90) + "$"
    elif raw_letter == chr(43):
        encrypted_string = encrypted_string + chr(79) + "$"
    elif raw_letter == chr(44):
        encrypted_string = encrypted_string + chr(76) + "$"
    elif raw_letter == chr(45):
        encrypted_string = encrypted_string + chr(71) + "$"
    elif raw_letter == chr(46):
        encrypted_string = encrypted_string + chr(65) + "$"
    elif raw_letter == chr(47):
        encrypted_string = encrypted_string + chr(55) + "$"
    # 58-64
    elif raw_letter == chr(58):
        encrypted_string = encrypted_string + chr(239) + "$"
    elif raw_letter == chr(59):
        encrypted_string = encrypted_string + chr(222) + "$"
    elif raw_letter == chr(60):
        encrypted_string = encrypted_string + chr(123) + "$"
    elif raw_letter == chr(61):
        encrypted_string = encrypted_string + chr(114) + "$"
    elif raw_letter == chr(62):
        encrypted_string = encrypted_string + chr(86) + "$"
    elif raw_letter == chr(63):
        encrypted_string = encrypted_string + chr(69) + "$"
    elif raw_letter == chr(64):
        encrypted_string = encrypted_string + chr(56) + "$"

    # 91-96
    elif raw_letter == chr(91):
        encrypted_string = encrypted_string + chr(61) + "$"
    elif raw_letter == chr(92):
        encrypted_string = encrypted_string + chr(111) + "$"
    elif raw_letter == chr(93):
        encrypted_string = encrypted_string + chr(48) + "$"
    elif raw_letter == chr(94):
        encrypted_string = encrypted_string + chr(74) + "$"
    elif raw_letter == chr(95):
        encrypted_string = encrypted_string + chr(75) + "$"
    elif raw_letter == chr(96):
        encrypted_string = encrypted_string + chr(72) + "$"

    # 123-126
    elif raw_letter == chr(123):
        encrypted_string = encrypted_string + chr(43) + "$"
    elif raw_letter == chr(124):
        encrypted_string = encrypted_string + chr(61) + "$"
    elif raw_letter == chr(125):
        encrypted_string = encrypted_string + chr(109) + "$"
    elif raw_letter == chr(126):
        encrypted_string = encrypted_string + chr(62) + "$"

    # end of logic 2
    return

def logic_three(raw_letter):
    # yha teesra logic lgake aur un do letters ko append kr dege in encrypted_string
    global encrypted_string
    # for lowercase
    if raw_letter == chr(97):
        encrypted_string = encrypted_string + chr(90) + "%"
    elif raw_letter == chr(98):
        encrypted_string = encrypted_string + chr(89) + "%"
    elif raw_letter == chr(99):
        encrypted_string = encrypted_string + chr(88) + "%"
    elif raw_letter == chr(100):
        encrypted_string = encrypted_string + chr(87) + "%"
    elif raw_letter == chr(101):
        encrypted_string = encrypted_string + chr(86) + "%"
    elif raw_letter == chr(102):
        encrypted_string = encrypted_string + chr(85) + "%"
    elif raw_letter == chr(103):
        encrypted_string = encrypted_string + chr(84) + "%"
    elif raw_letter == chr(104):
        encrypted_string = encrypted_string + chr(83) + "%"
    elif raw_letter == chr(105):
        encrypted_string = encrypted_string + chr(82) + "%"
    elif raw_letter == chr(106):
        encrypted_string = encrypted_string + chr(81) + "%"
    elif raw_letter == chr(107):
        encrypted_string = encrypted_string + chr(80) + "%"
    elif raw_letter == chr(108):
        encrypted_string = encrypted_string + chr(79) + "%"
    elif raw_letter == chr(109):
        encrypted_string = encrypted_string + chr(78) + "%"
    elif raw_letter == chr(110):
        encrypted_string = encrypted_string + chr(77) + "%"
    elif raw_letter == chr(111):
        encrypted_string = encrypted_string + chr(76) + "%"
    elif raw_letter == chr(112):
        encrypted_string = encrypted_string + chr(75) + "%"
    elif raw_letter == chr(113):
        encrypted_string = encrypted_string + chr(74) + "%"
    elif raw_letter == chr(114):
        encrypted_string = encrypted_string + chr(73) + "%"
    elif raw_letter == chr(115):
        encrypted_string = encrypted_string + chr(72) + "%"
    elif raw_letter == chr(116):
        encrypted_string = encrypted_string + chr(71) + "%"
    elif raw_letter == chr(117):
        encrypted_string = encrypted_string + chr(70) + "%"
    elif raw_letter == chr(118):
        encrypted_string = encrypted_string + chr(69) + "%"
    elif raw_letter == chr(119):
        encrypted_string = encrypted_string + chr(68) + "%"
    elif raw_letter == chr(120):
        encrypted_string = encrypted_string + chr(67) + "%"
    elif raw_letter == chr(121):
        encrypted_string = encrypted_string + chr(66) + "%"
    elif raw_letter == chr(122):
        encrypted_string = encrypted_string + chr(65) + "%"
    # for uppercase
    elif raw_letter == chr(65):
        encrypted_string = encrypted_string + chr(122) + "%"
    elif raw_letter == chr(66):
        encrypted_string = encrypted_string + chr(121) + "%"
    elif raw_letter == chr(67):
        encrypted_string = encrypted_string + chr(120) + "%"
    elif raw_letter == chr(68):
        encrypted_string = encrypted_string + chr(119) + "%"
    elif raw_letter == chr(69):
        encrypted_string = encrypted_string + chr(118) + "%"
    elif raw_letter == chr(70):
        encrypted_string = encrypted_string + chr(117) + "%"
    elif raw_letter == chr(71):
        encrypted_string = encrypted_string + chr(116) + "%"
    elif raw_letter == chr(72):
        encrypted_string = encrypted_string + chr(115) + "%"
    elif raw_letter == chr(73):
        encrypted_string = encrypted_string + chr(114) + "%"
    elif raw_letter == chr(74):
        encrypted_string = encrypted_string + chr(113) + "%"
    elif raw_letter == chr(75):
        encrypted_string = encrypted_string + chr(112) + "%"
    elif raw_letter == chr(76):
        encrypted_string = encrypted_string + chr(111) + "%"
    elif raw_letter == chr(77):
        encrypted_string = encrypted_string + chr(110) + "%"
    elif raw_letter == chr(78):
        encrypted_string = encrypted_string + chr(109) + "%"
    elif raw_letter == chr(79):
        encrypted_string = encrypted_string + chr(108) + "%"
    elif raw_letter == chr(80):
        encrypted_string = encrypted_string + chr(107) + "%"
    elif raw_letter == chr(81):
        encrypted_string = encrypted_string + chr(106) + "%"
    elif raw_letter == chr(82):
        encrypted_string = encrypted_string + chr(105) + "%"
    elif raw_letter == chr(83):
        encrypted_string = encrypted_string + chr(104) + "%"
    elif raw_letter == chr(84):
        encrypted_string = encrypted_string + chr(103) + "%"
    elif raw_letter == chr(85):
        encrypted_string = encrypted_string + chr(102) + "%"
    elif raw_letter == chr(86):
        encrypted_string = encrypted_string + chr(101) + "%"
    elif raw_letter == chr(87):
        encrypted_string = encrypted_string + chr(100) + "%"
    elif raw_letter == chr(88):
        encrypted_string = encrypted_string + chr(99) + "%"
    elif raw_letter == chr(89):
        encrypted_string = encrypted_string + chr(98) + "%"
    elif raw_letter == chr(90):
        encrypted_string = encrypted_string + chr(97) + "%"
    # for numbers
    elif raw_letter == chr(48):
        encrypted_string = encrypted_string + chr(255) + "%"
    elif raw_letter == chr(49):
        encrypted_string = encrypted_string + chr(245) + "%"
    elif raw_letter == chr(50):
        encrypted_string = encrypted_string + chr(227) + "%"
    elif raw_letter == chr(51):
        encrypted_string = encrypted_string + chr(211) + "%"
    elif raw_letter == chr(52):
        encrypted_string = encrypted_string + chr(199) + "%"
    elif raw_letter == chr(53):
        encrypted_string = encrypted_string + chr(186) + "%"
    elif raw_letter == chr(54):
        encrypted_string = encrypted_string + chr(172) + "%"
    elif raw_letter == chr(55):
        encrypted_string = encrypted_string + chr(165) + "%"
    elif raw_letter == chr(56):
        encrypted_string = encrypted_string + chr(154) + "%"
    elif raw_letter == chr(57):
        encrypted_string = encrypted_string + chr(143) + "%"
    # for remaining symbols intervals
    # 33-47
    elif raw_letter == chr(33):
        encrypted_string = encrypted_string + chr(48) + "%"
    elif raw_letter == chr(34):
        encrypted_string = encrypted_string + chr(57) + "%"
    elif raw_letter == chr(35):
        encrypted_string = encrypted_string + chr(49) + "%"
    elif raw_letter == chr(36):
        encrypted_string = encrypted_string + chr(142) + "%"
    elif raw_letter == chr(37):
        encrypted_string = encrypted_string + chr(50) + "%"
    elif raw_letter == chr(38):
        encrypted_string = encrypted_string + chr(159) + "%"
    elif raw_letter == chr(39):
        encrypted_string = encrypted_string + chr(224) + "%"
    elif raw_letter == chr(40):
        encrypted_string = encrypted_string + chr(51) + "%"
    elif raw_letter == chr(41):
        encrypted_string = encrypted_string + chr(206) + "%"
    elif raw_letter == chr(42):
        encrypted_string = encrypted_string + chr(52) + "%"
    elif raw_letter == chr(43):
        encrypted_string = encrypted_string + chr(237) + "%"
    elif raw_letter == chr(44):
        encrypted_string = encrypted_string + chr(53) + "%"
    elif raw_letter == chr(45):
        encrypted_string = encrypted_string + chr(54) + "%"
    elif raw_letter == chr(46):
        encrypted_string = encrypted_string + chr(55) + "%"
    elif raw_letter == chr(47):
        encrypted_string = encrypted_string + chr(56) + "%"
    # 58-64
    elif raw_letter == chr(58):
        encrypted_string = encrypted_string + chr(222) + "%"
    elif raw_letter == chr(59):
        encrypted_string = encrypted_string + chr(47) + "%"
    elif raw_letter == chr(60):
        encrypted_string = encrypted_string + chr(43) + "%"
    elif raw_letter == chr(61):
        encrypted_string = encrypted_string + chr(45) + "%"
    elif raw_letter == chr(62):
        encrypted_string = encrypted_string + chr(40) + "%"
    elif raw_letter == chr(63):
        encrypted_string = encrypted_string + chr(33) + "%"
    elif raw_letter == chr(64):
        encrypted_string = encrypted_string + chr(41) + "%"

    # 91-96
    elif raw_letter == chr(91):
        encrypted_string = encrypted_string + chr(62) + "%"
    elif raw_letter == chr(92):
        encrypted_string = encrypted_string + chr(59) + "%"
    elif raw_letter == chr(93):
        encrypted_string = encrypted_string + chr(63) + "%"
    elif raw_letter == chr(94):
        encrypted_string = encrypted_string + chr(58) + "%"
    elif raw_letter == chr(95):
        encrypted_string = encrypted_string + chr(64) + "%"
    elif raw_letter == chr(96):
        encrypted_string = encrypted_string + chr(62) + "%"

    # 123-126
    elif raw_letter == chr(123):
        encrypted_string = encrypted_string + chr(94) + "%"
    elif raw_letter == chr(124):
        encrypted_string = encrypted_string + chr(92) + "%"
    elif raw_letter == chr(125):
        encrypted_string = encrypted_string + chr(95) + "%"
    elif raw_letter == chr(126):
        encrypted_string = encrypted_string + chr(91) + "%"

    # end of logic 3
    return

def logic_four(raw_letter):
    # yha fourth logic lgake aur un do letters ko append kr dege in encrypted_string
    global encrypted_string
    # for lowercase
    if raw_letter == chr(97):
        encrypted_string = encrypted_string + chr(48) + "&"
    elif raw_letter == chr(98):
        encrypted_string = encrypted_string + chr(33) + "&"
    elif raw_letter == chr(99):
        encrypted_string = encrypted_string + chr(58) + "&"
    elif raw_letter == chr(100):
        encrypted_string = encrypted_string + chr(62) + "&"
    elif raw_letter == chr(101):
        encrypted_string = encrypted_string + chr(49) + "&"
    elif raw_letter == chr(102):
        encrypted_string = encrypted_string + chr(34) + "&"
    elif raw_letter == chr(103):
        encrypted_string = encrypted_string + chr(61) + "&"
    elif raw_letter == chr(104):
        encrypted_string = encrypted_string + chr(43) + "&"
    elif raw_letter == chr(105):
        encrypted_string = encrypted_string + chr(50) + "&"
    elif raw_letter == chr(106):
        encrypted_string = encrypted_string + chr(63) + "&"
    elif raw_letter == chr(107):
        encrypted_string = encrypted_string + chr(51) + "&"
    elif raw_letter == chr(108):
        encrypted_string = encrypted_string + chr(128) + "&"
    elif raw_letter == chr(109):
        encrypted_string = encrypted_string + chr(52) + "&"
    elif raw_letter == chr(110):
        encrypted_string = encrypted_string + chr(53) + "&"
    elif raw_letter == chr(111):
        encrypted_string = encrypted_string + chr(54) + "&"
    elif raw_letter == chr(112):
        encrypted_string = encrypted_string + chr(59) + "&"
    elif raw_letter == chr(113):
        encrypted_string = encrypted_string + chr(64) + "&"
    elif raw_letter == chr(114):
        encrypted_string = encrypted_string + chr(41) + "&"
    elif raw_letter == chr(115):
        encrypted_string = encrypted_string + chr(60) + "&"
    elif raw_letter == chr(116):
        encrypted_string = encrypted_string + chr(55) + "&"
    elif raw_letter == chr(117):
        encrypted_string = encrypted_string + chr(47) + "&"
    elif raw_letter == chr(118):
        encrypted_string = encrypted_string + chr(56) + "&"
    elif raw_letter == chr(119):
        encrypted_string = encrypted_string + chr(40) + "&"
    elif raw_letter == chr(120):
        encrypted_string = encrypted_string + chr(42) + "&"
    elif raw_letter == chr(121):
        encrypted_string = encrypted_string + chr(57) + "&"
    elif raw_letter == chr(122):
        encrypted_string = encrypted_string + chr(44) + "&"
    # for uppercase
    elif raw_letter == chr(65):
        encrypted_string = encrypted_string + chr(101) + "&"
    elif raw_letter == chr(66):
        encrypted_string = encrypted_string + chr(107) + "&"
    elif raw_letter == chr(67):
        encrypted_string = encrypted_string + chr(91) + "&"
    elif raw_letter == chr(68):
        encrypted_string = encrypted_string + chr(97) + "&"
    elif raw_letter == chr(69):
        encrypted_string = encrypted_string + chr(92) + "&"
    elif raw_letter == chr(70):
        encrypted_string = encrypted_string + chr(93) + "&"
    elif raw_letter == chr(71):
        encrypted_string = encrypted_string + chr(108) + "&"
    elif raw_letter == chr(72):
        encrypted_string = encrypted_string + chr(94) + "&"
    elif raw_letter == chr(73):
        encrypted_string = encrypted_string + chr(95) + "&"
    elif raw_letter == chr(74):
        encrypted_string = encrypted_string + chr(96) + "&"
    elif raw_letter == chr(75):
        encrypted_string = encrypted_string + chr(110) + "&"
    elif raw_letter == chr(76):
        encrypted_string = encrypted_string + chr(98) + "&"
    elif raw_letter == chr(77):
        encrypted_string = encrypted_string + chr(123) + "&"
    elif raw_letter == chr(78):
        encrypted_string = encrypted_string + chr(102) + "&"
    elif raw_letter == chr(79):
        encrypted_string = encrypted_string + chr(124) + "&"
    elif raw_letter == chr(80):
        encrypted_string = encrypted_string + chr(99) + "&"
    elif raw_letter == chr(81):
        encrypted_string = encrypted_string + chr(105) + "&"
    elif raw_letter == chr(82):
        encrypted_string = encrypted_string + chr(127) + "&"
    elif raw_letter == chr(83):
        encrypted_string = encrypted_string + chr(109) + "&"
    elif raw_letter == chr(84):
        encrypted_string = encrypted_string + chr(104) + "&"
    elif raw_letter == chr(85):
        encrypted_string = encrypted_string + chr(111) + "&"
    elif raw_letter == chr(86):
        encrypted_string = encrypted_string + chr(106) + "&"
    elif raw_letter == chr(87):
        encrypted_string = encrypted_string + chr(100) + "&"
    elif raw_letter == chr(88):
        encrypted_string = encrypted_string + chr(125) + "&"
    elif raw_letter == chr(89):
        encrypted_string = encrypted_string + chr(103) + "&"
    elif raw_letter == chr(90):
        encrypted_string = encrypted_string + chr(126) + "&"
    # for numbers
    elif raw_letter == chr(48):
        encrypted_string = encrypted_string + chr(113) + "&"
    elif raw_letter == chr(49):
        encrypted_string = encrypted_string + chr(65) + "&"
    elif raw_letter == chr(50):
        encrypted_string = encrypted_string + chr(68) + "&"
    elif raw_letter == chr(51):
        encrypted_string = encrypted_string + chr(112) + "&"
    elif raw_letter == chr(52):
        encrypted_string = encrypted_string + chr(114) + "&"
    elif raw_letter == chr(53):
        encrypted_string = encrypted_string + chr(69) + "&"
    elif raw_letter == chr(54):
        encrypted_string = encrypted_string + chr(116) + "&"
    elif raw_letter == chr(55):
        encrypted_string = encrypted_string + chr(66) + "&"
    elif raw_letter == chr(56):
        encrypted_string = encrypted_string + chr(67) + "&"
    elif raw_letter == chr(57):
        encrypted_string = encrypted_string + chr(115) + "&"
    # for remaining symbols intervals
    # 33-47
    elif raw_letter == chr(33):
        encrypted_string = encrypted_string + chr(79) + "&"
    elif raw_letter == chr(34):
        encrypted_string = encrypted_string + chr(71) + "&"
    elif raw_letter == chr(35):
        encrypted_string = encrypted_string + chr(117) + "&"
    elif raw_letter == chr(36):
        encrypted_string = encrypted_string + chr(75) + "&"
    elif raw_letter == chr(37):
        encrypted_string = encrypted_string + chr(76) + "&"
    elif raw_letter == chr(38):
        encrypted_string = encrypted_string + chr(118) + "&"
    elif raw_letter == chr(39):
        encrypted_string = encrypted_string + chr(72) + "&"
    elif raw_letter == chr(40):
        encrypted_string = encrypted_string + chr(77) + "&"
    elif raw_letter == chr(41):
        encrypted_string = encrypted_string + chr(119) + "&"
    elif raw_letter == chr(42):
        encrypted_string = encrypted_string + chr(78) + "&"
    elif raw_letter == chr(43):
        encrypted_string = encrypted_string + chr(73) + "&"
    elif raw_letter == chr(44):
        encrypted_string = encrypted_string + chr(120) + "&"
    elif raw_letter == chr(45):
        encrypted_string = encrypted_string + chr(74) + "&"
    elif raw_letter == chr(46):
        encrypted_string = encrypted_string + chr(70) + "&"
    elif raw_letter == chr(47):
        encrypted_string = encrypted_string + chr(121) + "&"
    # 58-64
    elif raw_letter == chr(58):
        encrypted_string = encrypted_string + chr(83) + "&"
    elif raw_letter == chr(59):
        encrypted_string = encrypted_string + chr(80) + "&"
    elif raw_letter == chr(60):
        encrypted_string = encrypted_string + chr(85) + "&"
    elif raw_letter == chr(61):
        encrypted_string = encrypted_string + chr(81) + "&"
    elif raw_letter == chr(62):
        encrypted_string = encrypted_string + chr(84) + "&"
    elif raw_letter == chr(63):
        encrypted_string = encrypted_string + chr(82) + "&"
    elif raw_letter == chr(64):
        encrypted_string = encrypted_string + chr(122) + "&"

    # 91-96
    elif raw_letter == chr(91):
        encrypted_string = encrypted_string + chr(89) + "&"
    elif raw_letter == chr(92):
        encrypted_string = encrypted_string + chr(87) + "&"
    elif raw_letter == chr(93):
        encrypted_string = encrypted_string + chr(165) + "&"
    elif raw_letter == chr(94):
        encrypted_string = encrypted_string + chr(88) + "&"
    elif raw_letter == chr(95):
        encrypted_string = encrypted_string + chr(90) + "&"
    elif raw_letter == chr(96):
        encrypted_string = encrypted_string + chr(86) + "&"

    # 123-126
    elif raw_letter == chr(123):
        encrypted_string = encrypted_string + chr(236) + "&"
    elif raw_letter == chr(124):
        encrypted_string = encrypted_string + chr(239) + "&"
    elif raw_letter == chr(125):
        encrypted_string = encrypted_string + chr(244) + "&"
    elif raw_letter == chr(126):
        encrypted_string = encrypted_string + chr(247) + "&"

    # end of logic 4
    return

def calc_logic(raw_letter):
    # random logic no uss logic ko lga ke do letters bn gye ek ke ab in do letters ko append krna in encrypted_string string, aur han hm  bs isi b mein append krte jayenge to make a encrypted paragraph.

    logic=random.randint(1,4)
    if logic==1:
        logic_one(raw_letter)
    elif logic==2:
        logic_two(raw_letter)
    elif logic==3:
        logic_three(raw_letter)
    else:
        logic_four(raw_letter)

    return

def into_letters(raw_line):
    global encrypted_string
    for raw_letter in raw_line:
        # space between words daalni pdgi yha
        if raw_letter==" ":
            encrypted_string=encrypted_string+chr(10000)
        else:
            calc_logic(raw_letter)
    # add krna h string mein unicode for line change ,, for ke bahar
    encrypted_string = encrypted_string + chr(10001)
    return

def takeline():
    for line_no in range(1,101,1):
        raw=""
        raw=input()
        # yha ek condition add hgi to check if quit is entered, aur agar han toh ,
        #sidha encrypted_string i.e encrypted data ko print kr dege
        if(raw.lower()=="quit"):
            print("Your encrypted data is :--")
            for t in encrypted_string:
                print(t,end="")
                sleep(random.uniform(0,0.3))
            print()
            print()
            return
        else:
            into_letters(raw)


# calling takeline
effect="ACCESS GRANTED..."
password=input("Enter password to access : ")
if(password=="aadharjain2002e"):
    # for just typewriter effect
    for w in effect:
        print(w,end="")
        sys.stdout.flush()
        sleep(0.1)
    print()
    print()
    print("Enter data to Encrypt")
    takeline()
else:
    print("ACCESS DENIED!")