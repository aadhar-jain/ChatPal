def logic_one(raw_letter):
    # apply logic first to raw_letter, append to encrypted_string
    # return it and since string is pass by value
    # in main.py , append returned string to original encrypted_string out there.
    encrypted_string = ""

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
    return encrypted_string