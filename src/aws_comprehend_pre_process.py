import json
import sys

def write_file_after_process(input_path, output_path):
    with open(output_path, 'w', encoding='utf-8') as file_write:
        with open(input_path, 'r', encoding='utf-8') as file_read:
            for line in file_read.readlines():
                data = json.loads(line)
                keywords = [d['Text'] for d in data['KeyPhrases']]
                file_write.write(",".join(keywords)+'\n')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ['test', 'all']:
            # test keyword extraction process
            write_file_after_process('./data/test/output', './data/test/keywords.txt')
        if arg in ['train', 'all']:
            # train keyword extraction process
            write_file_after_process('./data/train/output', './data/train/keywords.txt')