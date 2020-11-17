
## GymLogger

Project for parsing log from gym, and displaying nice charts showing your progress
in various exercises, and life best results.

### Context

Over many years, I collected a huge journal/log of exercises. I would like to be able
to analyse it, watch charts and draw conclusions. Unfortunately it's written in quite
chaotic way, with many different syntaxes and lots of exceptions and errors. 

Here's the idea for this project:
1. Create Parser script that will ingest this log and extract information into yaml file with
well defined schema. Then it will be much easier to perform any kind of operations on it.

2. Create Charter program that will show graphs of weight and exercise progress. Killer feature
would be to run ML algorithms that find the combination of exercises, weights, repetitions
and trainings frequency, that gave best results.

3. Create GymLogger mobile app or webpage that will make filling in new trainings quick & easy.
It should show exercises using images, and big buttons/sliders for easy setting of
weights and repetitions.


### TODO

Parser:
- convert all letters to lowercase and transliterate polish chars
- checkout https://textx.github.io/Arpeggio/ and https://github.com/textX/textX
- design parser language
- perform one-off-conversion

Charter:
- choose one of gui frameworks 
- setup gui
- choose one of charts libraries
- load trainings file and show charts
- display top-10 best results for particular exercise
- trace best results to training
- ML part


### DONE
+ load exercise definitions
+ parse yaml with trainings
+ find max weight ever for exercise in all trainings
+ unit tests