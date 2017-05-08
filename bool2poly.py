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
    if(len(bool_eqn) == 8):
        if(bool_eqn[3] == '*' and bool_eqn[5] == '*'):
            if '!' in bool_eqn[2]:
                bool_eqn[2] = re.sub('[^a-zA-Z0-9_\s]','',bool_eqn[2])
                bool_eqn[2] = "("+str(bool_eqn[2])+" + 1)"
            if '!' in bool_eqn[4]:
                bool_eqn[4] = re.sub('[^a-zA-Z0-9_\s]','',bool_eqn[4])
                bool_eqn[4] = "("+str(bool_eqn[4])+" + 1)"
            if '!' in bool_eqn[6]:
                bool_eqn[6] = re.sub('[^a-zA-Z0-9_\s]','',bool_eqn[6])
                bool_eqn[6] = "("+str(bool_eqn[6])+" + 1)"
            poly.append(str(bool_eqn[0]) + " + " + str(bool_eqn[2]) + " * "  + str(bool_eqn[4]) + " * " + str(bool_eqn[6]) + ";")

        if(bool_eqn[3] == '+' and bool_eqn[5] == '+'):
            if '!' in bool_eqn[2]:
                bool_eqn[2] = re.sub('[^a-zA-Z0-9_\s]','',bool_eqn[2])
                bool_eqn[2] = "("+str(bool_eqn[2])+" + 1)"
            if '!' in bool_eqn[4]:
                bool_eqn[4] = re.sub('[^a-zA-Z0-9_\s]','',bool_eqn[4])
                bool_eqn[4] = "("+str(bool_eqn[4])+" + 1)"
            if '!' in bool_eqn[6]:
                bool_eqn[6] = re.sub('[^a-zA-Z0-9_\s]','',bool_eqn[6])
                bool_eqn[6] = "("+str(bool_eqn[6])+" + 1)"
            poly.append(str(bool_eqn[0]) + " + " + str(bool_eqn[2]) + " + " + str(bool_eqn[4]) + " + " + str(bool_eqn[6]) + " + " + str(bool_eqn[2]) + " * " + str(bool_eqn[4]) + " + " + str(bool_eqn[4]) + " * " + str(bool_eqn[6]) + " + " + str(bool_eqn[2]) + " * " + str(bool_eqn[6]) + " + " + str(bool_eqn[2]) + " * " + str(bool_eqn[4]) + " * " + str(bool_eqn[6]) + ";")

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


##*****************************************************************
##             Main Part of the code begins here
##*****************************************************************

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
    #print clean_line
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

    line = clean_line.split(' ')
    #print line

    #print len(line)

    if(len(line) <= 6 and len(line) >=2):
        bool_list.append(line)
        continue
    if(len(line) == 8 and (line[3] == line[5])):
        bool_list.append(line)
        continue

    #************* AND Gate Reduction - STARTS HERE ************#
    word_index = 0
    for word in line: #Loop 1 starts here
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

        ## Checking for 2 or 3 Input gates before further processing
        temp4_line = ' '.join(line)
        temp4_line = re.sub(' +',' ',temp4_line) #To remove more than whitespace
        temp4_line = temp4_line.split(' ')
        if(len(temp4_line) == 4):
            print "ERROR: Expression with one Element found" # Element with single variable should have got filtered earlier itself
        if((len(temp4_line) == 6) and (temp4_line[3] == '*')):
            bool_list.append(temp4_line)
            break
        if((len(temp4_line) == 8) and (temp4_line[3] == '*') and (temp4_line[3] == temp4_line[5])):
            bool_list.append(temp4_line)
            break

        temp_list = []

        if word_index < len(line)-5:
            if (line[word_index + 1] == '*') and (line[word_index + 3] == '*'):
                temp_list.insert(0, 't_net_'+str(net_cnt))
                temp_list.insert(1, '=')
                temp_list.insert(2, word)
                temp_list.insert(3, '*')
                temp_list.insert(4, line[word_index+2])
                temp_list.insert(5, '*')
                temp_list.insert(6, line[word_index+4])
                temp_list.insert(7, ';')
                bool_list.append(temp_list)

                line[word_index] = ' '
                line[word_index+1] = ' '
                line[word_index+2] = ' '
                line[word_index+3] = ' '
                line[word_index+4] = 't_net_'+str(net_cnt)
                net_list.append('t_net_'+str(net_cnt))
                net_cnt = net_cnt + 1
                word_index = word_index + 1
                continue

        if word_index >= len(line)-3:
            word_index = word_index + 1
            continue

        temp_list = []
        if line[word_index + 1] == '*':
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
    ##Loop 1 Ends here

    line = ' '.join(line)
    line = re.sub(' +',' ',line) #To remove more than whitespace
    line = line.split(' ');

    if(len(line) == 4):
        bool_list.append(line)
        continue  #If an expression had only and gates initially, then this 'line' will end up having single variable.

    #************* AND Gate Reduction - ENDS HERE ************#
    #print "For OR Gate processing"
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

        ## Checking for 2 or 3 Input gates before further processing
        temp4_line = ' '.join(line)
        temp4_line = re.sub(' +',' ',temp4_line) #To remove more than whitespace
        temp4_line = temp4_line.split(' ')
        if(len(temp4_line) == 4):
            print "ERROR: Expression with one Element found" # Element with single variable should have got filtered earlier itself
        if((len(temp4_line) == 6) and (temp4_line[3] == '+')):
            bool_list.append(temp4_line)
            break
        if((len(temp4_line) == 8) and (temp4_line[3] == '+') and (temp4_line[3] == temp4_line[5])):
            bool_list.append(temp4_line)
            break

        temp_list = []
        if word_index < len(line)-5:
            if (line[word_index + 1] == '+') and (line[word_index + 3] == '+'):
                temp_list.insert(0, 't_net_'+str(net_cnt))
                temp_list.insert(1, '=')
                temp_list.insert(2, word)
                temp_list.insert(3, '+')
                temp_list.insert(4, line[word_index+2])
                temp_list.insert(5, '+')
                temp_list.insert(6, line[word_index+4])
                temp_list.insert(7, ';')
                bool_list.append(temp_list)

                line[word_index] = ' '
                line[word_index+1] = ' '
                line[word_index+2] = ' '
                line[word_index+3] = ' '
                line[word_index+4] = 't_net_'+str(net_cnt)
                net_list.append('t_net_'+str(net_cnt))
                net_cnt = net_cnt + 1
                word_index = word_index + 1
                continue

        if word_index >= len(line)-3:
            word_index = word_index + 1
            continue

        temp_list = []
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
