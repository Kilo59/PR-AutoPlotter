#DemoFunctions
def variance(number_list, average):
    variance = 0
    for number in number_list:
        variance += (average - number) ** 2

    result = variance / len(number_list)
    return result

def std_dev(variance):
    result = variance ** 0.5 #Sqrt(variance)
    return result

def remove_duplicates(Items):
    ItemsNoDuplicates = []
    for i in Items:
        if i not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(i)
    return ItemsNoDuplicates

def distinct_items(item_list):
    distinct_list = remove_duplicates(item_list)
    result = len(distinct_list)
    return result

#arg = filename without .extension
def read_text(arg):
    file_name = arg +'.txt'

    r = open(file_name, 'r')
    text_string = (r.read())
    r.close()
    return text_string

def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1
    return count

def reverse(text):
    RevWord = ''
    pos = len(text) - 1
    while pos >= 0:
        RevWord += text[pos]
        pos -= 1
    return  RevWord

def complement(Nucleotides):
    comp = ''
    index = 0
    nucleotide_list = ['A', 'T', 'G', 'C']
    for base in Nucleotides:
        #print(base)
        if Nucleotides[index] == 'A':
            comp += 'T'
        elif Nucleotides[index] == 'T':
            comp += 'A'
        elif Nucleotides[index] == 'G':
            comp += 'C'
        elif Nucleotides[index] == 'C':
            comp += 'G'
        elif Nucleotides[index] not in nucleotide_list:
            print('Invalid Nucleotide')
        else:
            print('Error')
        index = index + 1
    return comp

def ReverseComplement(Pattern):
    revComp = complement(reverse(Pattern))
    return revComp

#print(ReverseComplement('ACT'))
#print(ReverseComplement('AGT'))

'''
print(PatternCount('GCG', 'GCGCG'))

genomeList = ['t_petrophila_oriC', 'Vibrio_cholerae']
patternList = ['AACT', 'AATGAG', 'ACAATGAG']

genomeDict = {}

pattern_match_list = []
for genome in genomeList:
    #genome = []
    print(genome)
    for pattern in patternList: #pattern match on the sequence and reverseComplement of sequence
        pattern_match = 0
        pattern_match += PatternCount(pattern, read_text(genome))
        pattern_match += PatternCount(ReverseComplement(pattern), genome)
        pattern_match_list.append(pattern_match)
        #genList.append(pattern_match)

print(pattern_match_list)
#print(t_petrophila_oriC)
'''
