import sys
import csv
import argparse

if __name__ == '__main__':
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    parser.add_argument('-f', '--fields', required=True)
    args = parser.parse_args()
    
    # if input file was not provided, use stdin
    if args.input:
        input = open(args.input, 'r')
    else:
        input = sys.stdin

    # if output file was not provided, use stdout
    if args.output:
        output = open(args.output, 'w')
    else:
        output = sys.stdout
    
    # get comma delimited field list
    if args.fields:
        field_list = args.fields.split(',')

    writer = csv.writer(output, delimiter=',',
                        quoting=csv.QUOTE_ALL)

    with input as csvfile:
        reader = csv.reader(csvfile)
        header = reader.next()
        
        # create list to indicate which field indexes we want
        idx_list = []
        new_header = []
        for idx, field in enumerate(header):
            if field in field_list:
                idx_list.append(idx)
                new_header.append(field)

        # write out new header
        writer.writerow(new_header)

        # read each row and only write out the fields requested
        for row in reader:
            new_row = []
            for idx in idx_list:
                new_row.append(row[idx])
            writer.writerow(new_row)

    # close files
    input.close()
    output.close()
    