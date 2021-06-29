import clamd

from six import BytesIO
from strelka import strelka


class ScanClam(strelka.Scanner):
    """Sends files to ClamAV.
       Working, needs tested against known bad file, delete commented code later
    """
    def scan(self, data, file, options, expire_at):

        try:

            try:
                cd = clamd.ClamdUnixSocket("/etc/clamysock/clamd.sock",None)

                #scan_result = cd.instream(BytesIO(clamd.EICAR))
                scan_result = cd.instream(BytesIO(data))

                #self.event['clamresults'] = scan_result
                #self.flags.append(scan_result['stream'][0])

                self.event['ClamResult'] = scan_result['stream'][0]
                self.event['ClamSignature'] = scan_result['stream'][1]



            except:
                self.flags.append('error_scanning')

        except:
            self.flags.append('error_processing')
            return

        #self.flags.append(str(scan_result))
