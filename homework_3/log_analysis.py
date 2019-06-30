# -*- coding: utf-8 -*-
import os
import sys
import re
import gzip
from collections import Counter
import json


class LogAnalysis:
    def __init__(self, path_log):
        self.path = path_log

    @staticmethod
    def read_file(path_log_file):
        """Read file from file system
        :return list with str from file"""
        if path_log_file.endswith('.gz'):
            with gzip.open(path_log_file, 'r') as f:
                return list(map(lambda x: x.decode('utf-8'), f.readlines()))
        else:
            with open(path_log_file, 'r', encoding='utf-8') as f:
                return f.readlines()

    @staticmethod
    def write_stats_as_json(result):
        """Write python dict as json to result.json"""
        file_result = "result.json"
        result_json = json.dumps(result, ensure_ascii=False)
        with open(file_result, 'w') as f:
            f.write(result_json)
        print("Result was write in ", file_result)

    @staticmethod
    def parse_apache_logs(files):
        logs_apache = []
        regex_apache = r'^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+)\s?(\S+)?\s?(\S+)?" (\d{3}|-) (\d+|-)\s?"?([^"]*)"?\s?"?([^"]*)?"?$'
        for file in files:
            try:
                res = LogAnalysis.read_file(file)
                logs_apache.extend(list(map(lambda line: re.match(regex_apache, line).groups(), res)))
            except:
                print("The file %s could not be processed." % file)
                sys.exit(1)
        return logs_apache

    @staticmethod
    def collect_statics(apache_log):
        stats = {}
        #Total number of queries executed
        total_query = len(apache_log)
        stats["total_query"] = total_query

        #Type query
        count_query_by_type = dict(Counter([qr[4] for qr in apache_log]))
        stats["query_by_type"] = count_query_by_type

        #TOP 10 ip address
        cnt = Counter(qr[0] for qr in apache_log)
        top_10_ip = dict(cnt.most_common(10))
        stats["top_10_ip"] = top_10_ip

        #TOP 10 long time query
        data_for_long_query = list(map(lambda line: {'time': int(line[8]), 'method': line[4], 'ip_address': line[0], 'url':line[5]}, apache_log))
        top_10_long_query = sorted(data_for_long_query, key = lambda x: x.get('time'), reverse=True)[:10]
        stats["top_10_long_query"] = top_10_long_query


        #TOP 10 client error
        data_client_error = list(filter(lambda x: x.get('status_code') >= 400 and x.get('status_code') < 500,
                                        map(lambda line: {'status_code': int(line[7]), 'method': line[4],
                                                          'ip_address': line[0], 'url': line[5]}, apache_log)))[:10]
        stats["top_10_client_error"] = data_client_error

        # TOP 10 server error
        data_server_error = list(filter(lambda x: x.get('status_code') >= 500,
                                        map(lambda line: {'status_code': int(line[7]), 'method': line[4],
                                                          'ip_address': line[0], 'url': line[5]}, apache_log)))[:10]
        stats["top_10_server_error"] = data_server_error

        return stats

    @staticmethod
    def get_list_file_from_folder(path):
        all_file = os.listdir(path)
        return [file for file in all_file if file.startswith('access')]

    @staticmethod
    def check_folder(path_dir):
        """
        :return True if folder
        :return False if file
        """
        return os.path.isdir(path_dir)

    def main(self):
        is_folder = self.check_folder(self.path)
        file_for_analysis = []
        if is_folder:
            result = self.get_list_file_from_folder(self.path)
            count = 0
            print("Please enter number of file or 'allLog'.")
            print(0, 'allLog')
            for res in result:
                count += 1
                print(count, res)
            try:
                user_choice = int(input('Your choice: '))
                if user_choice > count:
                    raise Exception
                else:
                    if user_choice == 0:
                        print('all files from directory will be analyzed')
                        allFiles = [self.path + file for file in result]
                        file_for_analysis.extend(allFiles)
                    else:
                        print('File was selected: ', result[user_choice-1])
                        file_for_analysis.append(self.path + result[user_choice-1])

            except:
                print('Incorrect format or file is not exists')
                sys.exit(1)
        else:
            file_for_analysis.append(self.path)

        apache_log = LogAnalysis.parse_apache_logs(file_for_analysis)
        stats = LogAnalysis.collect_statics(apache_log)
        LogAnalysis.write_stats_as_json(stats)


if __name__ == '__main__':
    parseLog = LogAnalysis('/var/log/apache2/')
    parseLog.main()
