# Title:       Project for Software Quality Assurance (COMP 5710/6710)
# Description: Automatically fuzzes five methods from TestOrchestrator4ML
# Authors:     Mary Mitchell (mem0250) and Adia Foster (azf0046)
# Course:      COMP5710 - Software Quality Assurance
# Due Date:    1 December 2022
# Run:         fuzz.py will be automatically executed from GitHub actions

import detection.constants as constants
from detection.py_parser import checkMetricNames 
from generation.py_parser import checkAlgoNames
from generation.main import generateAttack
#from label_perturbation_attack.cliffsDelta import runs
from label_perturbation_attack.knn import euc_dist

def fuzzCheckMetricNames():
    fuzzValues = [0, None, 'RANDOMSTRING', {'RANDOM': 'DICTIONARY'}, 3.14159, {None}, [None], b'0000', int(b'0000'), {}, [], "\"`'><script>\\xE2\\x80\\xA8javascript:alert(1)</script>'", '', [[]]]
    print("Start fuzzing checkMetricNames...")
    for input in fuzzValues:
        try: 
            checkMetricNames(input)
            print("checkMetricNames passed with input" + str(input))
        except:
            print("checkMetricNames failed with input: " + str(input))  
    print("Finish fuzzing checkMetricNames...")

def fuzzCheckAlgoNames():
    fuzzValues = [0, None, 'RANDOMSTRING', {'RANDOM': 'DICTIONARY'}, 3.14159, {None}, [None], b'0000', int(b'0000'), {}, [], "\"`'><script>\\xE2\\x80\\xA8javascript:alert(1)</script>'", '', [[]]]
    print("Start fuzzing checkAlgoNames...")
    for input in fuzzValues:
        try: 
            checkAlgoNames(input)
            print("checkAlgoNames passed with input" + str(input))
        except:
            print("checkAlgoNames failed with input: " + str(input)) 
    print("Finish fuzzing checkAlgoNames...")

def fuzzGenerateAttack():

    print("Start fuzzing generateAttack...")
    print("Finish fuzzing generateAttack...")

def fuzzRuns():
    print("Start fuzzing runs...")
    print("Finish fuzzing runs...")

def fuzzEuc_Dist():
    fuzzValue1 = [0, 1, 2, None]
    fuzzValue2 = [0, 2, 1, None]
    print("Start fuzzing euc_dist...")
    for val1 in fuzzValue1:
        for val2 in fuzzValue2:
            try:
                euc_dist(val1, val2)
            except:
                print("euc_dist failed with parameters: " + str(val1) + " and " + str(val2))
    print("Finish fuzzing euc_dist...")

def main():
    print("*** Begin Fuzzer ***")
    fuzzCheckMetricNames()
    fuzzCheckAlgoNames()
    fuzzEuc_Dist()
    print("*** End Fuzzer ***")

if __name__ == "__main__":
    main()