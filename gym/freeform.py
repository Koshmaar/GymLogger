
"""

-------- Syntax cases mixed inside, that have to be taken into account by one grammar:

*2010-08-07 Klata*
  wyciskania płaska 50/12  60/8  65/6  70/2      // A
  sztangielki skosna  12x15  10x20  6x22.5       // B
  przenoszenie sztangielki 20 22.5 25            // C
  podrzut  20/10 x3                              // D
  łydki                                          // E

A - 50/12 means: 12 repetitions with 50kg
B - 10x20 means: 10 repetitions with 20 kg
C - 20 means: 20kg had typical (sic) number of repetitions in this exercise
D - foo x3 means: the exercise foo was performed 3 times
E - no info means exercise was done with typical (sic) weights and repetitions
    there needs to be additional config file which stores those


2010-08-25
nogi
 przysiady 12x50 10x70 8x80 7x90 2x95
 wyprosty siedzac 12x20 12x30 8x40 6x50
 zginanie lezac 12x20 10x30 7x40 7x40
 wyprosty na maszynie 5x90 5x115 5x135 5x155


-------- Syntax samples that has to be manually fixed in file (before parsing):

1 nozne 7, 7.5 /7, 10/
Jefferson 40/10, 65/

"""

# grammar in BNF kinda:

training_header="<*>DATE<*>  COMMENT <*>"
after_training_header="COMMENT"

exercise="<NAME>\s(<REPETITIONS> <SEPARATOR> )* "   # todo: for last repetition, separator is not needed
name="<string>"

repetitions="(WEIGHT/TIMES | TIMES | +WEIGHT) <MULTIPLIER>"

weight="FLOAT"
times="INT|INT\s+\s<after_short_break>"
after_short_break="INT"

separator = (",|space")

multiplier = "x\s<NUMBER>"

additional_weight = "+<NUMBER>(kg)"
