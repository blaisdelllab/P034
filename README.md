# P034 - The Role of Post-Choice Feedback in Learning a MTO Task
This is the main code for Cyrus Kirkman and Dr. Li Fang's P034b project studying
the role of feedback upon response accuracy (and maybe learning acquisition)
in a delayed many-to-one task (DMTO). It is an alternative approach to the
previous three-button layout approoach (P034a), in the hopes of both improving
baseline accuracy but also better observing a learning curve from 50% (chance)
accuracy over time, dependent upon feedback. The choice layout included two
statically colored and placed buttons on L/R sides of the screen with a
dynamically changing center stimulus. L/R key accuracy was dependent upon the
image type and was fixed accross sessions. Trainings are as follows:
    
1) Mixed instrumental/autoshaping: one of the three stimuli were filled in
    at the beginning of each trial. After a peck on the filled stimulus (FR1),
    a reinforcer was immediately provided. If no response was made within 
    10 s, a reinforcer was immediately provided. Fill colors were either blue
    or yellow, save for six trials for the first two sessions that were grey.
    
2) Many-to-One: The next phase was a simple MTO task in which a color
    was presented in the sample slot. After several pecks (FR3 to start,
    then inreased to FR10), a blue and yellow option were presented in 
    each of the comparison locations below (randomly assigned per trial) 
    while the sample remained filled in. A peck on the correct comparison
    key (e.g., blue comparison in the context of a blue sample) was
    immediately reinforced, while an incorrect choice (e.g., yellow
    comparison in the context of the blue sample) was punished with a 10s
    timeout before the ITI and next trial. Subjects proceeded to the next
    phase after they demonstrated at least 85% accuracy on a completed 
    session

FINAL EXPERIMENTAL CODE

3) Delayed Many-to-One: Similar to the priorMTO phase, the DMTO started
    with presentation of the sample and completion of a FR10 schedule to 
    proceed. Next, the sample dissapeared and birds faced a delay period 
    of variable length: either 2, 3, 4, or 5 s. After the delay concluded,
    the two differently filled comparison choice options appeared. When a
    choice was made, subjects were presented with a post-choice interval
    in which the sample key (which had been empty) was manipulated in a 
    manner dependent upon the group subjects were assigned: birds in the
    control group faced a filled grey key for every post-choice interval. 
    Birds in the experimental group faced a re-presentation of the sample
    color from the start of the trial. After the 3s post-choice interval,
    a correct choice was reinforced with food while and incorrect choice 
    was punished with a 10s TO.
        
Once pigeons reached the DMTO phase, there were a series of nine distinct 
phases to measure different aspects of feedback in learning. Some phases were
replicated across multiple stimulus sets, which are provided in parantheses. 
Details on each of these phases will be provided in the manuscript.

i. (3,12) Informative Feedback vs. Immediate Outcome (IFvIO)

ii. (2,4) Informative feedback vs. non-informative feedback with
          identical control cues (IFvN-IF)

iii. (5,6,7,8,9) Informative feedback vs. paired non-informative
          feedback (IFvPNIF)

iv. (10) Informative feedback vs. varied non-informative feedback (IFvVNIF)

v. (11) Informative feedback vs. blank interval (IFvBI)

vi. (13) Informative feedback vs. paired categorical feedback (IFvPCF)

vii. (14) Informative feedback vs. unpaired categorical feedback (IFvUCF)

viii. (15) Paired categorical feedback vs. psuedopaired categorical
           feedback (PCFvUCF)

ix. (16, 17) Informative feedback vs. Encoded Outcome (IFvEO)

