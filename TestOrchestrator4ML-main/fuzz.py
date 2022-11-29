# Title:       Project for Software Quality Assurance (COMP 5710/6710)
# Description: Automatically fuzzes five methods from TestOrchestrator4ML
# Authors:     Mary Mitchell (mem0250) and Adia Foster (azf0046)
# Course:      COMP5710 - Software Quality Assurance
# Due Date:    1 December 2022
# Run:         fuzz.py will be automatically executed from GitHub actions

from detection.py_parser import checkMetricNames 
from generation.py_parser import checkAlgoNames
from generation.main import generateAttack
from label_perturbation_attack.cliffsDelta import runs
from label_perturbation_attack.knn import euc_dist

def fuzzCheckMetricNames():
    fuzzValues = [0, None, 'RANDOMSTRING', {'RANDOM': 'DICTIONARY'}, 3.14159, {None}, [None], b'0000', {}, []]
    print("Start fuzzing checkMetricNames...")
    for input in fuzzValues:
        try: 
            checkMetricNames(input)
        except Exception as exct:
            print("checkMetricNames failed with input: " + input)
    print("Finish fuzzing checkMetricNames...")

def fuzzCheckAlgoNames():
    print("Start fuzzing checkAlgoNames...")
    print("Finish fuzzing checkAlgoNames...")

def fuzzGenerateAttack():
    print("Start fuzzing generateAttack...")
    print("Finish fuzzing generateAttack...")

def fuzzRuns():
    print("Start fuzzing runs...")
    print("Finish fuzzing runs...")

def fuzzEuc_Dist():
    print("Start fuzzing euc_dist...")
    print("Finish fuzzing euc_dist...")

def main():
    print("*** Begin Fuzzer ***")
    print("*** End Fuzzer ***")

if __name__ == "__main__":
    main()