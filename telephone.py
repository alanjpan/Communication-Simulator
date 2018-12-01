# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:28:35 2018

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

Program used to simulate and describe communication.

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Communication Simulator [Computer software]. Github repository <https://github.com/alanjpan/Communication-Simulator>

Note this software's license is GNU GPLv3.
"""

import random

line = []

def probability(success, failure):
    outcomes = success + failure
    likelihood = success / outcomes
    return likelihood

def createline(nodes):
    global line
    line.clear()
    for i in range(nodes):
        #communication success probability threshold
        line.append(random.randrange(90, 100, 1))
        
def message(msg, n):
    global line
    createline(n)
    string = []
    #dissassemble string
    for char in msg:
        string.append(char)
    #pass string through line of nodes
    for i in range(len(string)):
        for j in line:
            #message vector
            if random.randrange(0, 100, 1) > j:
                string[i] = '@'
                break
    #reassemble string
    output = ''
    success = 0
    failure = 0
    for i in string:
        output += i
        if i == '@':
            failure += 1
        else:
            success += 1
    integrity = probability(success, failure)
    print('transmission integrity: ' + str(integrity))
    print('noise: ' + str(1 - integrity))
    print('char count: ' + str(len(msg)))
    print('received message: ' + output)
