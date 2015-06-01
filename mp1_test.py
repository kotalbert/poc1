from mp1 import merge

test1 = [2,0,2,4]
test2 = [0,0,2,2]
test3= [2,2,0,0]

output1 = [4,4,0,0]
output2 = [4,0,0,0]

def comp(list1, list2):
    for val in list1:
        if val not in list2:
            return False
    return True

def test_merge(line_in,line_out):
    merge_output = merge(line_in)
    
    if comp(merge_output, line_out):
        print "OK"
        
    else:
        print "Failed"
        
    print "line_in: ", line_in
    print "merge_output", merge_output
    print "line_out: ", line_out
    
test_merge(test1, output1)
test_merge(test2, output2)
test_merge(test3, output2)