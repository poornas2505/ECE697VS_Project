#!/usr/bin/env python

##*******************************************************************
#
#
#
#
#
#
##*******************************************************************

import sys
import re

def poly_gen(bool_eqn):
    poly = []
    if(len(bool_eqn) == 6):
        temp_bool_eqn = ' '.join(bool_eqn)
        temp_bool_eqn = re.sub('[^a-zA-Z0-9_=\[\]+*\s;]','! ',temp_bool_eqn)
        bool_eqn = temp_bool_eqn.split(' ')

        if(bool_eqn[2] != '!'):
            if(bool_eqn[4] != '!'): # y = a * b #or# y = a + b
                if(bool_eqn[3] == '+'):
                    poly.append(str(bool_eqn[0]) + " + " + str(bool_eqn[2]) + " + " + str(bool_eqn[4]) + " + " + str(bool_eqn[2]) + " * " + str(bool_eqn[4]) + ";")
                elif(bool_eqn[3] == '*'):
                    poly.append(str(bool_eqn[0]) + " + " + str(bool_eqn[2]) + " * " + str(bool_eqn[4]) + ";")
            else: # y = a * !b #or# y = a + !b
                if(bool_eqn[3] == '+'):
                    poly.append(str(bool_eqn[0]) + " + " + "1" + " + " + str(bool_eqn[5]) + " + " + str(bool_eqn[2]) + " * " + str(bool_eqn[5]) + ";")
                elif(bool_eqn[3] == '*'):
                    poly.append(str(bool_eqn[0]) + " + " + str(bool_eqn[2]) + " * " + str(bool_eqn[5]) + " + " + str(bool_eqn[2]) + ";")
        else:
            if(bool_eqn[5] != '!'): # y = !a + b #or# y = !a * b
                if(bool_eqn[4] == '+'):
                    poly.append(str(bool_eqn[0]) + " + " + "1" + " + " + str(bool_eqn[3]) + " + " + str(bool_eqn[3]) + " * " + str(bool_eqn[5]) + ";")
                elif(bool_eqn[4] == '*'):
                    poly.append(str(bool_eqn[0]) + " + " + str(bool_eqn[3]) + " * " + str(bool_eqn[5]) + " + " + str(bool_eqn[5]) + ";")
            else: # y = !a + !b #or# y = !a * !b
                if(bool_eqn[4] == '+'):
                    poly.append(str(bool_eqn[0]) + " + " + "1" +  " + " + str(bool_eqn[3]) + " * " + str(bool_eqn[6]) + ";")
                elif(bool_eqn[4] == '*'):
                    poly.append(str(bool_eqn[0]) + " + " + "1" + " + " + str(bool_eqn[3]) + " + " + str(bool_eqn[6]) + " + " + str(bool_eqn[3]) + " * " + str(bool_eqn[6]) + ";")

    if(len(bool_eqn) == 4):
        temp_bool_eqn = ' '.join(bool_eqn)
        temp_bool_eqn = re.sub('[^a-zA-Z0-9_=\[\]+*\s;]','! ',temp_bool_eqn)
        bool_eqn = temp_bool_eqn.split(' ')

        if(len(bool_eqn) == 4):
            poly.append(str(bool_eqn[0]) + " + " + str(bool_eqn[2]) + ";")
        else:
            poly.append(str(bool_eqn[0]) + " + " + str(bool_eqn[3]) + " + 1;")
    return ' '.join(poly)

#f1 = open(sys.argv[1], 'r')
#raw_lines = f1.read().split('\n')
#print raw_lines

bool_list = []
temp_list = []
net_list = []
net_cnt = 0
poly_list = []

with open(sys.argv[1],'r') as fh:
    raw_lines = fh.read().split('\n')

for raw_line in raw_lines:
    if "INORDER" in raw_line:
        continue
    if "OUTORDER" in raw_line:
        continue

    ## Remove special characters (Currently code supports '[' or ']') from starting/ ending character of a net - Singular doesn't support otherwise
    temp_line = re.sub('[^a-zA-Z0-9_=!\[\]+\s;]',' * ',raw_line)
    temp2_line = re.sub('[^a-zA-Z0-9_=!\[\]*\s;]',' + ',temp_line)
    temp3_line = re.sub('[^a-zA-Z0-9_=!\[\]*+\s]',' ;',temp2_line)
    clean_line = re.sub(' +',' ',temp3_line) #To remove more than one whitespace
    clean_line = clean_line.split(' ')
    net_index = 0
    for net in clean_line:
        if('[' in net):
            if('!' in net):
                net = re.sub('[^a-zA-Z0-9_=!*+\]\s;]','!tmp_',net)
                print "![] case found"
            else:
                net = re.sub('[^a-zA-Z0-9_=!*+\]\s;]','tmp_',net)
            net = re.sub('[^a-zA-Z0-9_=!*+\s;]','',net)
            clean_line[net_index] = net
        net_index = net_index + 1
    print clean_line
    raw_line = ' '.join(clean_line)

    ## Extracting nets to create vanishing polynomials ##
    temp_nets = re.split(r"[^A-Za-z0-9_\[\]]",raw_line)
    temp_nets = ' '.join(temp_nets)
    temp_nets = re.sub(' +',' ',temp_nets) #To remove more than whitespace
    temp_nets = temp_nets.split(' ')
    for net in temp_nets:
        if(net == ''):
            continue
        net_list.append(net)
    #print raw_line
    #print clean_line
    temp_line = re.sub('[^a-zA-Z0-9_=!\[\]+\s;]',' * ',raw_line)
    temp2_line = re.sub('[^a-zA-Z0-9_=!\[\]*\s;]',' + ',temp_line)
    temp3_line = re.sub('[^a-zA-Z0-9_=!\[\]*+\s]',' ;',temp2_line)
    clean_line = re.sub(' +',' ',temp3_line) #To remove more than whitespace

    #print raw_line
    #print temp_line
    #print clean_line

    line = clean_line.split(' ')
    #print raw_line
    #print clean_line
    print line

    print len(line)

    if(len(line) <= 6 and len(line) >=2):
        bool_list.append(line)
        continue

    #************* AND Gate Reduction - STARTS HERE ************#
    word_index = 0
    for word in line:
        #print "Word index is: ",(word_index)
        temp_list = []
        #word_index = line.index(word) #Using this causes problem when there are multiple occurances of same element
        if word_index == 0:
            word_index = word_index + 1
            continue
        if word == '=':
            word_index = word_index + 1
            continue
        if word == '+':
            word_index = word_index + 1
            continue
        if word == '*':
            word_index = word_index + 1
            continue
        if word == ';':
            word_index = word_index + 1
            continue
        if word_index >= len(line)-3:
            word_index = word_index + 1
            continue

        if line[word_index + 1] == '*':
            #temp_list[0] = 't_net_'+str(net_cnt)
            #temp_list[1] = '='
            #temp_list[2] = word
            #temp_list[3] = '*'
            #temp_list[4] = line[word_index+2]

            temp_list.insert(0, 't_net_'+str(net_cnt))
            temp_list.insert(1, '=')
            temp_list.insert(2, word)
            temp_list.insert(3, '*')
            temp_list.insert(4, line[word_index+2])
            temp_list.insert(5, ';')
            bool_list.append(temp_list)

            line[word_index] = ' '
            line[word_index+1] = ' '
            line[word_index+2] = 't_net_'+str(net_cnt)
            #print temp_list
            #print line
            net_list.append('t_net_'+str(net_cnt))
            net_cnt = net_cnt + 1
        word_index = word_index + 1

    line = ' '.join(line)
    line = re.sub(' +',' ',line) #To remove more than whitespace
    line = line.split(' ');

    if(len(line) == 4):
        bool_list.append(line)
        continue  #If an expression had only and gates initially, then this 'line' will end up having single variable.

    #************* AND Gate Reduction - ENDS HERE ************#
    print "For OR Gate processing"
    #print line

    if(len(line) <= 6 and len(line) >=2):
        bool_list.append(line)
        continue

    #************* OR Gate Reduction - STARTS HERE ************#
    word_index = 0
    for word in line:
        temp_list = []
        if word_index == 0:
            word_index = word_index + 1
            continue
        if word == '=':
            word_index = word_index + 1
            continue
        if word == '+':
            word_index = word_index + 1
            continue
        if word == '*':
            print "Error: AND Gates still present after reduction"
            continue
        if word == ';':
            word_index = word_index + 1
            continue
        if word_index >= len(line)-3:
            word_index = word_index + 1
            continue

        if line[word_index + 1] == '+':
            temp_list.insert(0, 't_net_'+str(net_cnt))
            temp_list.insert(1, '=')
            temp_list.insert(2, word)
            temp_list.insert(3, '+')
            temp_list.insert(4, line[word_index+2])
            temp_list.insert(5, ';')
            bool_list.append(temp_list)

            line[word_index] = ' '
            line[word_index+1] = ' '
            line[word_index+2] = 't_net_'+str(net_cnt)
            #print temp_list
            #print line
            net_list.append('t_net_'+str(net_cnt))
            net_cnt = net_cnt + 1
        word_index = word_index + 1

    line = ' '.join(line)
    line = re.sub(' +',' ',line) #To remove more than whitespace
    line = line.split(' ');

    if(len(line) == 4):
        bool_list.append(line)
        continue  #If an expression had only OR gates initially, then this 'line' will end up having single variable.
#print bool_list

##*****************************************************************
##                      Post-Processing
##*****************************************************************

poly_num = 0

fw = open(str(sys.argv[1])+".ply", "w")

## Writing Ring declaration and for creating vanishing Polynomials ##
#print net_list
net_list = ' '.join(net_list)
net_list = re.sub(' +',' ',net_list) #To remove more than whitespace
net_list = net_list.split(' ')
net_list = list(set(net_list))
#print net_list

fw.write("ring r = (%d, a), (%s, S, T), lp;\n"%(2**int(sys.argv[2]), ', '.join(net_list)))
fw.write("ideal J0 = T^%d + T;\n"%(2**int(sys.argv[2])))

for eqn in bool_list:
    poly = []
    temp_poly = poly_gen(eqn)
    poly.append("poly f_" + str(poly_num) + " = " + str(temp_poly))
    fw.write("%s"%(' '.join(poly)))
    fw.write('\n')
    poly_list.append("f_" + str(poly_num) + ", ")
    poly_num = poly_num + 1

for net in net_list:
    poly = []
    if(net == ''):
        continue
    poly.append("poly f_van_" + str(poly_num) + " = " + str(net) + "^2" + " - " + str(net) + ";")
    fw.write("%s"%(' '.join(poly)))
    fw.write('\n')
    poly_list.append("f_van_" + str(poly_num) + ", ")
    poly_num = poly_num + 1

## Adding Current State (S) and Next State (T) word level variables to create vanishing polynomial and ideal
poly = []
poly.append("poly f_van_" + str(poly_num) + " = T^" + str(2**int(sys.argv[2])) + "- T" + ";")
fw.write("%s"%(' '.join(poly)))
fw.write('\n')
poly_list.append("f_van_" + str(poly_num) + ", ")
poly_num = poly_num + 1

poly = []
poly.append("poly f_van_" + str(poly_num) + " = S^" + str(2**int(sys.argv[2])) + "- S" + ";")
fw.write("%s"%(' '.join(poly)))
fw.write('\n')
poly_list.append("f_van_" + str(poly_num) + ";")
poly_num = poly_num + 1

## Writing Ideal of allpolynomials
fw.write("\nideal poly_func = %s"%(' '.join(poly_list)))

fw.close()
