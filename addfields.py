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
        
        # add new fields to header
        header.extend(field_list)
        
        # write out new header
        writer.writerow(header)

        # write out each row with appended empty new fields
        for row in reader:
            row.extend([''] * len(field_list))
            writer.writerow(row)

    # close files
    input.close()
    output.close()
    