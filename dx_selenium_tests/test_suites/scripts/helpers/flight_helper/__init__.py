import os
import uuid
import csv
from lib.dx_date import DXDate

class FlightHelper(object):

    def read_csv(self, filename):
        self.datalist = []
        with open(os.path.dirname(__file__)+ '/../../../../data/flights_upload/' + filename + '.csv', 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            for reader in csvreader:
                self.datalist.append(reader)
            csvfile.close()

    def process_data(self, flight_payload = '', campaign=None):
        data = ''
        for line in self.datalist[1:]:
            if line[0] != '':
                if campaign:
                    line[0] = campaign.campaign_attributes['campaign_name']
                    line[1] = 'test-flight-' + str(uuid.uuid4())
                    line[8] = campaign.campaign_attributes['start_date']
                    line[9] = campaign.campaign_attributes['end_date']
                else:
                    line[0] = 'test-flight-'+str(uuid.uuid4()) + flight_payload
                    line[7] = DXDate().date_after_two_days()
                    line[8] = DXDate().last_date_of_current_month()
            data += '\n' + ",".join(line)
        self.data_to_write = ",".join(self.datalist[0]) + data

    def write_to_file(self, filename):
        csvfile = open(os.path.dirname(__file__)+ '/../../../../data/flights_upload/' + filename + '.csv', 'wb')
        csvfile.write(self.data_to_write)
        csvfile.close()
